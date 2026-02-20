#%% ============================================================================
# 04_Loop_Upgrade.py
# 주제: [Chapter 5] Generator & Lazy Evaluation
# 목표: Pythonic한 루프(enumerate, zip) 작성법과 메모리를 구원하는 '게으름'의 미학 체화
# ============================================================================
import sys
import time

# 벤치마킹용 헬퍼 함수
def bench(func, repeat=3, number=1):
    import timeit
    times = timeit.repeat(stmt=func, repeat=repeat, number=number)
    return min(times)

def print_bench(name, t):
    print(f"{name:>25} | {t:.6f}s")

#%% ============================================================================
# Experiment 1 — range(len(a)) vs enumerate(a)
# ----------------------------------------------------------------------------
# C언어나 R 스타일의 인덱싱 접근은 이제 그만.
# 파이썬은 값과 인덱스를 동시에 뱉어주는 우아한 도구가 있습니다.
# ============================================================================
print("\n=== Experiment 1: enumerate ===")

N = 1_000_000
data = list(range(N))

def loop_c_style():
    """하수: 인덱스로 접근해서 값을 또 찾음"""
    s = 0
    for i in range(len(data)):
        s += data[i]  # 배열을 한 번 더 찔러야 함 (Overhead)
    return s

def loop_pythonic():
    """고수: enumerate로 한방에 뽑음"""
    s = 0
    for i, val in enumerate(data):
        s += val
    return s

t_c = bench(loop_c_style, number=10)
t_py = bench(loop_pythonic, number=10)

print_bench("range(len(data))", t_c)
print_bench("enumerate(data)", t_py)
print("\n>> 분석: enumerate가 미세하게 더 빠르거나 비슷하지만, 가독성과 파이썬 내부 최적화 관점에서 무조건 승리.")


#%% ============================================================================
# Experiment 2 — Parallel Iteration: Index vs zip
# ----------------------------------------------------------------------------
# 두 개의 리스트(예: 웨이퍼 ID와 수율)를 짝지어서 돌릴 때의 정석.
# ============================================================================
print("\n=== Experiment 2: zip ===")

wafer_ids = [f"W_{i}" for i in range(N)]
yields = [0.99] * N

def zip_c_style():
    """하수: 같은 인덱스로 두 배열을 각각 찌름"""
    count = 0
    for i in range(len(wafer_ids)):
        w_id = wafer_ids[i]
        y = yields[i]
        count += 1
    return count

def zip_pythonic():
    """고수: zip으로 옷 지퍼 올리듯 두 개를 맞물려서 뽑음"""
    count = 0
    for w_id, y in zip(wafer_ids, yields):
        count += 1
    return count

t_zip_c = bench(zip_c_style, number=5)
t_zip_py = bench(zip_pythonic, number=5)

print_bench("Index Access (C-style)", t_zip_c)
print_bench("zip (Pythonic)", t_zip_py)
print("\n>> 분석: zip은 파이썬 C-API 내부에서 튜플을 묶어주기 때문에 인덱스 접근보다 오버헤드가 적음.")


#%% ============================================================================
# Experiment 3 — The Magic of Lazy Evaluation (메모리 아끼기)
# ----------------------------------------------------------------------------
# List Comprehension (Eager) vs Generator Expression (Lazy)
# 데이터 1,000만 개를 메모리에 다 올릴 것인가, 설계도만 그릴 것인가?
# ============================================================================
print("\n=== Experiment 3: Eager vs Lazy (Memory) ===")

SIZE = 10_000_000

# 1. Eager (탐욕스러운 방식): 리스트 컴프리헨션
print("1. List Comprehension 생성 중... (메모리에 1,000만 개 적재 중)")
eager_list = [x for x in range(SIZE)]
print(f"-> Eager List 메모리: {sys.getsizeof(eager_list):,} Bytes (약 {sys.getsizeof(eager_list)/1024/1024:.1f} MB)")

# 2. Lazy (게으른 방식): 제너레이터 표현식
print("\n2. Generator Expression 생성 중... (데이터 안 만들고 대기 중)")
lazy_gen = (x for x in range(SIZE))
print(f"-> Lazy Generator 메모리: {sys.getsizeof(lazy_gen):,} Bytes")

print("\n>> 분석: 80MB vs 100 Bytes. 제너레이터는 100억 개를 돌려도 메모리가 100바이트 언저리 고정입니다.")
print(">> 이유: 제너레이터는 '어떻게 만드는지(Rule)'만 기억하고, next()로 부를 때만 하나씩 생산하기 때문!")


#%% ============================================================================
# Experiment 4 — yield 실전 응용 (가상의 대용량 로그 전처리)
# ----------------------------------------------------------------------------
# 수백 GB의 MSR 데이터를 읽을 때, 메모리를 지키면서 전처리(pre)하는 법
# ============================================================================
print("\n=== Experiment 4: Custom Generator with yield ===")

def process_huge_log_mock():
    """가상의 대용량 로그 파일 제너레이터"""
    print("  [Generator] 파일 열기 (가상)")
    for i in range(1, 4):
        print(f"  [Generator] {i}번째 줄 읽어서 가공 중...")
        # 전처리 결과물 변수명: pre (prepro 아님)
        pre_data = f"Processed_Log_Line_{i}"
        
        # return 대신 yield를 쓰면 여기서 데이터를 던져주고 함수가 일시정지(Pause)됨
        yield pre_data 
        
    print("  [Generator] 파일 닫기 (가상)")

# 제너레이터 루프 돌리기
print("\n>> 데이터 전처리 루프 시작:")
log_stream = process_huge_log_mock()

for line in log_stream:
    print(f"<- [Main] 받은 데이터: {line}")
    time.sleep(0.5)  # 0.5초 대기 (데이터 하나 처리하는 데 걸리는 시간 가정)

print("\n>> 분석: Main 루프와 Generator가 핑퐁(Ping-Pong) 하듯 데이터를 하나씩 주고받음.")
print(">> 현업 적용: 용량이 아무리 커도 한 줄 단위로 처리하므로 절대 메모리가 터지지 않음.")