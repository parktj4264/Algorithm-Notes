#%% ============================================================================
"""
01_BigO_Loop — Big-O & Interpreter Overhead (실험 프로토콜 포함 .py)

목표
- Big-O(증가율)라는 '체급' 위에, CPython의 인터프리터 오버헤드/객체(Boxing)/메모리 접근(Locality)이
  어떻게 상수항(C)을 키우는지 실험으로 확인한다.
- 결론은 감이 아니라 "측정값 + 스케일링 + 증거(바이트코드/메모리 크기)"로 작성한다.

측정 규약(Benchmark Protocol)
1) time.perf_counter() 기반 반복 측정(표본)으로 mean/min 기록
2) 보조로 timeit.repeat()의 min(best-case)로 크로스체크
3) 노이즈 억제:
   - tight loop 측정 시 gc.disable() 옵션 제공 (측정 구간의 GC 노이즈 감소)
   - 너무 작은 N은 OS 스케줄링/터보부스트/캐시 효과로 노이즈가 커서, 최소 수십~수백 ms는 나오게 조절

실험 구성
Experiment 0 — 동일 O(N)에서도 상수항(C) 차이가 체감 성능을 가른다
- (A) for + indexing: for i in range(len(a)): s += a[i]
- (B) for + iteration: for x in a: s += x
- (C) builtin sum: sum(a)  (C-level 루프 경로)
가설:
- 보통 (B)가 (A)보다 유리(인덱싱 오버헤드 감소)
- (C)는 루프 자체가 C에서 돌아서 인터프리터 반복 비용이 크게 줄어들 수 있음

Experiment 1 — comprehension이 더 빠른 이유를 "증거"로 보기
- (A) out=[]; for x in a: out.append(x*x)
- (B) [x*x for x in a]
확장:
- dis.dis()로 바이트코드 비교 (attribute lookup/method call overhead 등 관찰)

Experiment 2 — O(N^2) 스케일링의 잔혹함(=Big-O의 얼굴)
- 이중 루프 workload로 n을 2배로 늘렸을 때 시간 배율이 ~4로 가는지 관찰
- 작은 n에서는 노이즈로 이상적 비율과 다를 수 있으나, n이 커질수록 증가율이 드러나는지 확인

Experiment 3 — Boxing/Locality 감각: list[int] vs array('I')
- list는 포인터 배열(원소는 PyObject) / array('I')는 C primitive contiguous storage
- sys.getsizeof로 컨테이너/원소의 대략적 오버헤드 감각화
- sum(list) vs sum(array) 비교 (단, sum도 내부 구현/경로에 따라 결과가 달라질 수 있음)

Experiment 4 — timeit(min)으로 결과를 재현 가능하게 고정
- Experiment 0의 핵심 비교(B vs C)를 timeit.repeat(min)으로 크로스체크

실험 후 작성할 결론(템플릿)
1) 동일 O(N)이라도 상수항(인터프리터 반복 비용/인덱싱/메서드 호출)이 결과를 갈라놓는다.
2) O(N^2)은 N이 조금만 커져도 게임 오버다. 최적화는 미시보다 구조(Big-O)부터.
3) list는 pointer chasing 구조라 대용량 수치 연산은 contiguous primitive 구조(예: numpy)로 내려야 한다.
"""
#%% ============================================================================

import sys
import time
import gc
import statistics as stats
import timeit
import dis
from array import array
from typing import Callable, List, Tuple, Any

print("done importing modules.")




#%% [공통] 벤치마크 유틸리티
def bench(fn: Callable[[], Any], repeat: int = 7, gc_disable: bool = True) -> Tuple[float, float, List[float]]:
    """
    perf_counter 기반 벤치.
    - repeat회 실행한 시간을 샘플로 수집
    - mean과 min을 리턴 (min은 OS 간섭이 적은 best-case 근사치)
    - gc_disable=True면 측정 구간에서 GC를 끄고 노이즈를 줄인다.
    """
    samples: List[float] = []

    if gc_disable:
        was_enabled = gc.isenabled()
        gc.disable()
    else:
        was_enabled = None

    try:
        for _ in range(repeat):
            t0 = time.perf_counter()
            fn()
            t1 = time.perf_counter()
            samples.append(t1 - t0)
    finally:
        if gc_disable and was_enabled:
            gc.enable()

    return stats.mean(samples), min(samples), samples


def print_bench(name: str, result: Tuple[float, float, List[float]]) -> None:
    mean_t, min_t, samples = result
    print(f"{name:>22} | mean={mean_t:.6f}s  min={min_t:.6f}s  samples={[round(x, 6) for x in samples]}")


def timeit_min(stmt: str, setup: str, repeat: int = 7, number: int = 1) -> float:
    """
    timeit.repeat의 여러 샘플 중 최소값(min)을 사용한다.
    - 환경 노이즈가 있을 때 min은 best-case 근사치로 유용하다.
    """
    samples = timeit.repeat(stmt=stmt, setup=setup, repeat=repeat, number=number)
    return min(samples)


#%% [데이터 준비] (환경에 따라 N을 조절)
# 너무 크면 느리고, 너무 작으면 노이즈가 커진다.
N = 2_000_000
a = list(range(N))


#%% ============================================================================
# Experiment 0 — 동일 O(N)에서 상수항(C) 차이 관찰
# ============================================================================

def sum_indexing() -> int:
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s


def sum_iteration() -> int:
    s = 0
    for x in a:
        s += x
    return s


def sum_builtin() -> int:
    return sum(a)


print("=== Experiment 0: O(N) 이지만 상수항(C)이 다르면 결과가 갈린다 ===")
print_bench("for + indexing", bench(sum_indexing))
print_bench("for + iteration", bench(sum_iteration))
print_bench("builtin sum", bench(sum_builtin))

# 정확성 체크(벤치 전에/후에 한 번 정도만)
x1 = sum_indexing()
x2 = sum_iteration()
x3 = sum_builtin()
print("correctness:", x1 == x2 == x3)


# 최대한 sum, min, max 같은 **내장 함수(Built-in Function)**나, 나중에 배울 NumPy 처럼 C로 짜인 도구들에게 일을 떠넘겨야 해. 내가 직접 for문 짜는 순간, 그건 '느린 길'로 들어서는 거야.


#%% ============================================================================
# Experiment 1 — list comprehension vs loop+append (+ 바이트코드 증거)
# ============================================================================

# 전체 a를 쓰면 너무 길 수 있으니 일부만 사용
SLICE_N = 200_000


def square_loop_append():
    out = []
    for x in a[:SLICE_N]:
        out.append(x * x)
    return out


def square_list_comp():
    return [x * x for x in a[:SLICE_N]]


print("\n=== Experiment 1: comprehension vs loop+append (모두 O(N)) ===")
print_bench("loop + append", bench(square_loop_append))
print_bench("list comp", bench(square_list_comp))

print("\n--- Bytecode 증거: loop+append ---")
dis.dis(square_loop_append)
print("\n--- Bytecode 증거: list comp ---")
dis.dis(square_list_comp)


#%% ============================================================================
# Experiment 2 — O(N^2) 스케일링: n을 2배로 하면 시간이 ~4배로 가는가?
# ============================================================================

def pair_sum_naive(n: int) -> int:
    """
    인위적 O(N^2) workload.
    n이 조금만 커져도 매우 느려질 수 있다. (실험의 의도)
    """
    s = 0
    for i in range(n):
        for j in range(n):
            s += i * j
    return s


def scaling_test(ns=(200, 400, 800), repeat=3):
    rows = []
    for n in ns:
        mean_t, min_t, _ = bench(lambda: pair_sum_naive(n), repeat=repeat)
        rows.append((n, mean_t, min_t))
        print(f"n={n:>5} | mean={mean_t:.4f}s | min={min_t:.4f}s")
    return rows


print("\n=== Experiment 2: O(N^2) scaling ===")
rows = scaling_test(ns=(200, 400, 800), repeat=3)

print("\n--- Scaling ratios (mean 기준) ---")
for (n1, t1, _), (n2, t2, _) in zip(rows, rows[1:]):
    ratio_n = n2 / n1
    ratio_t = t2 / t1
    print(f"n: {n1}->{n2} (x{ratio_n:.1f})  time ~ x{ratio_t:.2f}  ideal O(N^2): x{ratio_n**2:.2f}")


#%% ============================================================================
# Experiment 3 — Boxing/Locality 감각: list[int] vs array('I')
# ============================================================================

print("\n=== Experiment 3: memory + sum speed (list vs array) ===")
small = list(range(10_000))
arr = array('I', small)  # C unsigned int contiguous

# 컨테이너와 원소 오버헤드 감각화
print("sizeof(list container):", sys.getsizeof(small))
print("sizeof(array container):", sys.getsizeof(arr))
print("sizeof(one int object):", sys.getsizeof(1))

# list는 원소 자체가 포인터 배열(대개 64-bit면 8 bytes/slot)이고
# 실제 int 객체는 힙에 따로 존재한다. 아래는 '포인터 슬롯'만 대략 추정.
ptr_size = 8 if sys.maxsize > 2**32 else 4
print("approx list pointer slots bytes (rough):", len(small) * ptr_size)

def sum_list_small():
    return sum(small)

def sum_array_small():
    return sum(arr)

print_bench("sum(list[int])", bench(sum_list_small))
print_bench("sum(array('I'))", bench(sum_array_small))


#%% ============================================================================
# Experiment 4 — timeit(min)로 결과 고정(재현 가능성 강화)
# ============================================================================

print("\n=== Experiment 4: timeit min(repeat) cross-check ===")
setup_code = "from __main__ import a"

t_for_iter = timeit_min(
    stmt="s=0\nfor x in a: s+=x",
    setup=setup_code,
    repeat=7,
    number=1
)
t_builtin = timeit_min(
    stmt="sum(a)",
    setup=setup_code,
    repeat=7,
    number=1
)

print(f"timeit min | for-iter: {t_for_iter:.6f}s")
print(f"timeit min | builtin : {t_builtin:.6f}s")


#%% ============================================================================
# 실험 후 요약(직접 채우기)
# ============================================================================
"""
[결과 요약 작성]
1) Experiment 0:
   - for+indexing vs for+iteration vs builtin sum의 순위/격차를 기록
   - 결론: 동일 O(N)이라도 상수항(인터프리터 반복 비용/인덱싱 비용)이 결과를 갈라놓음

2) Experiment 1:
   - loop+append vs list comp 비교 + dis 결과를 근거로 해석
   - 결론: 못 피하는 루프라면, 반복 비용을 줄이는 구조가 유리

3) Experiment 2:
   - n을 2배로 했을 때 time ratio가 얼마나 증가하는지 기록
   - 결론: O(N^2)은 N이 조금만 커져도 현실적으로 불가능해짐 → 알고리즘 구조 변경이 우선

4) Experiment 3:
   - getsizeof/포인터 슬롯 추정/합산 속도를 보고 boxing/locality 모델을 강화
   - 결론: list는 pointer chasing 구조. 대규모 수치 연산은 contiguous primitive 구조로 내려야 함

5) Experiment 4:
   - timeit min(repeat) 결과로 핵심 비교를 고정


---

Experiment 0: 파이썬 for문은 인터프리터 오버헤드 때문에 느리다. (닥치고 Built-in 써라)Experiment 1: Loop보다 **Comprehension**이 빠른 이유는 Bytecode(전용 명령어) 덕분이다.Experiment 2: **$O(N^2)$**은 $N$이 조금만 커져도 재앙이다. (이중 루프 금지)Experiment 3: List는 메모리 돼지지만 빠르고, Array는 날씬하지만 Boxing 때문에 느리다. (그래서 NumPy가 짱이다)


1. 🐢 인터프리터 오버헤드 (Interpreter Overhead)
상황: for문 돌 때마다 파이썬이 한 줄씩 통역하는 상황.
비유: "동시 통역 비용"
R(sum)이나 C언어는 한국인끼리 말해서 0.1초면 알아듣는데,
파이썬 for문은 "영어 → 한국어 통역사" 거치느라 한 마디 할 때마다 1초씩 까먹음.
이 '통역사 부르는 비용'이 바로 오버헤드.
해결: Built-in (내장 함수) 쓰면 통역사 없이 그냥 **바디랭귀지(C언어)**로 바로 통함.

2. 📜 바이트코드 (Bytecode) & 컴프리헨션
상황: list.append() 대신 [x for x in a] 쓰는 게 빠른 이유.
비유: "작업 지시서(SOP)"
Loop: 작업자한테 "야, 매뉴얼 3페이지 펴서... append 찾아서... 실행해." (매번 찾음)
Comprehension: 작업자한테 "야! 묻지 말고 그냥 다 집어넣어!" 라고 전용 코드(LIST_APPEND) 발급.
파이썬 가상머신(PVM)이 읽는 '기계어 직전의 언어'가 바이트코드임.

"""
