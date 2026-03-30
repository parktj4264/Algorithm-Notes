우리가 오늘 부술 진짜 문제는 **[STEP 3]의 마지막 하이라이트, 힙(Heap / Priority Queue)** 파트인 **24번 문제**야!

---

# 1단계: 환경 세팅 다시! (Setup First)

터미널 파일명 새로 파자! 

* **📂 찐최종 네이밍 룰:** `24_260330_kth_largest_element_L215`
* **📄 파일 구성:** `solution.py`

---

# 2단계: 문제 및 가이드 제시 (The 'Heap' Perspective)

### 🚀 문제 215: Kth Largest Element in an Array
### 🔗 **링크:** [https://leetcode.com/problems/kth-largest-element-in-an-array/](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## **📜 문제 설명 (Mission Briefing):**
정렬되지 않은 정수 배열 `nums`와 정수 `k`가 주어졌을 때, 배열에서 **$k$번째로 큰 요소**를 찾는 문제야. 
(주의: 중복된 값이 있어도, 순위를 매길 때는 있는 그대로 다 카운트해야 해!)

* **예시 1:** `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
  * 내림차순 정렬하면 `[6, 5, 4, 3, 2, 1]` 이지? 여기서 2번째로 큰 건 `5`!

## **🎯 오늘 부술 로직 (Big-O 관점 & 통계학 비유):**
가장 1차원적인 생각: "어? 그냥 파이썬 `nums.sort(reverse=True)` 하고 `nums[k-1]` 뽑으면 되는 거 아님?"
물론 정답이야! 하지만 전체 데이터를 다 정렬하는 데는 시간 복잡도 **$O(N \log N)$**이 걸려. 데이터가 100만 개면 100만 개를 싹 다 정렬해야 하니까 비효율적이지. 통계로 치면 "상위 10개만 알고 싶은데, 굳이 100만 명의 등수를 꼴찌까지 다 매겨야 하나?" 랑 똑같은 고민이야.

이때 꺼내는 파이썬의 치트키가 바로 **'힙(Heap / Priority Queue)'**이야! 
힙은 **"항상 가장 작은 놈(또는 큰 놈)이 맨 꼭대기에 올라오는 반자동 정렬 트리"**야.

우리는 파이썬 내장 모듈인 `heapq` (최소 힙, Min-Heap)을 써서 **딱 $K$명만 들어가는 VIP 대기실(Heap)**을 만들 거야.
1. 배열의 숫자를 하나씩 VIP 대기실에 넣는다.
2. 대기실 인원이 $K$명을 초과하면? **가장 작은 놈(맨 꼭대기에 있는 놈)을 쫓아낸다!** (`heappop`)
3. 이걸 끝까지 반복하면, VIP 대기실에는 결국 **'배열에서 가장 큰 $K$개의 숫자'**만 남게 되겠지?
4. 그리고 그 대기실의 문지기(맨 꼭대기 값, `heap[0]`)가 바로 **우리가 찾는 $K$번째로 큰 값**이 되는 거야!

이렇게 하면 시간 복잡도를 **$O(N \log K)$**로 극적으로 줄일 수 있어. ($K$가 작을수록 $O(N)$에 가까워짐!)

## **🛠️ 네가 해야 할 것:**
* 파이썬의 `heapq` 모듈 사용법만 알면 5줄 컷 나는 문제야.
* `heapq.heappush(hq, num)`: 힙에 데이터 넣기
* `heapq.heappop(hq)`: 힙에서 가장 작은 데이터 빼기




```python
import heapq

# 1. 힙 생성 (전용 클래스가 아님! 그냥 빈 리스트를 만듦)
hq = []

# 2. 데이터 삽입 O(log N)
heapq.heappush(hq, 5)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
# 현재 hq 상태: [1, 5, 3] -> 1이 알아서 맨 앞으로 튀어 올라옴!

# 3. 데이터 추출 (가장 작은 값 빼기) O(log N)
min_val = heapq.heappop(hq)
# min_val은 1이 되고, 남은 [5, 3]은 다시 내부적으로 정렬되어 [3, 5]가 됨.

# 4. 🚨 [개꿀팁] 기존 리스트를 한 방에 힙으로 변환하기 O(N)
# 데이터를 하나씩 push 하면 O(N log N)이지만, heapify를 쓰면 O(N)으로 압축됨!
nums = [4, 1, 7, 3, 8, 5]
heapq.heapify(nums) 
print(nums) # [1, 3, 5, 4, 8, 7] (맨 앞이 1인 최소 힙 상태로 변신)
```




---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

파이썬의 `heapq`를 처음 써보는 거라면, 코드를 짜면서 이 자료구조가 알아서 정렬을 유지해 주는 쾌감을 느낄 수 있을 거야!

```python
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [] # K명만 들어갈 VIP 대기실 (Min-Heap)
        
        for num in nums:
            # 1. 일단 현재 숫자(num)를 대기실(hq)에 밀어 넣기 (heappush 사용)
            pass
            
            # 2. 만약 대기실 인원(len)이 K명을 초과했다면?
            # 제일 만만한 놈(최솟값)을 쫓아내기! (heappop 사용)
            pass
            
        # 3. 배열을 다 돌고 나면, 대기실(hq)에는 가장 큰 K명만 남고,
        # 그중 가장 작은 값(문지기)이 hq[0]에 위치하게 됨! 그 값을 리턴!
        pass


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print("TC 1:", sol.findKthLargest(nums1, k1)) # 예상 결과: 5
    
    # Test Case 2 (중복 데이터 포함)
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print("TC 2:", sol.findKthLargest(nums2, k2)) # 예상 결과: 4
```





<br><br><br><br><br><br><br><br><br>




# 📝 [복습 노트] 24. 배열의 K번째 큰 요소 (LeetCode 215)
**날짜:** 2026-03-31
**소요 시간:** 10분 컷 (힙 원리 파악 완료 🔥)

## 1. 🎯 핵심 로직: VIP 대기실 (Min-Heap of size K)
* **문제점:** 무지성 `sort()`는 $O(N \log N)$이 걸린다. 데이터가 1000만 개인데 3등만 찾고 싶을 때 비효율적!
* **해결책:** 파이썬의 `heapq`(최소 힙)를 이용해, 크기가 딱 $K$로 고정된 'VIP 대기실'을 운영한다.

## 2. 🐍 파이썬 힙(Heapq) 치트키 활용
* 배열의 숫자를 하나씩 힙에 넣는다. `heappush(hq, num)`
* 힙의 크기가 $K$를 초과하면, 맨 위(가장 작은 값)를 쫓아낸다! `heappop(hq)`
* 끝까지 순회하고 나면 힙에는 '가장 큰 $K$개의 숫자'만 남고, 힙의 루트(`hq[0]`)가 그중 가장 작은 값, 즉 **$K$번째로 큰 값**이 된다!

## 3. 📊 Big-O (시공간 복잡도)
* **시간 복잡도 $O(N \log K)$:** 배열 순회 $O(N)$ $\times$ 힙 삽입/삭제 $O(\log K)$. 전체 정렬($O(N \log N)$)보다 압도적으로 빠르다!
* **공간 복잡도 $O(K)$:** 메모리에는 항상 $K$개의 데이터만 존재함.