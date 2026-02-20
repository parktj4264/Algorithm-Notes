#%% ============================================================================
# 05_String_Prep.py
# 주제: [Chapter 6] Immutable Object & String Interning
# 목표: 문자열의 불변성(Immutability) 확인 및 O(N^2) 메모리 파편화를 막는 join() 체화
# ============================================================================
import time
import sys
import re

# 벤치마킹용 헬퍼 함수
def bench(func, repeat=3, number=1):
    import timeit
    times = timeit.repeat(stmt=func, repeat=repeat, number=number)
    return min(times)

def print_bench(name, t):
    print(f"{name:>25} | {t:.6f}s")

#%% ============================================================================
# Experiment 1 — String Interning & Immutability (메모리 주소 확인)
# ----------------------------------------------------------------------------
# 파이썬은 똑같은 문자열을 여러 번 만들지 않고 "돌려 씁니다" (Interning).
# 그리고 문자열을 수정하면 원래 놈이 바뀌는 게 아니라 "새로" 태어납니다 (Immutable).
# ============================================================================
print("\n=== Experiment 1: Interning & Immutability ===")

a = "Wafer_01"
b = "Wafer_01"

print(f"a의 메모리 주소: {id(a)}")
print(f"b의 메모리 주소: {id(b)}")
print(f"a is b ? -> {a is b}")  
# True! 완전히 같은 메모리를 가리킴 (메모리 절약 개꿀)

print("\n[문자열 수정 시도]")
old_id = id(a)
a += "_FAIL"  # 문자열을 수정해 보자!

print(f"수정 후 a의 주소: {id(a)}")
print(f"주소가 바뀌었나? -> {old_id != id(a)}")
print(">> 분석: 파이썬에서 문자열은 '불변(Immutable)'입니다. ")
print(">> += 연산은 기존 문자열을 고치는 게 아니라, 아예 새로운 객체를 만들어서 갈아끼우는 겁니다.")


#%% ============================================================================
# Experiment 2 — The Disaster of `+` vs The Magic of `join()`
# ----------------------------------------------------------------------------
# 현업에서 텍스트 합칠 때 `+`를 쓰면 안 되는 결정적 이유.
# ============================================================================
print("\n=== Experiment 2: String Concatenation (+ vs join) ===")

N = 300_000  # 30만 개 합치기
chars = ["A"] * N

def concat_plus():
    """하수: += 로 계속 이어 붙이기 (O(N^2)의 재앙)"""
    s = ""
    for c in chars:
        s += c  # 매번 새로운 집(메모리) 계약해서 이사 감
    return s

def concat_join():
    """고수: 리스트에 담아두고 한방에 join (O(N)의 기적)"""
    # chars 리스트 전체 길이를 미리 재고, 딱 한 번만 메모리 할당함
    return "".join(chars)

t_plus = bench(concat_plus, number=1)
t_join = bench(concat_join, number=1)

print_bench("s += c (O(N^2))", t_plus)
print_bench("\"\".join (O(N))", t_join)

speedup = t_plus / t_join
print(f"\n>> 결과: join()이 + 연산보다 약 {speedup:,.0f}배 압도적으로 빠름!")
print(">> 교훈: 문자열을 반복해서 합칠 때는 무조건 리스트에 모은 다음 마지막에 join()을 때리세요.")

# 시각적 이해를 돕기 위한 이미지
# 


#%% ============================================================================
# Experiment 3 — 필수 전처리 메서드 4대장
# ----------------------------------------------------------------------------
# 불량 로그나 MSR 데이터 파싱할 때 숨 쉬듯 쓰는 녀석들
# ============================================================================
print("\n=== Experiment 3: Essential String Methods ===")

raw_log = "   FAIL_Wafer-001_Particle_Error_Code_404   \n"
print(f"Raw: '{raw_log}'")

# 1. strip(): 앞뒤 쓸데없는 공백/줄바꿈 날리기 (R의 trimws)
clean_log = raw_log.strip()
print(f"1. strip()   : '{clean_log}'")

# 2. split(): 특정 구분자로 쪼개서 '리스트'로 반환 (R의 strsplit)
log_parts = clean_log.split("_")
print(f"2. split('_'): {log_parts}")

# 3. replace(): 단순 치환
fixed_log = clean_log.replace("-", "_")
print(f"3. replace() : '{fixed_log}'")

# 4. upper() / lower(): 대소문자 통일
print(f"4. lower()   : '{fixed_log.lower()}'")


#%% ============================================================================
# Experiment 4 — 정규식(Regex)을 활용한 우아한 데이터 클렌징
# ----------------------------------------------------------------------------
# replace로 감당 안 되는 복잡한 패턴 밀어버리기
# ============================================================================
print("\n=== Experiment 4: Regex (re 모듈) ===")

messy_data = "Wafer_Yield: 0.98!! (Note: Check machine #3) => Status: PASS"

# 목표: 알파벳, 숫자, 점(.) 빼고 특수문자 싹 다 날리기
# [^ ... ] : ... 를 제외한 나머지라는 뜻
clean_data = re.sub(r'[^a-zA-Z0-9.\s]', '', messy_data)

print(f"원본: {messy_data}")
print(f"정제: {clean_data}")
print(">> 분석: 데이터 분석 직전(pre)에 쓰레기 텍스트 날려버릴 때 re.sub()가 직빵입니다.")