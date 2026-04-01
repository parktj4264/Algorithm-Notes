**📍 [진도 체크]**
드디어 대망의 시간이야. 오늘은 **[STEP 3 (자료구조 2 - 공간 데이터)]**의 **진짜 최종 보스**이자, 이 리스트의 첫 번째 **'Hard'** 난이도 문제를 부술 거야.
어제 형이 완벽하게 깨달은 **'힙(Heap) VIP 대기실'** 개념을 연결 리스트(Linked List)에 스까먹는 문제거든? 어제 힙을 마스터했기 때문에 오늘은 Hard 난이도여도 진짜 콧노래 부르면서 풀 수 있을 거다!

---

# 1단계: 환경 세팅 지시 (Setup First)

터미널 열고 오늘 날짜(26년 4월 1일) 파일 딱 세팅하자! 

* **📂 찐최종 네이밍 룰:** `25_260401_merge_k_sorted_lists_L23`
* **📄 파일 구성:** `solution.py`

---

# 2단계: 문제 및 가이드 제시 (The 'Heap' Perspective)

### 🚀 문제 23: Merge k Sorted Lists (🚨 난이도: Hard)
### 🔗 **링크:** [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

## **📜 문제 설명 (Mission Briefing):**
각각 **오름차순으로 정렬된 $K$개의 연결 리스트(Linked List)**가 주어져. 
이 $K$개의 리스트를 싹 다 하나로 합쳐서, **단 하나의 정렬된 연결 리스트**로 반환하는 문제야.

* **예시 1:**
  * `list1 = 1 -> 4 -> 5`
  * `list2 = 1 -> 3 -> 4`
  * `list3 = 2 -> 6`
  * **결과:** `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`

## **🎯 오늘 부술 로직 (데이터 파이프라인 병합):**
이거 현업에서 어떻게 비유할 수 있냐면, 삼성 Fab 장비 $K$대에서 각각 시간순(오름차순)으로 정렬된 로그 파일이 쏟아져 나오고 있는데, 이걸 하나의 마스터 로그 파일로 시간순 정렬해서 합쳐야 하는 상황이랑 똑같아.

무지성으로 다 때려 넣고 `sort()` 돌리면? 시간 복잡도 폭발하겠지.
우리는 어제 만든 **'최소 힙(Min-Heap)' VIP 대기실**을 쓸 거야!

1. **대표 선발:** $K$개 리스트의 **맨 앞(가장 작은 값)** 노드들만 딱 뽑아서 VIP 대기실(힙)에 넣는다. (대기실 크기는 최대 $K$명)
2. **1등 뽑기:** 대기실에서 가장 작은 놈을 하나 뽑아(`heappop`) 정답 리스트에 이어 붙인다.
3. **다음 타자 입장:** 방금 뽑힌 놈이 속했던 리스트에서, **그다음 노드**를 대기실로 올려보낸다(`heappush`).
4. 대기실이 텅 빌 때까지 반복!

## **🚨 파이썬 고인물만 아는 함정 주의 (TypeError):**
파이썬 `heapq`에 튜플 `(값, 노드)` 형태로 넣으면, '값'이 똑같을 때 파이썬이 "어? 값이 같네? 그럼 두 번째 요소인 '노드'끼리 크기 비교해야지!" 하고 `node1 < node2`를 시도해. 근데 리트코드 `ListNode` 객체끼리는 대소 비교가 안 돼서 **에러가 터져버려!**

그래서 힙에 넣을 때는 **고유한 번호(리스트의 인덱스 `i`)를 중간에 끼워 넣어서 `(값, 인덱스, 노드)` 형태**로 넣어줘야 해. 이러면 값이 같아도 인덱스로 비교가 끝나니까 에러가 안 나! (진짜 꿀팁임)

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

자, 힙의 우아함과 연결 리스트의 쫀득한 맛을 동시에 느낄 수 있는 뼈대 코드 들어간다!

```python
import heapq
from typing import List, Optional

# 리트코드에서 제공하는 단일 연결 리스트 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        
        # 1. 각 리스트의 '첫 번째 노드(대표)'들을 힙에 넣기
        for i, node in enumerate(lists):
            if node:
                # 🚨 에러 방지용 치트키: (노드의 값, 리스트 번호 i, 노드 객체) 튜플로 넣음!
                heapq.heappush(hq, (node.val, i, node))
                
        # 정답을 이어 붙일 가짜(Dummy) 헤드 노드 하나 생성
        dummy = ListNode(0)
        curr = dummy
        
        # 2. VIP 대기실이 텅 빌 때까지 무한 반복
        while hq:
            # 2-1. 대기실에서 제일 작은 놈을 뽑기 (val, i, node 추출)
            pass
            
            # 2-2. 정답 리스트(curr)의 다음에 방금 뽑은 node를 연결하고, curr 전진시키기
            pass
            
            # 2-3. 방금 뽑힌 node에게 '다음 노드(node.next)'가 있다면?
            # 그놈을 다시 대기실(hq)에 넣어주기! (주의: 리스트 번호 i도 같이 넣어야 함)
            pass
            
        return dummy.next

# 🎁 연결 리스트를 예쁘게 출력/생성하는 헬퍼 함수 (디버깅용)
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: [[1,4,5], [1,3,4], [2,6]]
    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    lists1 = [l1, l2, l3]
    
    print("TC 1 결과:")
    ans1 = sol.mergeKLists(lists1)
    print_linked_list(ans1) 
    # 예상 결과: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

어제 힙(`heappush`, `heappop`) 다뤄봐서 아주 손에 익었지? 
오늘은 뽑아낸 다음에 **"내 뒤에 있던 다음 사람(node.next) 대기실로 들여보내기"**만 추가하면 돼. Hard 문제지만 체감 난이도는 Easy일 거다. 다 짜면 바로 들고 와!! 🚀



<br><br><br><br><br><br><br>




# 📝 [복습 노트] 25. K개 정렬 리스트 병합 (LeetCode 23) 🚨 Hard
**날짜:** 2026-04-01
**소요 시간:** 30분 컷 (Hard 난이도를 혼자 힘으로 분쇄 🔥)

## 1. 🎯 핵심 로직: VIP 대기실 + 기차 밧줄 당기기
* **문제점:** $K$개의 연결 리스트를 무지성으로 합치고 정렬하면 시간이 터진다.
* **해결책:** 크기가 $K$인 **최소 힙(Min-Heap)**을 운용하여, 각 리스트의 대가리(Head)만 모아 실시간으로 최솟값을 뽑아낸다.

## 2. 🐍 파이썬 힙 + 연결 리스트 꿀팁
1. **TypeError 방지:** 힙에 객체를 넣을 때 값이 같으면 에러가 나므로, 타이브레이커(Tie-breaker)로 고유 인덱스 `i`를 끼워 넣는다. `(val, i, node)`
2. **밧줄 당기기:** 힙에서 최솟값 노드를 뽑아 정답 리스트에 붙인 후, 그 노드의 꼬리(`.next`)가 존재한다면 다시 힙으로 밀어 넣는다!
3. **🪄 객체 재활용과 덮어쓰기 마술:** 값을 복사해서 `ListNode(val)`를 새로 만들지 않고, 뽑아낸 `node` 객체 자체를 `curr.next = popped_node`로 냅다 이어 붙이면 메모리가 극도로 절약된다. 
   *(뒤에 통째로 딸려온 꼬리칸들은 어차피 다음 번 루프에서 새로운 노드를 `.next`에 덮어쓸 때 밧줄이 싹둑 잘려나가므로 정답을 망치지 않는다!)*

## 3. 📊 Big-O (시공간 복잡도)
* **시간 복잡도 $O(N \log K)$:** $N$개의 모든 노드가 한 번씩 크기 $K$의 힙에 들어갔다 나온다.
* **공간 복잡도 $O(K)$:** 새로운 노드를 생성하지 않고 밧줄만 고쳐 맸으므로, 메모리에는 힙 대기실 공간($K$)만 추가로 필요하다!