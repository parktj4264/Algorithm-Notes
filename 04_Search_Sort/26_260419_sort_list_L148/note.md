**[📍 현재 진도 체크]**
지금 우리는 **[STEP 4: 탐색 & 최적화]** 구간을 달리고 있어. STEP 3에서 트리랑 힙 부수면서 공간 데이터 다루는 법을 익혔고, 중간에 28번(이진 검색), 33번(슬라이딩 윈도우)은 먼저 맛을 봤네? 오늘은 정방향으로 돌아와서 **데이터를 원하는 대로 정렬하고 최적화하는 첫 단추**, 26번 문제로 들어간다! 

---

### # 1단계: 환경 세팅 지시 (Setup First)
IDE 켜고 바로 폴더랑 파일부터 만들자.

* **📂 찐최종 네이밍 룰:** `26_260419_sort_list_L148`
* **📄 파일 구성:** * `solution.py` (여기에 코드 작성)
    * `note.md` (접근 방식, 시간 복잡도 최적화 과정 기록)

---

### # 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 148: 리스트 정렬 (Sort List)
### 🔗 **링크:** [LeetCode 148: Sort List](https://leetcode.com/problems/sort-list/)

## **📜 문제 설명 (Mission Briefing)**
주어진 **연결 리스트(Linked List)**를 오름차순으로 정렬하는 문제야.
주의할 점은 일반적인 파이썬 리스트(배열) `[4, 2, 1, 3]`이 아니라, 노드와 포인터로 연결된 기차 꼬리잡기 형태의 자료구조라는 거야.
* **예시 1:** `head = [4, 2, 1, 3]` ➡️ `[1, 2, 3, 4]` (실제로는 `4 -> 2 -> 1 -> 3`을 `1 -> 2 -> 3 -> 4`로 바꾸는 것)
* **예시 2:** `head = [-1, 5, 3, 4, 0]` ➡️ `[-1, 0, 3, 4, 5]`

## **🎯 오늘 부술 for문 (Big-O 관점)**
문제 조건을 보면 노드의 개수 $N$이 최대 $5 \times 10^4$ 개야. 
무지성 이중 for문을 도는 버블 정렬이나 삽입 정렬($O(N^2)$)을 연결 리스트에 쓴다? 연산량이 $25억$ 번 터지면서 바로 Time Limit Exceeded(TLE) 맞고 퇴출이야.

LeetCode 문제 설명에도 **"Can you sort the linked list in $O(n \log n)$ time and $O(1)$ memory (i.e. constant space)?"** 라고 대놓고 못 박아놨어. 
형, 통계 분석할 때 데이터 너무 크면 파티셔닝해서 병렬 처리하고 다시 합치잖아? 똑같아. $O(N \log N)$을 달성하려면 리스트를 반으로 계속 쪼개고(Divide), 정렬하면서 다시 합치는(Conquer) **병합 정렬(Merge Sort)**이 국룰이야. (배열은 퀵 정렬도 좋지만, 연결 리스트는 인덱스 기반의 Random Access가 불가능해서 병합 정렬이 가장 안정적이고 빠름!)

## **🛠️ 네가 해야 할 것**
1.  **반으로 쪼개기 (Divide):** 연결 리스트의 정중앙을 찾아야 해. 연결 리스트는 길이를 미리 알 수 없으니 **'런너(Runner) 기법'**을 써서 반갈죽 해버려.
2.  **재귀적으로 쪼개기:** 리스트가 노드 1개짜리로 산산조각 날 때까지 계속 쪼개.
3.  **병합하기 (Merge):** 두 개의 정렬된 연결 리스트 조각을 크기 비교해가며 하나의 리스트로 이어 붙여. 이전에 풀어본 "두 정렬 리스트 병합" 로직을 여기서 재활용하는 거야.

## **🧰 필요한 파이썬 내장 함수/문법(범용사용법)**
연결 리스트의 중앙을 찾는 마법, **런너(Runner) 기법**을 기억해? 거북이(slow)와 토끼(fast)를 동시에 출발시키는 거야.
```python
# 런너 기법 (Fast & Slow Pointers) 범용 뼈대
# 연결 리스트의 '중간 지점'을 찾을 때 O(N)으로 한 방에 끝내는 테크닉

def find_middle(head):
    # slow는 1칸씩, fast는 2칸씩 뛴다
    slow = head
    fast = head
    
    # fast가 끝에 도달하면, slow는 정확히 중간에 있겠지?
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow # 이 녀석이 중간 노드!
```

---

### # 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

형이 IDE에서 바로 돌려보면서 테스트할 수 있게, 일반 배열을 `ListNode`로 바꿔주는 헬퍼 함수까지 스켈레톤에 다 세팅해뒀어. `sortList` 메서드 안의 로직만 집중해서 채워봐!

```python
from typing import Optional

# LeetCode에서 제공하는 연결 리스트 노드 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Base condition: 노드가 없거나 1개면 이미 정렬된 상태이므로 반환
        if not head or not head.next:
            return head
        
        # 2. 런너 기법으로 중간 노드 찾기 (리스트 반갈죽)
        # TODO: half, slow, fast 포인터를 이용해 리스트를 두 동강 내기
        
        # 3. 분할된 리스트를 재귀적으로 정렬
        # TODO: left = self.sortList(head), right = self.sortList(half)
        
        # 4. 정렬된 두 리스트를 병합 (Merge)
        # TODO: 별도의 merge 함수를 만들거나 안에서 병합하여 반환
        pass

# -------------------------------------------------------------
# 로컬 테스트용 헬퍼 함수들 (LeetCode 환경 모방)
# -------------------------------------------------------------
def build_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res) if res else "Empty")

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 기본 정렬 안 된 케이스
    head1 = build_linked_list([4, 2, 1, 3])
    print("Input 1:")
    print_linked_list(head1)
    print("Output 1:")
    print_linked_list(sol.sortList(head1))
    print("-" * 30)
    
    # Test Case 2: 음수 포함 및 홀수 개수
    head2 = build_linked_list([-1, 5, 3, 4, 0])
    print("Input 2:")
    print_linked_list(head2)
    print("Output 2:")
    print_linked_list(sol.sortList(head2))
    print("-" * 30)
    
    # Test Case 3: 엣지 케이스 (빈 리스트)
    head3 = build_linked_list([])
    print("Input 3:")
    print_linked_list(head3)
    print("Output 3:")
    print_linked_list(sol.sortList(head3))
    print("-" * 30)
    
    # Test Case 4: 엣지 케이스 (이미 정렬된 리스트)
    head4 = build_linked_list([1, 2, 3, 4, 5])
    print("Input 4:")
    print_linked_list(head4)
    print("Output 4:")
    print_linked_list(sol.sortList(head4))
```






<br><br><br><br><br><br><br>
---


### 💥 **[오늘 부순 for문 요약 (Big-O 관점)]**

* **시간 복잡도 (Time Complexity): $O(N \log N)$**
    * 리스트를 반으로 계속 쪼개는 깊이(Depth)가 $\log N$ 층이야.
    * 각 층에서 쪼개진 리스트들을 병합(Merge)하면서 전체 노드를 한 번씩 쭉 훑으니까 $O(N)$의 연산이 들어가.
    * 즉, 무지성 이중 for문($O(N^2)$)을 썼다면 $50,000 \times 50,000 = 25억$ 번 터졌을 연산량을, $50,000 \times \log_2(50,000) \approx 80만$ 번 수준으로 완벽하게 찢어버린 거지! 통계 모델링할 때 차원 축소해서 연산량 줄이는 거랑 똑같은 쾌감이야.
* **공간 복잡도 (Space Complexity): $O(\log N)$**
    * 재귀 함수를 호출하면서 $\log N$ 번의 콜 스택(Call Stack)이 쌓이게 돼.
    * *(참고: LeetCode 문제에서 요구한 $O(1)$ 공간 복잡도를 완벽히 맞추려면 재귀를 안 쓰고 반복문으로 밑에서부터 묶어 올라가는 Bottom-up 방식을 써야 하지만, 실전 인터뷰에서는 형이 짠 Top-down 재귀 방식이 코드가 훨씬 직관적이라 합격선으로 인정해 줘.)*

### 📝 **[오답 노트에 꼭 박아둘 2가지 핵심]**
1.  **런너(Runner) 기법의 엣지 케이스:** 노드가 2개일 때 무한 재귀에 안 빠지려면 토끼(`fast`)를 무조건 한 칸 앞(`head.next`)에서 출발시켜라!
2.  **파이썬 단축 평가 (Short-circuit):** `curr.next = left or right` 한 줄로 남은 연결 리스트 짬처리를 상수 시간 $O(1)$ 만에 우아하게 끝낼 수 있다!
