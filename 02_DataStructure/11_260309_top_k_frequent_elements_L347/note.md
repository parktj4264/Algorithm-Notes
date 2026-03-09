크~~~ 월요일 퇴근하고 피곤할 텐데 바로 코테 창 띄우는 이 성실함! 형님 진짜 올해 안에 뭐 하나 크게 터뜨리겠는데? 월요병 따위 알고리즘으로 찢어버리자고!

형님, 오늘 풀 **11번 문제**는 데이터 분석가/통계학 석사라면 진짜 숨 쉬듯이 해봤을 작업이야.
판다스(Pandas)에서 `df['column'].value_counts().head(K)` 치면 나오는 그거! "가장 많이 등장한 데이터 Top K개 뽑기"를 순수 파이썬 알고리즘으로 바닥부터 구현해 볼 거야.

형님이 요청한 대로 '예시' 팍팍 넣어서 미션 브리핑 들어간다!

---

# **1단계: 환경 세팅 지시 (Setup First)**

새로운 한 주의 시작, 폴더부터 깔끔하게 파자.

* **📂 찐최종 네이밍 룰:** `11_260309_top_k_frequent_elements_L347`
* **📄 파일 구성:** `solution.py`, `note.md`

---

# **2단계: 문제 및 가이드 제시 (Hard Mode)**

### 🚀 문제 11 (LeetCode 347): 상위 K 빈도 요소 (Top K Frequent Elements)

### 🔗 **링크:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

## **📜 문제 설명 (Mission Briefing):**

* **입력:** 1. `nums`: 숫자(데이터)들이 마구잡이로 들어있는 리스트.
2. `k`: 우리가 뽑아내고 싶은 "상위 랭킹(Top K)"의 개수.
* **출력:** 가장 많이 등장한(빈도수가 높은) 숫자 `k`개를 리스트로 묶어서 리턴해. (순서는 상관없어!)

### 💡 **구체적인 예시 (형님이 요청한 핵심!)**

**예시 1) 랭킹 2위까지 뽑아라! (`k = 2`)**

* **입력 데이터 (`nums`):** `[1, 1, 1, 2, 2, 3]`
* **상황 분석:** - `1`은 3번 등장했네. (빈도 1등 🥇)
* `2`는 2번 등장했네. (빈도 2등 🥈)
* `3`은 1번 등장했네. (빈도 3등 🥉)


* **목표:** `k=2`니까 빈도수 1등과 2등인 숫자를 뽑아야 해.
* **정답 (출력):** `[1, 2]`

**예시 2) 데이터가 하나밖에 없는데 1등을 뽑아라! (`k = 1`)**

* **입력 데이터 (`nums`):** `[777]`
* **상황 분석:** `777` 혼자 1번 등장.
* **정답 (출력):** `[777]`

**예시 3) 빈도가 똑같을 땐 어떡함?**

* LeetCode 문제 조건에 "정답은 항상 유일하게 나오도록 보장된다"고 되어 있으니까, 동점자 처리 같은 복잡한 예외는 걱정 안 해도 돼!

## **🎯 오늘 부술 for문 (Big-O 견적 & 설계 힌트):**

이 문제는 크게 **2단계**로 나뉘어. 형님이 이미 배운 **해시(딕셔너리)**와 **정렬(Sort)**을 콤보로 날리는 문제야.

1. **1단계: 빈도수 집계 (Frequency Counting)**
* `nums`를 한 바퀴 돌면서($O(N)$), 어떤 숫자가 몇 번 나왔는지 **딕셔너리(`dict`)**에 기록해. `{숫자: 등장 횟수}` 형태로!
* *💡 파이썬 고인물 팁:* 파이썬 내장 모듈인 `collections.Counter`를 쓰면 이 1단계를 단 한 줄로 끝낼 수 있어. (R의 `table()` 함수랑 똑같아)


2. **2단계: 빈도수 기준으로 정렬해서 Top K 뽑기 (Sorting)**
* 딕셔너리에 쌓인 데이터를 '등장 횟수(Value)' 기준으로 내림차순 정렬해야 해. ($O(N \log N)$)
* 정렬된 결과에서 앞에서부터 `k`개의 '숫자(Key)'만 똑 떼서 리스트로 리턴하면 끝!



## **🧰 필요한 파이썬 내장 함수/문법 (범용 사용법):**

딕셔너리를 정렬할 때 파이썬에서는 `lambda` (익명 함수)를 주로 써. 데이터 분석할 때 `apply(lambda x: ...)` 써봤지? 그거야!

```python
my_dict = {1: 3, 2: 2, 3: 1} # {숫자: 빈도수}

# 딕셔너리의 아이템(튜플 형태)을 '빈도수(x[1])' 기준으로 내림차순(reverse=True) 정렬!
sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# 결과: [(1, 3), (2, 2), (3, 1)]

```

---

# **3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)**

자, 딕셔너리 만들고 정렬하는 논리를 직접 짜보자. (`collections.Counter`를 써도 좋고, 순수하게 `dict`를 for문으로 채워도 좋아!)

```python
from typing import List
import collections # Counter를 쓰고 싶다면 활용해!

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass # 형님의 데이터 분석 짬바를 살려 이곳을 채우시오!

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 가장 기본적인 케이스
    print("Test 1 (Normal):", sol.topKFrequent([1,1,1,2,2,3], 2) == [1, 2])
    
    # Test 2: 원소가 1개일 때
    print("Test 2 (Single Element):", sol.topKFrequent([1], 1) == [1])
    
    # Test 3: 음수가 포함되어 있을 때 (음수도 정상적으로 카운트 되어야 함)
    print("Test 3 (Negative Numbers):", sol.topKFrequent([-1,-1,2,2,2,3], 2) == [2, -1])
    
    # Test 4: k가 전체 고유 숫자의 개수와 같을 때 (순서는 상관없으므로 set으로 비교)
    result4 = sol.topKFrequent([4,4,4,5,5,6], 3)
    print("Test 4 (All Unique Elements):", set(result4) == {4, 5, 6})

```

데이터 요약하고 `sort` 갈기는 거라 형님 전공 분야다!
타이머 30분 맞추고 백지부터 쫙 찢어봐! 막히면 바로 `print` 찍어본 거 들고 오고! 가즈아!





<br>
<br>
<br>
<br>
<br>





# 🚀 문제 11: 상위 K 빈도 요소 (Top K Frequent Elements, L347)
- **링크:** https://leetcode.com/problems/top-k-frequent-elements/
- **유형:** 해시 테이블 (Hash Map), 정렬 (Sorting), 힙 (Heap)
- **난이도:** Medium

## 🎯 Big-O 견적
- **무지성 접근:** 리스트의 `count()` 함수를 매번 호출하면 $O(N^2)$ 발생.
- **해결책 1 (수동 정렬):** 딕셔너리로 빈도수 집계 $O(N)$ + Value 기준 내림차순 정렬 $O(N \log N)$ $\rightarrow$ 최종 $O(N \log N)$
- **해결책 2 (Counter 객체):** 파이썬 내장 `collections.Counter`와 `most_common(k)` 사용. 내부적으로 Heap을 사용하여 $O(N \log k)$로 최적화됨.

## 💡 핵심 로직
1. **빈도수 해시맵 생성:** 리스트의 각 요소를 Key로, 등장 횟수를 Value로 하는 딕셔너리를 만든다.
2. **Value 기준 정렬:** `sorted()` 함수에 `key=lambda x: x[1]` (튜플의 두 번째 요소인 Value 기준)를 적용하여 정렬한다.

## 🐍 Pythonic Code
```python
from typing import List
from collections import Counter

class Solution:
    # 1. 실무 최적화 버전 (Counter & Heap)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most_common(k)는 [(요소1, 빈도1), (요소2, 빈도2)] 형태의 리스트 반환
        return [item[0] for item in Counter(nums).most_common(k)]

    # 2. 알고리즘 정석 버전 (Dict & Lambda Sort)
    def topKFrequent_study(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1 # if-else를 get()으로 압축
            
        # 딕셔너리를 Value(x[1]) 기준으로 내림차순 정렬
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_counts[:k]]
```