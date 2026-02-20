앞에서는 속도(Time)를 쥐어짜는 법을 배웠다면, 이번 챕터는 **"메모리(Space)의 마술"**이야.

현업에서 수백 GB짜리 설비 로그(MSR 데이터) 분석할 때, R처럼 메모리에 한 번에 다 올려버리면 바로 **OOM(Out Of Memory)** 뜨고 서버 터지는 거 알지? 파이썬은 이 문제를 **"게으름(Lazy Evaluation)"**으로 해결해.

파이썬 루프를 가장 파이썬답게, 그리고 메모리 효율을 극한으로 끌어올리는 원리를 담은 마크다운 파일이야.

---

# 🔄 04_Loop_Upgrade — Generator & Lazy Evaluation

## 0. Overview

* **Target:** "C언어나 R에서 하던 버릇대로 `for i in range(len(data)):`를 쓰는 사람."
* **Goal:** 파이썬 루프의 근간인 **Iterator Protocol**을 이해하고, 수백억 개의 데이터를 처리해도 메모리가 터지지 않는 **제너레이터(Generator)**와 **지연 평가(Lazy Evaluation)**의 마법을 체화한다.
* **Key Concept:** `__iter__`, `__next__`, `yield`, `enumerate`, `zip`, `Lazy Evaluation`.

---

## 1. Low-Level Theory: 이터레이터와 지연 평가 🧠

### 1-1. Iterator Protocol: "다음에 줄게"

파이썬의 `for`문은 사실 내부적으로 객체한테 계속 "다음 거 내놔"라고 조르는 구조야. 이 약속(Protocol)을 지키는 객체만 루프를 돌릴 수 있어.

* **`__iter__()`:** "나 반복 가능한 놈(Iterable)이야" 하고 선언하는 매직 메서드. 이걸 호출하면 **이터레이터(Iterator)** 객체가 튀어나옴.
* **`__next__()`:** "자, 여기 다음 데이터" 하고 하나씩 던져주는 메서드. 더 이상 줄 게 없으면 `StopIteration` 에러를 던져서 루프를 종료시킴.
* **비유:** **페즈(PEZ) 캔디 디스펜서**를 생각하면 돼. 사탕(데이터)이 안에 들어있고, 대가리를 젖힐 때(`__next__()` 호출)마다 하나씩만 톡 튀어나옴.

### 1-2. Lazy Evaluation (지연 평가): "필요할 때만 일한다"

형, 1부터 100억까지의 숫자가 필요하다고 쳐보자.

* **Eager Evaluation (기존 방식):** 100억 개의 숫자를 메모리에 **다 만들어 놓고** 시작함. (메모리 수십 GB 폭파 💥)
* **Lazy Evaluation (지연 평가):** 지금 당장 1이 필요해? 그럼 1만 만들어줄게. 다음 루프에서 2가 필요해? 그때 2를 계산해서 줄게. (메모리 점유율 **수십 바이트** 유지 🛡️)

이 "게으르지만 똑똑한" 계산 방식을 파이썬에서는 **제너레이터(Generator)**가 수행해.

### 1-3. State 유지와 `yield`의 마법

일반 함수(`return`)는 값을 반환하면 자기 할 일 다 했다고 로컬 변수 다 날리고 죽어버리잖아?
근데 제너레이터 함수는 **`yield`**를 만나면 값을 던져주고 **"일시 정지(Pause)"** 상태로 들어가.

* 자기가 어디까지 읽었는지, 현재 변수 상태는 어떤지(State)를 메모리 한편에 고이 간직함.
* 다음 `__next__()`가 호출되면, 정지했던 그 줄부터 다시 코드가 실행됨.

---

## 2. Practical Guide: 파이썬 스타일 루프 (Step-by-Step)

### Step 1: C-Style Loop (하수) vs Pythonic Loop (고수)

인덱스(i)와 값(value)이 동시에 필요할 때, C언어 짬바가 나오는 코드와 파이썬 고수의 코드는 달라.

* **Legacy (C-Style):**
```python
a = ['apple', 'banana', 'cherry']
for i in range(len(a)):       # 👈 길이를 구해서 인덱스로 접근 (Non-Pythonic)
    print(i, a[i])            # 👈 a[i]를 또 찾아가야 함
```


* **Modern (`enumerate`):**
```python
for i, val in enumerate(a):   # 👈 알아서 인덱스랑 값을 튜플로 던져줌 (개꿀)
    print(i, val)
```



### Step 2: 두 배열을 동시에 돌기 (`zip`)

웨이퍼 ID 리스트랑 해당 웨이퍼의 수율 리스트를 짝지어서 보고 싶을 때.

* **Legacy (Index 접근):**
```python
for i in range(len(wafers)):
    print(wafers[i], yields[i])
```


* **Modern (`zip`):**
```python
for w, y in zip(wafers, yields):  # 👈 두 리스트의 요소를 옷 지퍼 올리듯 맞물려줌
    print(w, y)
```


* *주의:* `zip`도 내부적으로는 **Lazy Evaluation**을 함. 즉, 한 번에 다 묶어두는 게 아니라 루프가 돌 때마다 하나씩 꺼내서 묶어줌 (메모리 절약).



---

## 3. Deep Dive: Generator Expression (제너레이터 표현식) 🚀

어제 배운 `List Comprehension`(`[ ]`)의 유일한 단점은 "결과를 통째로 메모리에 올린다"는 거야. 데이터가 1억 개면 메모리 터짐.
이걸 소괄호 `( )`로만 바꾸면 **Generator Expression**이 되면서 메모리를 아예 안 먹어.

```python
# 1. List Comprehension (Eager) - 메모리 엄청 먹음
squares_list = [x*x for x in range(10_000_000)]  # 👈 실행 순간 1000만 개 연산 다 함

# 2. Generator Expression (Lazy) - 메모리 거의 안 먹음
squares_gen = (x*x for x in range(10_000_000))   # 👈 "나중에 달라고 할 때 계산할게" (설계도만 만듦)

# 필요할 때 뽑아 쓰기
print(next(squares_gen)) # 0
print(next(squares_gen)) # 1

```

---

## 4. Summary for R User 📝

1. **R은 주로 통째로 연산(Vectorization)한다.** 수십 GB짜리 데이터를 다루려면 RAM이 엄청 빵빵해야 함.
2. **파이썬은 흐르는 강물(Stream)처럼 처리할 수 있다.** 제너레이터(`yield`)를 쓰면 100TB짜리 로그 파일도 줄 단위로 읽어와서 메모리 OOM 없이 끝까지 분석할 수 있다.
3. 앞으로 파이썬에서 `range(len(x))`를 치고 있는 자신을 발견하면, 스스로 손등을 때리고 **`enumerate()`**나 **`zip()`**으로 고쳐 써라.

