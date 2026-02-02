# 🐍 00_Pythonic_Basic: R 유저를 위한 파이썬 기초 체력 & CS 이론

> **Target:** R(Vector, data.table)에 익숙하지만, 파이썬의 기본 자료구조(List, Dict)와 제어문(Loop)이 낯선 데이터 사이언티스트.  
> **Goal:** 단순히 문법만 익히는 것이 아니라, 파이썬 인터프리터 내부의 메모리 관리(Memory Management)와 자료구조의 구현 원리(Low-level Mechanics)를 이해하여 '이유 있는' 최적화 코드를 작성한다.

---

## 📚 Curriculum (총 5강 - Theory & Practice)

R의 벡터 연산이 빠른 이유(C-level Loop)와 파이썬 리스트가 무거운 이유(Object Overhead)를 비교하며 진행합니다.

### 1️⃣ `01_BigO_Loop.py` 🐢🐇
- **주제:** **[Chapter 4] Big-O & Iterator Overhead**
- **실습 단계:**
    - **Step 1 (Basic):** 단순 `for` 루프와 인덱싱(`a[i]`) 성능 측정.
    - **Step 2 (Evolution):** 이중 루프($O(N^2)$)가 될 때 기하급수적으로 느려지는 현상 확인.
- **🧠 Low-Level Theory:**
    - **Interpreter Overhead:** 파이썬 `for`문이 R의 `Vectorization`보다 느린 이유 (Type Checking, Reference Counting).
    - **CPU Cache:** 연속된 메모리(Array)와 흩어진 메모리(Linked List)의 캐시 히트율 차이.

### 2️⃣ `02_List_Evolution.py` 🧬
- **주제:** **[Chapter 5] Dynamic Array (List) & Memory Allocation**
- **실습 단계:**
    - **Step 1 (Basic):** `append()`, `insert()`, `pop()`, `remove()` 등 리스트 조작의 정석 익히기.
    - **Step 2 (Evolution):** 위 코드를 `List Comprehension`으로 한 줄로 줄이는 과정 (Pythonic).
- **🧠 Low-Level Theory:**
    - **Dynamic Array:** 파이썬 리스트는 연결 리스트가 아니다. **포인터 배열(Array of Pointers)**이다.
    - **Amortized O(1):** `append()`가 꽉 차면 메모리를 어떻게 2배로 늘리는가? (Doubling Strategy).
    - **Bytecode:** 리스트 컴프리헨션이 일반 `for`문보다 빠른 이유 (Stack 처리 방식).

### 3️⃣ `03_Dict_Set_Essential.py` 🔑
- **주제:** **[Chapter 5] Hash Table Implementation**
- **실습 단계:**
    - **Step 1 (Basic):** 딕셔너리 생성(`{}`), 추가(`d[k]=v`), 삭제(`del`), 조회(`get`).
    - **Step 2 (Evolution):** `KeyError` 방지용 `defaultdict`, 빈도수 계산용 `Counter`.
- **🧠 Low-Level Theory:**
    - **Hash Function:** 키(Key)를 주소(Address)로 바꾸는 수학적 원리.
    - **Collision Resolution:** 충돌이 났을 때 파이썬은 어떻게 해결하는가? (Open Addressing vs Chaining).
    - **Load Factor:** 딕셔너리가 꽉 차기 전에 미리 크기를 키우는 임계값.

### 4️⃣ `04_Loop_Upgrade.py` 🔄
- **주제:** **[Chapter 5] Generator & Lazy Evaluation**
- **실습 단계:**
    - **Step 1 (Basic):** `range(len(list))`를 이용한 C언어 스타일 루프.
    - **Step 2 (Evolution):** `enumerate()`(인덱스+값)와 `zip()`(병렬 처리)을 쓴 파이썬 스타일.
- **🧠 Low-Level Theory:**
    - **Iterator Protocol:** `__iter__`와 `__next__` 매직 메소드의 작동 원리.
    - **Memory Efficiency:** 제너레이터가 100억 개의 데이터를 처리해도 메모리가 터지지 않는 이유 (State 유지).

### 5️⃣ `05_String_Prep.py` ✂️
- **주제:** **[Chapter 6] Immutable Object & String Interning**
- **실습 단계:**
    - **Step 1 (Basic):** `split()`, `join()`, `upper()`, `replace()` 등 필수 함수 4대장.
    - **Step 2 (Evolution):** `s[::-1]` (슬라이싱)과 `re.sub()` (정규식)을 활용한 고급 전처리.
- **🧠 Low-Level Theory:**
    - **Immutability:** 파이썬 문자열은 왜 수정 불가능(Immutable)한가?
    - **String Interning:** 똑같은 문자열 "Hello"를 두 개 만들면 메모리 주소가 같은가 다른가?
    - **Garbage Collection:** 문자열 합치기(`+`)가 메모리 파편화를 일으키는 이유와 `join()`의 효율성.

---

## ⚡ How to Run
* **Extension:** VS Code 'Jupyter' Extension 필수.
* **Kernel:** `algo-base` (conda env)
* **Mode:** 코드를 드래그하거나 셀(`#%%`) 단위로 **`Shift + Enter`**를 눌러 Interactive Window에서 실행하세요.