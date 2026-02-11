#%% ============================================================================
# 02_List_Evolution.py
# 주제: [Chapter 5] Dynamic Array (List) & Memory Allocation
# 목표: 파이썬 리스트의 '이사 비용(Doubling)'과 '끼어들기(Shift)'의 비용을 눈으로 확인한다.
# ============================================================================
import sys
import time
import dis
import timeit

# 벤치마킹용 헬퍼 함수
def bench(func, number=1):
    # number: 한 번 실행할 때 루프 횟수 (여기선 함수 안에서 루프 도니까 1로 설정)
    times = timeit.repeat(stmt=func, repeat=5, number=number)
    return min(times) # 노이즈 제거를 위해 최소값 사용

def print_bench(name, t):
    print(f"{name:>25} | {t:.6f}s")

#%% ============================================================================
# Experiment 1 — The Doubling Strategy (이사 비용 확인)
# ----------------------------------------------------------------------------
# [수정] 매 스텝마다 메모리 변화를 출력해서 '계단식 성장'을 눈으로 확인합니다.
# 평지(Flat): O(1) 구간 / 점프(Jump): Resize 구간
# ============================================================================

print("\n=== Experiment 1: Doubling Strategy (Memory Allocation) ===")

data = []
old_size = sys.getsizeof(data)

print(f"{'Length':<10} | {'Size(bytes)':<15} | {'Status'}")
print("-" * 50)

# 0부터 40까지만 넣어봐도 패턴 보임
for i in range(40):
    data.append(i)
    new_size = sys.getsizeof(data)
    
    if new_size > old_size:
        # 🔥 이사 발생 (Capacity Doubling)
        growth = new_size - old_size
        print(f"{len(data):<10} | {new_size:<15} | 🔥 RESIZE (+{growth})")
        old_size = new_size
    else:
        # 🧊 평온함 (Amortized O(1))
        # 방이 남아돌아서 메모리 변화 없음
        print(f"{len(data):<10} | {new_size:<15} |  -")

print("\n>> 분석: '-' 구간이 바로 '공짜(O(1))'로 데이터를 넣는 구간입니다.")
print(">> 분석: 데이터가 쌓일수록 '공짜 구간'이 점점 길어지는 게 보이나요?")
print(">> 결론: 이게 바로 'Amortized O(1)'의 시각적 증거입니다.")


#%% ============================================================================
# Experiment 2 — Head vs Tail: O(1) vs O(N)의 재앙
# ----------------------------------------------------------------------------
# R의 vector나 Python의 list나 똑같습니다.
# "맨 뒤"에 붙이는 건 빠르지만, "맨 앞"에 넣으면 전체가 뒤로 밀려납니다(Shift).
# ============================================================================

N = 50_000  # 5만 개만 해도 차이가 극명함

def append_tail():
    """맨 뒤에 추가 (Fast)"""
    lst = []
    for i in range(N):
        lst.append(i)  # O(1)
    return lst

def insert_head():
    """맨 앞에 추가 (Slow - Disaster)"""
    lst = []
    for i in range(N):
        lst.insert(0, i)  # O(N) -> 전체 반복시 O(N^2)
    return lst

print(f"\n=== Experiment 2: append(end) vs insert(0) (N={N}) ===")

# 1. Tail Append
t_tail = bench(append_tail, number=1)
print_bench("append(tail) O(1)", t_tail)

# 2. Head Insert
t_head = bench(insert_head, number=1)
print_bench("insert(head) O(N)", t_head)

ratio = t_head / t_tail
print(f"\n>> 결과: insert(0)가 약 {ratio:.1f}배 느림!")
print(">> 교훈: 큐(Queue)처럼 쓰고 싶으면 list 말고 'collections.deque'를 써야 합니다.")


#%% ============================================================================
# Experiment 3 — Evolution: Loop vs List Comprehension
# ----------------------------------------------------------------------------
# "파이썬스럽다(Pythonic)"라는 건 단순히 짧은 게 아니라,
# 내부적으로 최적화된 바이트코드(LIST_APPEND)를 쓴다는 뜻입니다.
# ============================================================================

N_COMP = 500_000
sample_data = list(range(N_COMP))

def loop_filter_map():
    """Legacy Style: 짝수만 골라서 제곱하기"""
    res = []
    for x in sample_data:
        if x % 2 == 0:
            res.append(x * x)
    return res

def comp_filter_map():
    """Modern Style: List Comprehension"""
    return [x * x for x in sample_data if x % 2 == 0]

print(f"\n=== Experiment 3: Loop vs Comprehension (N={N_COMP}) ===")

t_loop = bench(loop_filter_map, number=10)
t_comp = bench(comp_filter_map, number=10)

print_bench("Loop + append", t_loop)
print_bench("Comprehension", t_comp)

speedup = (t_loop / t_comp - 1) * 100
print(f"\n>> 결과: Comprehension이 Loop보다 약 {speedup:.1f}% 빠름")


#%% ============================================================================
# Experiment 4 — Bytecode Deep Dive (Why fast?)
# ----------------------------------------------------------------------------
# 눈으로 확인하는 증거. LOAD_METHOD vs LIST_APPEND
# ============================================================================
print("\n=== Experiment 4: Bytecode Analysis ===")

print("\n[1] Loop Bytecode (Look at LOAD_METHOD 'append')")
dis.dis(loop_filter_map)

print("\n" + "="*40 + "\n")

print("[2] Comprehension Bytecode (Look at LIST_APPEND)")
dis.dis(comp_filter_map)

print("\n>> 핵심: Loop는 'append'라는 이름을 매번 찾고(LOAD_METHOD),")
print(">> Comprehension은 'LIST_APPEND'라는 전용 기계어로 바로 꽂아 넣습니다.")