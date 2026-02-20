#%% ============================================================================
# 03_Dict_Set_Essential.py
# 주제: [Chapter 5] Hash Table Implementation
# 목표: O(1) 검색의 위력 확인 및 파이썬의 우아한 카운팅 기법(Counter) 체화
# ============================================================================
import sys
import time
from collections import defaultdict, Counter

# 벤치마킹용 헬퍼 함수
def bench(func, repeat=3, number=1):
    import timeit
    times = timeit.repeat(stmt=func, repeat=repeat, number=number)
    return min(times)

def print_bench(name, t):
    print(f"{name:>25} | {t:.6f}s")

#%% ============================================================================
# Experiment 1 — The Power of O(1): List vs Set 검색 속도
# ----------------------------------------------------------------------------
# 현업에서 "이 데이터가 로그에 있나?" 찾을 때 List를 쓰면 서버가 터집니다.
# ============================================================================
print("\n=== Experiment 1: Search Speed (List vs Set) ===")

N = 10_000_000  # 1,000만 개 데이터
print(f"데이터 {N:,}개 생성 중... (잠시 대기)")

large_list = list(range(N))
large_set = set(large_list)  # 리스트를 해시 테이블(Set)로 변환

# 찾으려는 타겟 (최악의 시나리오: 맨 끝에 있거나 아예 없는 경우)
target = N - 1  
missing_target = -1

def search_list(): return target in large_list      # O(N)
def search_set(): return target in large_set        # O(1)
def search_list_miss(): return missing_target in large_list  # O(N)
def search_set_miss(): return missing_target in large_set    # O(1)

print("\n[Target이 존재하는 경우 (맨 끝)]")
t_list = bench(search_list, number=10)
t_set = bench(search_set, number=10)
print_bench("List Search O(N)", t_list)
print_bench("Set Search O(1)", t_set)
print(f"👉 Set이 List보다 약 {t_list / t_set:,.0f}배 빠름!")

print("\n[Target이 아예 없는 경우 (최악의 탐색)]")
t_list_miss = bench(search_list_miss, number=10)
t_set_miss = bench(search_set_miss, number=10)
print_bench("List Miss O(N)", t_list_miss)
print_bench("Set Miss O(1)", t_set_miss)

print("\n>> 분석: List는 1,000만 개를 다 뒤져보고 '없네' 하지만,")
print(">> Set은 해시 함수로 단번에 주소를 계산해서 '이 방 비어있네? 그럼 없는 거임' 하고 끝냅니다.")


#%% ============================================================================
# Experiment 2 — Dict의 기본과 안전한 조회 (get)
# ----------------------------------------------------------------------------
# KeyError로 프로그램이 뻗는 걸 막아주는 우아한 방법
# ============================================================================
print("\n=== Experiment 2: Dictionary Safe Access ===")

wafer_yields = {"Wafer_A": 0.98, "Wafer_B": 0.95, "Wafer_C": 0.99}

# 1. 일반적인 조회 (위험)
print("Wafer_A 수율:", wafer_yields["Wafer_A"])

# print(wafer_yields["Wafer_D"])  # 🚨 주석 풀면 KeyError 발생! 프로그램 사망.

# 2. 안전한 조회 (현업 권장)
# get(key, default_value) -> 키가 없으면 에러 대신 디폴트값을 반환
print("Wafer_D 수율 (get):", wafer_yields.get("Wafer_D", "데이터 없음"))


#%% ============================================================================
# Experiment 3 — Evolution: defaultdict & Counter
# ----------------------------------------------------------------------------
# R의 `table()` 함수를 파이썬에서 가장 깔끔하게 구현하는 방법
# ============================================================================
print("\n=== Experiment 3: defaultdict & Counter ===")

# 반도체 불량 로그 데이터 (예시)
defects = ['Scratch', 'Particle', 'Particle', 'Crack', 'Scratch', 'Particle', 'Void']

# [하수 버전] 생짜 Dict 사용
counts_basic = {}
for defect in defects:
    if defect not in counts_basic:
        counts_basic[defect] = 0
    counts_basic[defect] += 1
print(f"Basic Dict : {counts_basic}")

# [중수 버전] defaultdict 사용 (KeyError 방지)
counts_default = defaultdict(int)  # 기본값을 정수(0)로 세팅
for defect in defects:
    counts_default[defect] += 1    # 조건문 없이 그냥 더하면 됨!
print(f"DefaultDict: {dict(counts_default)}")

# [고수 버전] Counter 사용 (R의 table() 완벽 대체)
counts_counter = Counter(defects)
print(f"Counter    : {counts_counter}")

# 빈도수 높은 Top 2 불량 추출 (데이터 분석 시 개꿀)
print(f"Top 2 불량 : {counts_counter.most_common(2)}")


#%% ============================================================================
# Experiment 4 — Hash의 실체 (id vs hash)
# ----------------------------------------------------------------------------
# 파이썬이 문자열이나 숫자를 어떻게 "방 번호"로 바꾸는지 확인
# ============================================================================
print("\n=== Experiment 4: What is Hash? ===")

name1 = "Taejun"
name2 = "Taejun"
number = 100

print(f"hash('Taejun') : {hash(name1)}")
print(f"hash(number)   : {hash(number)}")  # 정수의 해시값은 보통 자기 자신

# 이 해시값을 딕셔너리의 현재 크기(예: 8)로 나눈 나머지가 실제 메모리 방 번호가 됨
# index = hash("Taejun") % 8
print(f"\n>> 'Taejun'이 들어갈 딕셔너리 방 번호 (크기 8 기준): {hash(name1) % 8}")