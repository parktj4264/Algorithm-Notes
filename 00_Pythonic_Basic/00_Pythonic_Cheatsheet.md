# PYTHONIC HIGH-LEVEL CHEATSHEET

`00_Pythonic_Basic` 핵심을 코딩테스트/실무 기준으로 1장에 압축한 고수준 치트시트.

---

## 0. Core Principle
1. 차수 먼저: `O(N^2)`를 `O(N log N)` 또는 `O(N)`으로 낮춘다.
2. 자료구조 다음: `list`보다 `set/dict/deque`가 맞는지 먼저 본다.
3. 문법 최적화 마지막: comprehension, built-in으로 상수항을 줄인다.

---

## 1. Big-O + Runtime Reality
- `O(1)`: 상수 시간
- `O(N)`: 선형
- `O(N log N)`: 정렬/분할
- `O(N^2)`: 이중 루프 (N 커지면 위험)

### 왜 파이썬 루프가 느릴 수 있나
- 인터프리터 opcode dispatch
- 객체(`PyObject`) 접근/타입 분기
- 포인터 추적 + 캐시 미스

### 빠른 기본기
```python
# Bad
total = 0
for x in arr:
    total += x

# Better (C-level built-in path)
total = sum(arr)
```

---

## 2. list (Dynamic Array)
- 인덱스 조회: `O(1)`
- `append/pop()`(끝): 평균 `O(1)`
- `insert(0, x)` / `pop(0)`: `O(N)`

### 큐 안티패턴
```python
# Bad
q = [1, 2, 3]
q.pop(0)  # O(N)

# Good
from collections import deque
q = deque([1, 2, 3])
q.popleft()  # O(1)
```

### list comprehension
```python
# Good
evens_sq = [x * x for x in nums if x % 2 == 0]
```

---

## 3. dict / set (Hash Table)
- 조회/삽입/삭제 평균 `O(1)`
- membership 검사에 최적

```python
# membership
seen = set()
for x in nums:
    if x in seen:
        return True
    seen.add(x)

# counting
from collections import Counter
freq = Counter(words)

# grouping
from collections import defaultdict
g = defaultdict(list)
for k, v in pairs:
    g[k].append(v)
```

### 핵심 주의
- Python 3.7+ dict insertion order 보장
- 그래도 문제에서 순서를 엄격히 요구하면 명시적 정렬/검증

---

## 4. Loop Upgrade (`enumerate`, `zip`, `generator`)
```python
# enumerate: index + value
for i, v in enumerate(arr):
    ...

# zip: 병렬 순회
for a, b in zip(arr1, arr2):
    ...

# generator: lazy
def gen(n):
    for i in range(n):
        yield i
```

### 대용량 메모리 규칙
- 한 번에 다 만들 필요 없으면 list 대신 generator/range 우선

---

## 5. String Handling
- 문자열은 immutable
- 루프에서 `+=` 반복은 누적 재할당 비용 위험
- 누적 결합은 `''.join(parts)` 사용

```python
# Good
parts = []
for token in tokens:
    parts.append(token)
s = ''.join(parts)
```

### 전처리 표준 템플릿
```python
import re

def normalize(s: str) -> str:
    s = s.lower()
    return re.sub(r'[^a-z0-9]', '', s)
```

### 회문 템플릿
```python
def is_palindrome(s: str) -> bool:
    s = normalize(s)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
```

---

## 6. 실전 30초 체크리스트
1. 입력 최대 N으로 허용 복잡도 먼저 고정했는가?
2. `x in list` 반복을 `set/dict`로 바꿀 수 있는가?
3. `pop(0)`/중간 삽입 같은 `O(N)` 연산이 루프 안에 있는가?
4. 문자열 누적을 `+=`로 하고 있지 않은가?
5. 빈 입력/길이 1/중복/경계 인덱스 테스트 했는가?

---

## 7. 면접용 3문장 템플릿
- "먼저 N 범위로 목표 복잡도를 정했고, 그에 맞춰 자료구조를 선택했습니다."
- "membership가 병목이라 list 대신 set으로 바꿔 평균 `O(1)` 조회를 확보했습니다."
- "마지막으로 built-in/comprehension으로 상수항을 줄였습니다."
