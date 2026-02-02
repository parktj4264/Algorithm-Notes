# 01_BigO_Loop — Big-O & Interpreter Overhead

## 0) Overview
- **Big-O Notation** ($O(\cdot)$): 입력 크기 $N$이 무한대로 발산($N \to \infty$)할 때, 연산 비용 함수 $f(N)$의 점근적 상한(Asymptotic Upper Bound)을 나타내는 척도.
    - 즉, 데이터가 늘어날 때 연산량이 폭발하는 증가율(Rate of Growth)의 체급을 분류한 것.
    - $O(g(n)) = \left\{ f(n) \mid \exists C > 0, \exists n_0 \in \mathbb{R} \text{ s.t. } \forall n \ge n_0, \; 0 \le f(n) \le C \cdot g(n) \right\}$
    - Big-O는 측정 단위(Unit/Notation) → 시간 복잡도랑 공간 복잡도 측정 가능
- 파이썬 루프가 느린 핵심 이유는 “한 번 도는 비용”이 비싸서다.
  - 매 반복마다: 바이트코드 실행 + 객체 접근 + 타입/참조카운트 처리 등등
- R의 벡터 연산이 빠른 핵심 이유는 “루프가 C에서 돈다”에 가깝다.
  - 한 번에 덩어리로 처리 (tight loop + contiguous memory)


## 1) Big-O 감각: O(1), O(N), O(N^2)
- O(1): 입력 크기 N과 무관하게 거의 일정
    - 데이터($N$)가 아무리 늘어나도, CPU가 처리해야 할 명령어의 수가 고정됨.
    - $Cost(N) = C$ (상수 함수). $\frac{d(Cost)}{dN} = 0$.
- O(N): N이 2배면 시간도 대충 2배
    - 데이터 하나당 처리 비용($C$)이 존재하고, 전체 비용은 $N$에 비례하여 누적됨.
    - $Cost(N) \approx C \cdot N$.
    - R (Vector): $C$가 매우 작음 (C언어 레벨의 타이트한 루프) / Python (List): $C$가 매우 큼 (객체 언박싱 + 타입 체크 + 레퍼런스 카운팅) → 파이썬에선 $C$를 줄이기 위해 Loop 대신 List Comprehension이나 Built-in을 써야 함
- O(N^2): N이 2배면 시간은 대충 4배
    - $Cost(N) \approx N \times N$


## 2) 파이썬 연산 속도가 느린 이유

Python 반복문(Loop)이 느린 이유를 설계 철학과 메모리 관리 관점에서

### 1. Object Representation: Boxing & Memory Overhead

Python 데이터는 순수 값(Raw Value)이 아닌, 메타데이터가 포함된 **구조체(Structure)** 형태 → **박싱(Boxing)**

* **C/R (Primitive Type):**
    * 정수 `1`은 메모리에 4~8바이트 이진수(`000...01`)로 저장됨.
    * 메타데이터가 없어 메모리 효율 좋음.

* **Python (PyObject Wrapper):**
    * 모든 변수는 `PyObject`라는 거대한 C 구조체
    * 정수 `1` 하나 저장하려고 다음 헤더 정보들이 붙음.
        * `ob_refcnt`: 참조 계수 (Reference Count)
        * `ob_type`: 타입 정보 (Type Pointer)
        * `ob_digit`: 실제 값 (Payload)

* **결과:** 정수 하나에 약 28바이트 소요 → C/R 대비 **7배 이상 메모리 낭비(Overhead)** 발생



### 2. Type System: Dynamic Dispatch & Runtime Overhead

Python은 **동적 타이핑(Dynamic Typing)** 언어라, 연산 때마다 타입을 추론하고 검증 비용 발생

* **R (Vectorization) - Static-like:**
    * 벡터 전체 타입이 같다는 보장이 있음.
    * 타입 검사는 연산 시작 전 **딱 1회**만 하고, 내부 C 루프에선 검사 없이 고속 주행


* **Python (Loop) - Dynamic Dispatch:**
    * `for` 루프 돌 때마다 인터프리터가 아래를 반복
    1. 변수 `a`, `b` 타입 확인 (Type Checking)
    2. 타입에 맞는 더하기 함수(`__add__`) 찾기 (Method Dispatch)
    3. 연산 후 참조 카운트 갱신


**결과:** 100만 번 루프 돌면 **100만 번 검사** → 실제 연산보다 준비 과정 비용이 더 큼.



### 3. Memory Access: Indirection & Cache Inefficiency

데이터 메모리 배치 방식 차이가 **CPU 캐시 적중률(Cache Hit Rate)**을 가름.

* **R (Contiguous Memory):**
    * 벡터 데이터가 물리적 메모리에 아파트 옆집처럼 연속으로 붙어있음.
    * **참조 지역성(Locality):** 하나 읽을 때 옆에 것도 같이 딸려와서 캐시 적중률(Cache Hit) 높음

* **Python (Array of Pointers):**
    * 리스트(`List`)는 실제 값이 아니라 주소(Pointer)들의 배열
    * 실제 객체는 힙(Heap) 메모리 여기저기 흩어져 있음 (Fragmentation).
* **결과:** 리스트 돌 때 주소 따라가느라(Pointer Chasing) CPU가 계속 딴 데 쳐다봄.  → 캐시 미스(Cache Miss) 발생.


### 따라서

1. **Boxing:** 데이터가 메타데이터 포함된 무거운 객체(`PyObject`)라 메모리 비효율적
2. **Overhead:** 루프 매회 발생하는 타입 검증 & 동적 바인딩 비용이 연산 비용보다 더 큼.
3. **Locality:** 메모리가 흩어져 있어 CPU 캐시 도움(Spatial Locality)을 못 받음.





## 3) CPU Cache 감각 (CPU Cache & Memory Access Patterns)

### 1. The 64-Byte Rule: 도매상의 원칙

CPU는 데이터를 RAM에서 가져올 때, 절대 "한 숟가락(1 Byte/1 Word)"만 퍼오지 않음. 한 번 트럭을 보내면 **무조건 한 박스(Cache Line)**를 꽉 채워서 가져옴.

* **Cache Line:** 보통 **64 Bytes**.
* **원리:** 니가 `Address 100`번지의 데이터를 요청하면, CPU는 `100 ~ 163`번지 데이터를 통째로 긁어서 L1 캐시에 저장함.
* **이유:** "얘가 100번지 썼으면, 곧 101번지도 쓰겠지?"라는 **공간 지역성(Spatial Locality)** 대전제 때문임.

### 2. R/Numpy (Array): 캐시 히트(Cache Hit)의 축복

R의 벡터나 Numpy 어레이는 C의 배열(Contiguous Memory)임.

* **구조:** `[Int(4B) | Int(4B) | Int(4B) | ... ]`
* **시나리오:**
1. CPU가 `vec[0]`을 읽음.
2. 메모리 컨트롤러가 `vec[0]`부터 `vec[15]`까지(64B / 4B = 16개) 한방에 캐시로 가져옴.
3. CPU가 `vec[1]`을 읽으려 함. -> **"어? 이미 캐시에 있네?" (L1 Cache Hit)**
4. RAM까지 안 가고 바로 연산. (나노세컨드 단위의 초고속 처리)


* **결과:** 고속도로 질주.

### 3. Python (List): 포인터 체이싱(Pointer Chasing)의 지옥

파이썬 리스트는 "값"이 아니라 **"주소(Pointer)"들의 모임**임.

* **구조:** `[Ptr A | Ptr B | Ptr C | ... ]` (리스트 자체는 연속적일 수 있음)
* **문제:** 하지만 `Ptr A`가 가리키는 **실제 데이터(PyObject A)**는 저 멀리 힙(Heap) 메모리 구석에 처박혀 있음.
* **시나리오:**
1. CPU가 `list[0]`의 주소(Ptr A)를 읽음. (여기까진 괜찮음)
2. 그 주소를 따라 **실제 값**을 가지러 감 -> **램의 엉뚱한 주소(Random Address)로 점프.**
3. 그거 처리하고 `list[1]`을 봄. `Ptr B`를 얻음.
4. `Ptr B`를 따라 실제 값을 가지러 감 -> **또 다른 램의 엉뚱한 주소로 점프.**


* **결과:** 매번 RAM의 새로운 위치를 건드림. 캐시에 받아둔 건 쓸모가 없음. **Cache Miss**의 연속. (이걸 **Pointer Chasing**이라 함)

### 따라서

1. **Cache Line:** CPU는 64바이트 단위로 데이터를 긁어옴 (도매상).
2. **R/C:** 데이터가 붙어 있어서(Contiguous) "하나 사면 15개 덤"으로 딸려옴 **(Spatial Locality 극대화)**.
3. **Python:** 데이터가 흩어져 있어서(Scattered) 덤으로 가져온 데이터가 쓸모없음. 매번 RAM 문을 다시 두드려야 함 **(Latency 폭발)**.

이 원리를 이해하면, **"왜 대용량 데이터 처리는 파이썬 `List` 대신 `Numpy`나 `Pandas`를 써야 하는가?"**에 대한 답이 하드웨어 레벨에서 증명됨. `Numpy`는 파이썬 안에서 **C의 연속 메모리 구조**를 강제로 구현한 라이브러리기 때문


---
---


## 4) 벤치마크 할 때 지켜야 할 룰
- `time.time()` 말고 `time.perf_counter()` 사용
- 한 번만 재지 말고 반복해서 통계(평균/최소)를 본다
- 너무 작은 N은 노이즈가 크다 (OS 스케줄링, 캐시, 터보부스트 등)
- 가능하면 `timeit`도 같이 써라 (파이썬 표준 벤치 도구)


## 5) 실습 시나리오
### Step 1: O(N) — 단순 합
- (A) for + 인덱싱 `a[i]`
- (B) for + direct iteration `for x in a`
- (C) sum(a)  (내장함수: C쪽 루틴이라 대체로 빠름)

**관찰 포인트**
- (B)가 보통 (A)보다 빠른 경우가 많다 (인덱싱 오버헤드 감소)
- (C)는 급이 다르게 빠를 수 있다 (C에서 루프)

### Step 2: O(N^2) — 이중루프
- 모든 쌍의 합/곱 같은 걸 만들면 N^2이 된다
- N=5,000만 돼도 25,000,000 연산이다. (이제부터 숨이 가빠짐)

**관찰 포인트**
- N을 2배로 올렸을 때 시간이 4배로 뛰는지 확인
- “파이썬 루프 비용 × N^2”가 되면서 체감이 급격히 나빠진다


## 6) 오늘의 과제(짧고 강력)
1) O(N)에서 (A)(B)(C) 순위 확인
2) O(N^2)에서 N을 500, 1000, 2000으로 올리며 시간 증가 비율 확인
3) 결론 한 줄로 적기:
   - “파이썬은 루프를 어떻게 쓰는 게 좋다/나쁘다”
