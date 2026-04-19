**진도 체크:**
드디어 **[STEP 2 (자료구조 1 - 속도)]**의 마지막 보스전이야. 해시, 스택, 큐를 거쳐서 오늘 배울 건 바로 **'원형 큐(Circular Queue)'**야.
데이터 엔지니어링이나 통계 쪽에서 실시간 스트리밍 데이터(센서 로그, 주식 틱 데이터 등) 받을 때 메모리 터지지 말라고 쓰는 **'링 버퍼(Ring Buffer)'**랑 완벽하게 똑같은 개념이야. 오늘 이거 부수고 STEP 2 깔끔하게 졸업하자고!

---

# 1단계: 환경 세팅 지시 (Setup First)

본가 컴퓨터 터미널 열고 세팅부터 가자!

* **📂 찐최종 네이밍 룰:** `15_260313_design_circular_queue_L622`
* **📄 파일 구성:** `solution.py` (오늘의 링 버퍼 구현), `note.md` (고정 메모리와 모듈로(%) 연산의 마법 메모)

---

# 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 15: 원형 큐 디자인 (Design Circular Queue)

### 🔗 **링크:** [https://leetcode.com/problems/design-circular-queue/](https://leetcode.com/problems/design-circular-queue/)

## **📜 문제 설명 (Mission Briefing):**

기존의 직선 형태 큐는 데이터를 빼내고 나면 앞쪽에 빈 공간이 생기는데, 배열로 큐를 구현하면 이 앞쪽 빈 공간을 재활용할 수가 없어. (어제 말했듯 당겨오려면 $O(N)$이 걸리니까!)
그래서 큐의 맨 끝과 맨 앞을 동그랗게 연결해버린 **'원형 큐'**를 배열(List)만을 이용해서 직접 설계하는 게 목표야.

* `MyCircularQueue(k)`: 큐의 최대 크기 `k`를 받아서 초기화.
* `enQueue(value)`: 큐의 맨 뒤에 데이터 삽입. (성공 시 True, 꽉 찼으면 False)
* `deQueue()`: 큐의 맨 앞 데이터 삭제. (성공 시 True, 비었으면 False)
* `Front()`: 맨 앞 데이터 반환. (비었으면 -1)
* `Rear()`: 맨 뒤 데이터 반환. (비었으면 -1)
* `isEmpty()`, `isFull()`: 큐가 비었는지, 꽉 찼는지 확인.

## **🎯 오늘 부술 for문 (Big-O 관점):**

파이썬에는 `collections.deque`가 있지만, 면접관이 **"가변 길이 리스트 말고, 딱 고정된 메모리(크기 $k$) 안에서 $O(1)$ 속도로 큐를 구현해 봐"**라고 압박 질문을 할 때 쓰는 무기야.

* **공간 복잡도 $O(k)$ 엄수:** 파이썬의 `append()`나 `pop()` 같은 가변 배열 메서드를 절대 쓰면 안 돼. 처음부터 길이 $k$짜리 빈 리스트를 만들어두고 시작해야 해.
* **시간 복잡도 $O(1)$ 방어:** 데이터가 꽉 차서 끝에 도달하면, 포인터가 다시 배열의 인덱스 0으로 돌아가서 빈 공간을 채워야 해. 이때 for문이나 조건문 떡칠 없이 단 한 번의 수식으로 인덱스를 회전시키는 방법이 바로 **'나머지 연산자(Modulo, `%`)'**야.

## **🛠️ 네가 해야 할 것:**

1. `__init__`에서 크기가 `k`인 고정 배열(`[None] * k`)을 하나 만들어.
2. 현재 맨 앞 데이터를 가리킬 투 포인터(`front_idx`, `rear_idx`)나, 큐에 들어있는 현재 데이터 개수(`size`), 최대 크기(`k`)를 내부 변수(`self.`)로 세팅해.
3. 데이터가 들어오거나(`enQueue`) 나갈 때(`deQueue`), 인덱스를 1씩 증가시키는데 **배열 끝에 다다르면 0으로 뺑뺑이 돌게 만들어야 해.** 👉 핵심 로직: `next_index = (current_index + 1) % k`
4. 배열의 상태를 직접 수정하면서 (예: `self.q[self.rear_idx] = value`), 각 메서드의 조건에 맞게 True/False나 값을 반환하게끔 짜봐.

## **🧰 필요한 파이썬 내장 함수/문법 (범용 사용법):**

```python
# 1. 고정된 크기의 배열 초기화 (R에서 rep(NA, k) 하는 것과 비슷함)
k = 5
fixed_array = [None] * k  # [None, None, None, None, None]

# 2. 모듈로(Modulo) 연산자를 활용한 순환 (뺑뺑이)
idx = 4
next_idx = (idx + 1) % 5  # 5 % 5 = 0 (배열의 맨 끝에서 다시 0번 인덱스로 돌아감!)

```

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

이번에도 클래스 구현이야. 파이썬의 편리한 `append`에 기대지 말고, 인덱스를 직접 수학적으로 계산해서 넣고 빼는 '로우 레벨(Low-level)' 감성을 느껴봐. 스켈레톤 복붙하고 시작!

```python
class MyCircularQueue:
    def __init__(self, k: int):
        # 최대 크기 k와 고정 배열을 초기화해.
        self.k = k
        self.q = [None] * k
        # 투 포인터(인덱스)와 현재 크기(size)를 추적할 변수들을 만들어봐.
        self.front = 0
        self.rear = 0 # (혹은 -1로 시작해도 됨, 본인 논리에 맞게 세팅)
        self.size = 0

    def enQueue(self, value: int) -> bool:
        # 꽉 찼으면 False 반환
        # 아니면 rear 위치에 값을 넣고, rear 인덱스를 1칸 전진(모듈로 연산!)
        pass

    def deQueue(self) -> bool:
        # 비었으면 False 반환
        # 아니면 front 위치의 값을 빼고(None 처리 등), front 인덱스를 1칸 전진(모듈로 연산!)
        pass

    def Front(self) -> int:
        # 비었으면 -1 반환, 아니면 front 위치의 값 반환
        pass

    def Rear(self) -> int:
        # 비었으면 -1 반환, 아니면 가장 최근에 삽입된 위치의 값 반환
        pass

    def isEmpty(self) -> bool:
        # 현재 사이즈가 0인지 체크
        pass

    def isFull(self) -> bool:
        # 현재 사이즈가 k인지 체크
        pass


if __name__ == "__main__":
    print("=== 원형 큐 테스트 시작 ===")
    cq = MyCircularQueue(3)  # 크기가 3인 원형 큐 생성
    
    print("enQueue 1:", cq.enQueue(1))  # Expected: True
    print("enQueue 2:", cq.enQueue(2))  # Expected: True
    print("enQueue 3:", cq.enQueue(3))  # Expected: True
    print("enQueue 4 (Full):", cq.enQueue(4))  # Expected: False (꽉 참)
    
    print("Rear element:", cq.Rear())  # Expected: 3
    print("isFull?:", cq.isFull())     # Expected: True
    
    print("deQueue:", cq.deQueue())    # Expected: True (1번 요소 빠짐, 공간 생김!)
    print("enQueue 4:", cq.enQueue(4))  # Expected: True (남은 공간에 4가 들어감)
    
    print("Rear element:", cq.Rear())  # Expected: 4

```

자, 불금의 마지막을 불태워보자! `%` 연산자를 써서 인덱스가 배열 크기를 넘어가지 않게 가둬버리는 게 핵심이야. 다 짜면 코드 올려주고, 막히면 바로 물어봐. 가즈아! 🔥











<br>
<br>
<br>
<br>
<br>
<br>
<br>









주말 아침부터 코테 켜는 폼 미쳤다! 어제 불금에 본가 와서 기절하고 아침에 일어나자마자 푼 거지? ㅋㅋㅋ (지금 토요일 오전 11시 다 돼가네!)

일단 네가 짠 코드는 테스트 케이스를 통과하는 **'기능적으로는 정상 작동하는 코드'**야. 이중 for문 안 쓰고 `rear`랑 `front` 포인터를 `% k`로 잘 굴렸어.

**근데 PT 쌤으로서 팩트 폭격 하나 세게 간다.**
어제 내가 *"절대 빈칸(`None`)을 찾으러 다니면 안 돼"* 라고 했던 거 기억나?
네 코드에는 통계/데이터 분석가의 영원한 습관, 즉 "데이터(결측치)를 직접 뒤져서 상태를 확인하려는 본능"이 아주 진하게 남아있어. 결과적으로 이 코드는 시간 복잡도 방어에 실패했어.

네가 주석으로 남긴 핵심 질문들부터 싹 다 대답해 주고, 왜 네 코드가 비효율적인지($O(N)$), 그리고 그걸 어떻게 $O(1)$로 찢어버릴 수 있는지 리팩토링해 줄게!

---

### ❓ 질문 1: `enQueue`, `deQueue`는 굳이 왜 `bool`로 리턴하는가? (이득이 뭔데?)

이건 진짜 실무(데이터 엔지니어링/백엔드) 관점에서 엄청 중요한 질문이야.
통계 모델링할 때는 데이터가 무조건 다 들어간다고 가정하지만, 실시간 스트리밍 환경(카프카, 로그 수집기 등)에서는 버퍼(큐)가 **꽉 차서 데이터를 뱉어내는 상황**이 비일비재해.

* **`enQueue`가 bool인 이유:** 프로듀서(데이터 넣는 놈)한테 **"야, 버퍼 꽉 차서 네 데이터 드랍(Drop)됐어(False)"** 혹은 **"잘 들어왔다(True)"**라고 피드백(ACK/NACK)을 줘야 해. 그래야 프로듀서가 "아, 꽉 찼네? 1초 뒤에 다시 보내야지(재시도)" 같은 에러 핸들링을 할 수 있거든.
* **`deQueue`가 bool인 이유:** 컨슈머(데이터 빼는 놈)한테 **"야, 지금 파이프 비어있으니까 허공에 삽질하지 마(False)"**라고 알려주는 거야.

---

### 🚨 팩트 체크: 왜 네 코드가 $O(N)$의 함정에 빠졌는가?

네가 짠 코드에서 제일 치명적인(비효율적인) 부분들이 바로 여기야.

1. **`if None not in self.q:` (isFull 체크 시)**
* 이건 파이썬 내부적으로 리스트의 처음부터 끝까지 `for`문을 돌면서 `None`이 있는지 일일이 확인하는 **$O(k)$**짜리 연산이야. 크기가 10만이면 10만 번을 뒤져야 해!


2. **`if self.q == [None] * self.k:` (isEmpty 체크 시)**
* 이건 더 최악이야. `[None] * k`라는 새로운 리스트를 메모리에 또 만들고, 기존 리스트랑 원소를 하나하나 다 비교해. 시간도 $O(k)$고, 메모리도 추가로 갉아먹지.



**💡 해결책: `self.size` (카운터)를 써라!**
네가 `__init__`에 `self.size = 0`이라고 예쁘게 만들어 놓고, 정작 함수들 안에서는 한 번도 안 썼어! ㅋㅋㅋ
술집에 사람이 꽉 찼는지 확인하려면, 테이블(배열) 돌아다니면서 빈자리가 있는지 다 찾아보는 게 빠를까? 아니면 **입구에 있는 알바생이 들고 있는 '현재 인원수 카운터(`size`)' 숫자 하나 딱 보는 게 빠를까?** 당연히 후자지! 카운터 숫자 하나만 확인하면 되니까 완벽한 **$O(1)$**이 돼.

---

### 🛠️ Pythonic & $O(1)$ 리팩토링 (이렇게 고쳐봐!)

네가 짠 로직을 `self.size`를 활용해서 완벽한 $O(1)$ 코드로 바꿔볼게. 잘 비교해 봐!

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.q = [None] * k
        self.front = 0
        self.rear = -1 
        self.size = 0  # ✨ 이 녀석이 핵심 치트키야!

    # 1. 상태 체크는 무조건 size로! (O(1))
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.k

    def enQueue(self, value: int) -> bool:
        if self.isFull():  # None을 찾을 필요 없이 알바생한테 꽉 찼냐고만 물어봄
            return False
        
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.size += 1     # ✨ 사람 들어왔으니 카운터 1 증가!
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # 💡 굳이 self.q[self.front] = None 으로 지울 필요조차 없어! 
        # 어차피 나중에 rear가 한 바퀴 돌아서 알아서 덮어쓸 거니까.
        self.front = (self.front + 1) % self.k
        self.size -= 1     # ✨ 사람 나갔으니 카운터 1 감소!
        return True
        
    def Front(self) -> int:
        if self.isEmpty(): # 비효율적으로 None인지 확인할 필요 없음
            return -1
        return self.q[self.front]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

```

### 🧠 깨달음 포인트

어때? `None`을 찾거나 쓸 필요가 아예 사라졌지?
포인터(`front`, `rear`)는 그저 **"어디서 쓰고 어디서 빼야 하는지" 위치만** 가리키고,
상태 관리(`isEmpty`, `isFull`)는 오직 **`size` 변수 하나만** 더하고 빼면서 $O(1)$로 완벽하게 통제하는 거야. 이게 바로 컴퓨터 공학에서 말하는 '메모리 관리의 덮어쓰기(Overwrite) 미학'이야.

자, 이렇게 해서 **[STEP 2: Hash, Stack, Queue]** 대단원을 깔끔하게 졸업했다!! 🎉
주말 아침부터 코딩하느라 뇌에 쥐 났을 텐데 진짜 수고 많았어.
오늘 코드 리팩토링된 거 네 언어로 `note.md`에 "데이터를 지울 필요 없이 포인터와 size만 갱신한다"라고 정리해 두고 푹 쉬어!

월요일에는 이제 2차원 공간과 트리(Tree)를 넘나드는 **[STEP 3 (자료구조 2 - 공간 데이터)]**의 첫 번째 보스, '그래프 탐색(DFS/BFS)'으로 찾아올게. 주말 꿀잼으로 보내라!! 🚀