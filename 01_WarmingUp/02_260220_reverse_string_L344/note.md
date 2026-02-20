현재 진도: **STEP 1 (워밍업) ➔ [진행 중: 2/38]**

---

### 🚀 문제 344: Reverse String (문자열 뒤집기)

🔗 **링크:** [https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/)

**1단계: 환경 세팅 지시 (Setup First)**

터미널 켜고 오늘 날짜(2월 20일)로 폴더부터 파라.

* 📂 **폴더:** `01_WarmingUp/02_260220_reverse_string_L344`
* 📄 **파일:** `solution.py`, `note.md`

만들었으면 `solution.py` 열어. 문제 나간다.

**2단계: 문제 및 가이드**

**[문제 설명]**
문자열을 뒤집는 함수를 작성해라. 입력값은 문자 배열(List of strings)이다.
단, 리턴하지 말고 **입력 배열 내부를 직접 수정(In-place)해야 한다.** (공간 복잡도  제한)

**[통계학 석사님을 위한 비유]**
형님, 이거 통계에서 **'중위수(Median)'** 찾을 때 양 극단(Min, Max)에서부터 하나씩 지워가면서 가운데로 좁혀 들어가는 거랑 똑같은 원리야.
왼쪽 끝(Left)이랑 오른쪽 끝(Right)에 포인터를 두고, 두 값을 **스왑(Swap)**한 다음 한 칸씩 가운데로 이동하는 거지. 두 포인터가 교차하면 끝나는 거고. 이걸 **투 포인터(Two Pointer)** 알고리즘이라고 해.
메모리(RAM)에 100GB짜리 행렬 올려놨는데, 그거 뒤집겠다고 새로운 100GB짜리 객체(`new_s = ...`) 또 만들면 OOM(Out of Memory) 뜨고 서버 터지겠지? 그래서 **제자리(In-place)**에서 값만 쇽쇽 바꾸는 게 핵심이야.

**[제약 사항 & 잔소리]**

1. 어제 배운 `s[::-1]` 쓰면 안 돼. 이건 '새로운 리스트'를 반환하기 때문에 공간 복잡도 $O(N)$이 돼버려. (정확히는 LeetCode에서 `s[:] = s[::-1]` 같은 꼼수가 통하긴 하지만, 지금은 투 포인터 원리를 배우는 게 목적이니까 봉인!)
2. 파이썬의 스왑은 개사기야. R에서는 임시 변수 `temp` 만들어서 복잡하게 바꿨지? 파이썬은 그냥 `a, b = b, a` 하면 끝이다.

**3단계: 실행 가능한 코드 스켈레톤**

아래 코드 긁어서 `solution.py`에 붙여넣어라.

```python
import sys
from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    :param s: 문자열 리스트
    """
    # 💡 쌤의 힌트:
    # 1. 왼쪽 인덱스(left)는 0, 오른쪽 인덱스(right)는 len(s) - 1 에서 시작.
    # 2. left가 right보다 작을 때까지 반복(while)하면서
    # 3. s[left]와 s[right]의 값을 서로 Swap!
    # 4. left는 1 증가, right는 1 감소시키며 가운데로 좁혀온다.
    
    pass

if __name__ == "__main__":
    # 예제 테스트 케이스 1
    s1 = ["h","e","l","l","o"]
    print(f"Test Input 1 (Before): {s1}")
    reverseString(s1)
    print(f"Result 1 (After)   : {s1}") # ["o","l","l","e","h"] 나와야 함
    
    print("-" * 30)
    
    # 예제 테스트 케이스 2
    s2 = ["H","a","n","n","a","h"]
    print(f"Test Input 2 (Before): {s2}")
    reverseString(s2)
    print(f"Result 2 (After)   : {s2}") # ["h","a","n","n","a","H"] 나와야 함

```

**[Next Step]**
자, 이번 미션은 **투 포인터(Two Pointer)**로 직접 구현해보는 거다.
형님 머리 좋으니까 10분이면 짤 거야. `solution.py` 채우고 다 돌아가면 코드 올려! 코드 리뷰 들어간다. 실시!




---


# 📓 2일차 오답노트 (26.02.20)
## 🚀 문제 344: Reverse String (문자열 뒤집기)

### 1. 내가 시도한 접근법 & 논리적 버그 해결
- **초기 실수:** 스왑(`a, b = b, a`)을 먼저 하고 멈춤(`break`) 조건을 체크해서, 짝수 길이 배열의 경우 중앙을 넘어가며 다시 원상 복구되는 'Double Swap' 버그 발생. (교호작용 통제 실패)
- **해결:** `break` 조건문(`front_index >= end_index`)을 스왑 로직 위로 올려서 '얼리 스토핑(Early Stopping)' 구현 완료. 로직 정상화.

### 2. 배운 점 (투 포인터의 정석: While vs For)
- 내 코드는 논리적으로 맞지만, `for i in range(len(s))`는 배열 전체를 순회하겠다는 의도를 내포하므로 절반만 도는 로직에는 어색함.
- **파이썬 코테의 국룰:** 양 끝에서 중앙으로 좁혀오는 투 포인터(Two Pointers)는 무조건 **`while left < right:`** 구조를 쓴다. 가독성이 압도적으로 좋고 홀/짝 길이 예외 처리가 필요 없다.
- **In-place 제약:** 공간 복잡도 $O(1)$을 지키기 위해 새로운 배열을 만들지 않고 기존 배열 내에서 인덱스만 활용해 Swap 처리함.

### 3. 핵심 코드 (The Pythonic Way)
```python
# 형님의 최종 통과 로직을 가장 파이썬답게(Pythonic) 바꾼 버전
left, right = 0, len(s) - 1

while left < right:
    # 파이썬 개사기 스왑
    s[left], s[right] = s[right], s[left]
    # 포인터 이동
    left += 1
    right -= 1
