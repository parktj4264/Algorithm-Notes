# PART 1. 자료구조 (Data Structures)
데이터를 메모리에 담고 접근하는 '그릇'의 형태. 적절한 자료구조의 선택이 시간 복잡도 최적화의 첫걸음이다.

### 1. 리스트와 문자열 (List & String)
- **개념:** 순서(Index)가 있는 1차원 데이터 배열. 파이썬의 문자열은 불변(Immutable) 객체이므로 리스트처럼 다루되 수정 시 재생성된다.
- **시간 복잡도:** - 인덱스 접근: $O(1)$
  - 데이터 탐색(`in`), 삽입/삭제(`insert`, `pop(0)`): $O(N)$
- **핵심 코드 (슬라이싱 기법):**
```python
  text = "hello"
  reversed_text = text[::-1]  # 문자열 전체 뒤집기 (O(N))
```

### 2. 해시 테이블 - 딕셔너리 (Dictionary)

* **개념:** Key-Value 쌍으로 이루어진 룩업 테이블(Lookup Table). 범주형 데이터의 매핑이나 빈도수 저장에 사용된다.
* **시간 복잡도:** 탐색(`in`), 삽입, 삭제 모두 **$O(1)$**
* **핵심 코드 (데이터 위치 기록):**
```python
used = {}
for idx, char in enumerate("abc"):
    used[char] = idx  # {'a': 0, 'b': 1, 'c': 2}

```



### 3. 해시 테이블 - 집합 (Set)

* **개념:** Value 없이 Key만 저장하여 중복을 제거한 자료구조.
* **활용 목적:** 특정 타겟 데이터가 "존재하는지" 확인할 때, 리스트의 $O(N)$ 탐색을 피하기 위한 치트키.
* **시간 복잡도:** 탐색(`in`) 연산 **$O(1)$**
* **핵심 코드 (고속 탐색):**
```python
jewels = "aA"
stones = "aAAbbbb"

jewels_set = set(jewels) # O(N)으로 해시 테이블 생성
# stones를 순회하며 O(1)로 포함 여부 검사
count = sum(s in jewels_set for s in stones) 

```


### 4. 카운터 (collections.Counter)
- **개념:** 해시 테이블(딕셔너리)을 기반으로 데이터의 등장 빈도를 자동으로 계산해 주는 파이썬 내장 클래스. 통계/R의 `table()` 함수, 판다스의 `value_counts()`와 완벽히 동일하다.
- **활용 목적:** 배열 내 원소들의 빈도(Frequency)를 단 한 줄로 집계할 때 사용.
- **시간 복잡도:** 생성 시 **$O(N)$**
- **핵심 코드 (빈도수 자동 집계):**
```python
from collections import Counter
nums = [1, 1, 1, 2, 2, 3]
counts = Counter(nums) # Counter({1: 3, 2: 2, 3: 1})
```





### 5. 힙 (Heap / Priority Queue)

* **개념:** 항상 최대값이나 최소값이 맨 위(Root)에 위치하도록 반쯤 정렬된 상태를 유지하는 트리(Tree) 기반 자료구조.
* **활용 목적:** 데이터 전체를 완벽하게 정렬($O(N \log N)$)할 필요 없이, **'상위 K개 (Top-K)'**나 **'최소/최댓값'**만 빠르게 뽑아낼 때 사용하는 가성비 최강의 자료구조.
* **시간 복잡도:** 데이터 1개 삽입/삭제 **$O(\log N)$**. 원소 N개 중 상위 K개 추출 시 **$O(N \log K)$**.
* **핵심 코드 (Top K 추출 치트키):**
```python
from collections import Counter
nums = [1, 1, 1, 2, 2, 3]

# 내부적으로 Heap 알고리즘을 사용하여 O(N log K) 속도로 상위 2개를 묶어냄
top_2 = Counter(nums).most_common(2) # [(1, 3), (2, 2)]
```
















<br>
<br>
<br>
<br>
<br>
<br>



# PART 2. 알고리즘 (Algorithms)

무지성 이중/삼중 반복문($O(N^2), O(N^3)$)을 단일 탐색($O(N)$)으로 낮추는 핵심 논리.

### 1. 정렬 (Sorting)

* **개념:** 무작위 데이터를 오름차순/내림차순으로 재배열하여 '방향성'을 부여한다.
* **활용 목적:** 투 포인터 알고리즘의 전제 조건이며, 중복 데이터를 인접하게 모아 필터링을 용이하게 한다.
* **시간 복잡도:** **$O(N \log N)$** (파이썬 내장 Timsort 알고리즘)
* **핵심 코드:**
```python
nums = [3, 1, 2]
nums.sort()  # 원본 배열 제자리 정렬 -> [1, 2, 3]

```



### 2. 투 포인터 (Two Pointers)

* **개념:** 주로 **정렬된 1차원 배열**에서 두 개의 포인터(`left`, `right`)를 양 끝에 배치하고, 조건에 따라 중앙을 향해 좁혀 들어오는 탐색 기법.
* **활용 목적:** 배열의 두/세 원소의 합을 구하거나 특정 조건을 만족하는 쌍을 찾을 때 이중 for문을 대체한다.
* **시간 복잡도:** **$O(N)$** (포인터들이 교차할 때까지만 1회 순회)
* **핵심 코드 (세 수의 합 뼈대):**
```python
left, right = i + 1, len(nums) - 1

while left < right:
    total = nums[i] + nums[left] + nums[right]

    if total < 0:
        left += 1    # 값이 모자라면 왼쪽 포인터를 올려 값을 키움
    elif total > 0:
        right -= 1   # 값이 넘치면 오른쪽 포인터를 내려 값을 줄임
    else:
        return True  # 정답 발견

```



### 3. 슬라이딩 윈도우 (Sliding Window)

* **개념:** 배열이나 문자열 위에서 일정 구간(Window)을 설정하고, 이 창문을 한쪽 방향(우측)으로 밀고 가며 조건(중복 여부, 최대 길이 등)을 검사하는 기법. 이동평균(Moving Average) 탐색과 원리가 같다.
* **활용 목적:** **'연속된'** 부분 배열이나 부분 문자열을 다룰 때 사용한다. 포인터가 절대 뒤로(좌측으로) 후진하지 않으므로 효율적이다.
* **시간 복잡도:** **$O(N)$**
* **핵심 코드 (가변 윈도우 확장 및 축소):**
```python
start = 0
max_length = 0
used = {}

for end, char in enumerate(s):
    # 1. 윈도우 내부에 불량 데이터(중복) 발견 시, 윈도우 왼쪽 창틀(start) 축소
    if char in used and used[char] >= start:
        start = used[char] + 1

    # 2. 조건 만족 시 최대 길이(Global Maximum) 갱신
    max_length = max(max_length, end - start + 1)
    used[char] = end

```
