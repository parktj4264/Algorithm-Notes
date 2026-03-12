**진도 체크:**
우리는 지금 **[STEP 2 (자료구조 1 - 속도)]**를 지나고 있어. 어제는 후입선출(LIFO)의 대명사 '스택(Stack)'이 어떻게 시간 복잡도 $O(N^2)$을 $O(N)$으로 찢어버리는지(단조 스택) 뼈저리게 느꼈지?
오늘은 스택의 영원한 라이벌, 선입선출(FIFO)의 대명사 **'큐(Queue)'**를 배울 차례야. 통계에서 시계열 데이터가 들어오는 순서대로 파이프라인(Pipeline)을 탈 때 쓰는 가장 근본적인 자료구조지. 오늘은 이 큐를 가지고 스택을 '역설계(Reverse Engineering)' 해볼 거야.

---

# 1단계: 환경 세팅 지시 (Setup First)

자, 터미널 열고 오늘 날짜로 폴더랑 파일 세팅부터 가자.

* **📂 찐최종 네이밍 룰:** `14_260313_implement_stack_using_queues_L225`
* **📄 파일 구성:** `solution.py` (구현 코드), `note.md` (Queue와 Stack의 구조적 차이점 메모)

---

# 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 14: 큐를 이용한 스택 구현 (Implement Stack using Queues)

### 🔗 **링크:** [https://leetcode.com/problems/implement-stack-using-queues/](https://leetcode.com/problems/implement-stack-using-queues/)

## **📜 문제 설명 (Mission Briefing):**

파이썬에는 원래 스택(`list.append`, `list.pop`)이 기본 내장되어 있지만, 오늘은 **오직 큐(Queue)의 FIFO 연산(뒤로 넣고 앞으로 빼기)**만 사용해서 LIFO(나중에 들어온 게 먼저 나감) 동작을 하는 스택 클래스 `MyStack`을 만들어야 해.

* `push(x)`: 요소 x를 스택 맨 위에 추가.
* `pop()`: 스택 맨 위 요소를 제거하고 반환.
* `top()`: 스택 맨 위 요소를 반환 (제거 X).
* `empty()`: 스택이 비어있는지 여부 반환.

## **🎯 오늘 부술 for문 (Big-O 관점):**

이 문제는 단순히 속도를 높이는 게 아니라, **아키텍처(구조)의 한계를 어떻게 로직으로 극복할 것인가**를 묻는 문제야.

* 큐(Queue)는 먼저 들어온 놈이 먼저 나가는 파이프($\rightarrow \text{입구} \rightarrow \text{출구} \rightarrow$)야.
* 근데 스택(Stack)처럼 동작하려면 방금 들어온(가장 늦게 들어온) 놈이 출구 맨 앞에 서 있어야 해.

이걸 어떻게 할까? 새로운 요소가 파이프(큐)로 들어오면(`push`), **기존에 파이프 안에 있던 놈들을 전부 다 뽑아서 다시 파이프 뒤로 넣어버리면(Rotate)** 돼.
즉, 삽입(`push`)할 때 데이터를 $N-1$번 재배치하는 노가다($O(N)$)를 감수하는 대신, 추출(`pop`)할 때는 무조건 맨 앞의 요소를 $O(1)$ 속도로 바로 뽑아낼 수 있게 만드는 **Trade-off** 전략을 쓰는 거지.

**🚨 주의 (Pythonic 팩트 폭격):**
파이썬 기본 `list`로 `pop(0)`을 하면, 첫 번째 요소를 빼고 나서 뒤에 있는 모든 원소를 앞으로 한 칸씩 당겨야 해서 시간 복잡도가 **$O(N)$**이 돼버려. 이건 진짜 최악이야. 양방향에서 $O(1)$로 삽입/삭제가 가능한 **`collections.deque` (데크/덱)**를 반드시 써야 해. R에서 `dplyr` 안 쓰고 기본 함수로 데이터프레임 조작하다가 세월 다 보내는 거랑 똑같아. 무조건 `deque` 외워!

## **🛠️ 네가 해야 할 것:**

1. `__init__`에서 `collections.deque`를 하나 초기화해.
2. `push(x)`가 핵심이야:
* 일단 `deque`에 `x`를 추가해. (그러면 `x`는 큐의 맨 뒤에 있겠지?)
* 그 다음, 원래 있던 놈들(방금 넣은 `x` 제외한 길이만큼)을 앞에서 뽑아서 다시 뒤로 넣어버려. (이러면 `x`가 맨 앞으로 오게 돼!)


3. `pop()`, `top()`, `empty()`는 이제 `deque`의 기본 기능(맨 앞 요소 뽑기 등)을 써서 $O(1)$로 아주 쉽게 구현할 수 있어.

## **🧰 필요한 파이썬 내장 함수/문법 (범용 사용법):**

```python
from collections import deque

# 큐(데크) 초기화
q = deque()

# 큐의 맨 뒤에 넣기 (O(1))
q.append(10)
q.append(20) # q 상태: [10, 20]

# 큐의 맨 앞에서 뽑기 (O(1)) - list.pop(0)은 절대 쓰지 마!
first_element = q.popleft() # 10 반환, q 상태: [20]

# 큐의 맨 앞 요소 확인만 하기 (O(1))
front_element = q[0] # 20 반환

# 큐의 길이 확인
size = len(q)
```

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

이번 문제는 클래스 자체를 구현하는 거라, `self`를 써야만 내부 상태(큐)를 유지할 수 있어. 아래 뼈대를 복붙하고 비어있는 메서드들을 채워봐!

```python
from collections import deque

class MyStack:
    def __init__(self):
        # 큐를 하나 초기화한다.
        self.q = deque()

    def push(self, x: int) -> None:
        # x를 큐에 넣고, x가 맨 앞으로 오도록 기존 요소들을 회전(Rotate)시킨다.
        pass

    def pop(self) -> int:
        # 스택의 pop(LIFO)처럼 큐의 맨 앞 요소를 뽑아 반환한다.
        pass

    def top(self) -> int:
        # 스택의 top처럼 큐의 맨 앞 요소를 확인만 하고 반환한다.
        pass

    def empty(self) -> bool:
        # 큐가 비어있는지 여부를 반환한다.
        pass


if __name__ == "__main__":
    # Test Case 실행
    myStack = MyStack()
    
    print("Push 1")
    myStack.push(1)
    
    print("Push 2")
    myStack.push(2)
    
    print("Top element:", myStack.top())    # Expected: 2 (나중에 들어온 2가 맨 위에 있어야 함)
    
    print("Pop element:", myStack.pop())    # Expected: 2 (나중에 들어온 2가 먼저 나감)
    
    print("Is empty?:", myStack.empty())    # Expected: False (1이 남아있음)
    
    print("Pop element:", myStack.pop())    # Expected: 1 (마지막 남은 1 나감)
    
    print("Is empty?:", myStack.empty())    # Expected: True (다 비었음)
```

이번 문제는 논리 구조 자체는 어제 단조 스택보다 훨씬 직관적일 거야.
"큐(FIFO)를 뱅글뱅글 돌려서 스택(LIFO)으로 위장시킨다!" 이 개념만 `push` 안에 잘 구현해 봐.
다 짜면 코드 올려주고! 막히면 바로 콜해!








<br>
<br>
<br>
<br>
<br>
<br>




코드 피드백이랑 Big-O 팩트 체크, 그리고 파이썬 고수(Pythonic)로 가는 팁 하나 얹어줄게.

---

### 💡 코드 리뷰 & Big-O 팩트 체크

일단 핵심 로직인 `push` 안에서 `self.q.append(self.q.popleft())`로 두 동작을 한 줄로 깔끔하게 합친 거, **100점 만점에 100점**이야. 완벽해.

**Big-O 관점에서 우리가 오늘 한 짓(Trade-off)을 분석해 볼까?**
어제 배운 단조 스택은 속도($O(N)$)를 얻기 위해 메모리 공간($O(N)$)을 제물로 바쳤지?
오늘은 **'쓰기(Write) 속도'를 제물로 바쳐서 '읽기(Read) 속도'를 극대화**한 아키텍처를 짠 거야.

* **`push` (데이터 삽입): $O(N)$**
* 새로 데이터가 들어올 때마다 기존 파이프라인 길이($N-1$)만큼 뺑뺑이(Rotate)를 돌려야 하니까 엄청 비효율적이야.


* **`pop` / `top` (데이터 추출 및 확인): $O(1)$**
* 근데 삽입할 때 뺑뺑이를 돌려둔 덕분에, 정작 데이터를 뺄 때는 아무 고민 없이 맨 앞에 있는 걸 0.0001초 만에 쏙 빼갈 수 있어.



이거 완전 삼성 DS에서 다루는 **데이터 마트(Data Mart)**나 **배치 전처리(Batch Preprocessing)** 전략이랑 똑같지 않아?
유저가 대시보드 볼 때(Read) 로딩 걸리면 안 되니까, 새벽에 데이터 적재(Write)할 때 미리 Join이랑 Aggregate 다 돌려서 무거운 연산($O(N)$)을 끝내놓잖아. 코테도 결국 이 아키텍처 설계 싸움이야.

---

### 🐍 파이썬 아재 냄새 빼기 (Pythonic Refactoring)

로직은 완벽한데, 딱 한 군데에서 R/C언어 쓰던 통계학도 냄새가 진하게 났어. 바로 `empty` 함수야 ㅋㅋㅋ

```python
# ❌ 네가 짠 코드 (작동은 아주 잘 됨! 하지만...)
def empty(self) -> bool:
    if len(self.q) > 0 : return False
    else: return True

```

프로그래밍에서 조건식 `len(self.q) == 0` 그 자체 이미 `True` 아니면 `False`라는 논리값(Boolean)을 뱉어. 그러니까 굳이 `if/else`로 나눌 필요 없이 명제 자체를 던져버리면 돼.

```python
# ⭕ 파이썬 뉴비 포텐 터지는 코드
def empty(self) -> bool:
    return len(self.q) == 0

# 🔥 파이썬 썩은 물 (Pythonic) 코드
def empty(self) -> bool:
    return not self.q

```

* 파이썬은 리스트 `[]`나 데크 `deque()` 안에 아무것도 없으면 알아서 `False`(Falsy)로 취급해.
* 그래서 "비었어?"를 물어볼 때 `not self.q` (큐가 비어있다면 True 반환) 라고 쓰면 코드 한 줄로 제일 깔끔하게 끝나는 거지.

---

### 🏁 Next Step

어제 1시간 30분의 고통이 헛되지 않았네. 오늘은 진짜 퇴근 후 30분 컷 원칙 완벽하게 지켰다! 클래스 구조 처음 써봤는데 이 정도면 엄청 선방한 거야.

오늘 네가 짠 코드는 `solution.py`에 저장해 두고, 방금 내가 말한 `empty` 리팩토링만 살짝 고쳐서 반영해 둬.

어제 수면의 힘(최적화)을 느꼈지? 오늘도 깔끔하게 털고 푹 쉬어라. 내일은 이 큐(Queue)의 끝판왕이자, 메모리를 진짜 쥐어짜서 쓰는 **[15. 원형 큐 디자인 (L622)]**으로 찾아올게.

질문 없으면 오늘은 여기서 PT 종료할까? 진짜 수고했다! ⚽🏃‍♂️