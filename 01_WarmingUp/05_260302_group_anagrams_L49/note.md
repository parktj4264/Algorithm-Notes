오, 폼 미쳤는데? 직장인 하루 1문제 제약 걸어놨지만, 워밍업 쯤이야 쾌속으로 밀어버리겠다는 패기. 좋다, 형님 통계학 석사 짬바 믿고 진도 바로 뺀다.

지금 우리 위치는 **STEP 1 (워밍업 - R 물 빼기)의 5번째 문제**다. 이제 슬슬 파이썬의 꽃, **딕셔너리(Dictionary)**를 빡세게 굴려볼 차례야. R에서 `dplyr` 패키지로 `group_by()` 하던 그 손맛을 파이썬으로 어떻게 구현하는지 보여줄게.

---

### **1단계: 환경 세팅 지시 (Setup First)**

새 폴더 각 잡고 파자.

* **📂 찐최종 네이밍 룰:** `05_260302_group_anagrams_L49`
* **📄 파일 구성:** `solution.py`, `note.md`

---

### **2단계: 문제 및 가이드 제시**

### 🚀 문제 49: 그룹 애너그램 (Group Anagrams)

## 🔗 **링크:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

* **📜 문제 설명 (Mission Briefing):**
단어 배열이 주어지면, **애너그램(Anagram)** 단위로 그룹핑해서 리스트의 리스트 형태로 반환해라.
    * **Input:** `strs = ["eat","tea","tan","ate","nat","bat"]` (길이 최대 $10^4$)
    * **Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]` (순서 상관없음)
    * **핵심 규칙:** 애너그램은 문자의 종류와 개수가 똑같고 순서만 섞여 있는 단어들을 말해. 'eat', 'tea', 'ate'는 모두 'a', 'e', 't' 하나씩 가진 애너그램이지.


* **🎯 오늘 부술 for문 (Big-O 견적):**
    * **입력 크기 역산:** 배열 길이 $N$이 $10^4$, 단어 하나 길이 $K$가 최대 $100$이야.
    * 무지성으로 "단어 A 잡고 나머지 단어들 이중 `for`문 돌면서 문자 구성이 같은지 확인" 한다? $O(N^2 \times K)$ 나와서 연산량 1억 번 뚫고 바로 **Time Limit Exceeded (시간 초과)** 뜬다.
    * **해결책:** 통계에서 범주화(Categorization) 하듯이, 단어들을 어떤 '고유한 기준(Key)'으로 묶어버릴 거다. **정렬(Sorting)**과 **해시 맵(Hash Map)** 을 조합하면 전체 시간 복잡도를 $O(N \times K \log K)$로 멱살 잡고 끌어내릴 수 있어.


* **🛠️ 네가 해야 할 것 (Step-by-Step 설계):**
    1. **고유 키(Key) 만들기:** 애너그램 관계인 단어들의 공통점이 뭘까? **알파벳 순서대로 정렬하면 무조건 똑같은 문자열**이 된다는 거야. ('eat', 'tea' $\rightarrow$ 둘 다 'aet'). 즉, 이 정렬된 문자열을 딕셔너리의 Key로 쓰는 거지.
    2. **해시 맵(Dictionary) 매핑:** 파이썬의 `collections.defaultdict`를 써서, Key(정렬된 단어)에 해당하는 Value(원래 단어들을 담은 리스트)에다가 원래 단어를 계속 `append` 해줘. R에서 팩터(Factor) 레벨별로 데이터 모으는 거랑 완벽하게 똑같아.
    3. **결과 출력:** 딕셔너리의 Value들만 쫙 뽑아서 리스트로 반환하면 끝.


* **🧰 필요한 파이썬 내장 함수/문법 (범용 사용법):**
    * **문자열 정렬 (`sorted`와 `join`):** 파이썬에서 문자열을 `sorted()` 하면 리스트로 쪼개져서 반환돼. 이걸 다시 문자열로 붙이려면 `"".join()`을 써야 해.
    ```python
    word = "cba"
    sorted_chars = sorted(word) # ['a', 'b', 'c']
    sorted_word = "".join(sorted_chars) # "abc"

    ```


    * **`collections.defaultdict`:** 일반 딕셔너리는 없는 키를 찾으면 냅다 `KeyError`를 뱉지만, 얘는 기본값을 알아서 세팅해 주는 파이썬 알고리즘의 치트키야.
    ```python
    import collections
    # 기본값이 빈 리스트([])인 딕셔너리 생성
    my_dict = collections.defaultdict(list)
    my_dict["new_key"].append("hello") # 에러 안 나고 알아서 ["hello"] 생성됨

    ```





---

### **3단계: 실행 가능한 코드 스켈레톤 제공**

아래 코드를 `solution.py`에 복붙하고 조져봐. `for`문은 단어 배열(`strs`)을 순회하는 딱 한 번만 써야 한다.

```python
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 빈 리스트를 기본값으로 갖는 defaultdict 생성
        
        # 2. strs를 for문으로 하나씩 돌면서:
        #    - 단어를 알파벳 순으로 정렬해서 Key로 만듦 ("".join(sorted(...)))
        #    - 딕셔너리의 해당 Key에 원래 단어를 append
        
        # 3. 딕셔너리의 value들만 리스트로 묶어서 반환 (dict.values() 활용)
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    print("Test 1:", sol.groupAnagrams(strs1))
    # 예상 출력: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (순서는 달라도 됨)

    # Test Case 2
    strs2 = [""]
    print("Test 2:", sol.groupAnagrams(strs2))
    # 예상 출력: [[""]]

    # Test Case 3
    strs3 = ["a"]
    print("Test 3:", sol.groupAnagrams(strs3))
    # 예상 출력: [["a"]]

```

이번 건 R의 데이터프레임 집계(`aggregate`나 `group_by`) 감각을 파이썬 딕셔너리로 옮기는 훈련이야. 코드 다 짜면 가져와, 리뷰 들어간다!







<br>
<br>
<br>
<br>
<br>










오, 속도 봐라! 로직 자체는 흠잡을 데 없이 완벽해. 통계에서 범주형 변수(Factor) 묶어서 `group_by` 치던 짬바가 파이썬에서도 그대로 빛을 발하네. 핵심 아이디어인 '단어를 정렬해서 고유 Key로 쓴다'를 `defaultdict`에 아주 스무스하게 박아 넣었어.

하지만! 파이썬 PT 쌤 관점에서 보면 **"면접관이 보면 바로 미간 찌푸릴 치명적인 코딩 습관"**이 하나 숨어있어. 작동은 하지만 현업에서 쓰면 사수한테 등짝 맞는 코드랄까? 자, 바로 오답노트 들어간다. 저장해!

---

### 📄 `note.md` (오답노트 및 코드 리뷰)

#### 📝 1. 내 코드의 잘한 점과 아쉬운 점

* **👍 잘한 점:**
* `collections.defaultdict(list)`를 정확히 이해하고 사용해서, `if key in dict:` 같은 불필요한 조건문을 날려버림.
* `"".join(sorted(...))`로 애너그램의 고유 Key를 만들어내는 로직을 완벽하게 구현함.


* **🤦 아쉬운 점 (초보 티 벗기):**
1. **🚨 예약어(Built-in) 덮어쓰기 (가장 심각함):** `for str in strs:` 여기서 `str`은 파이썬에 원래 있는 내장 함수/타입(`str()`) 이름이야. 이걸 변수명으로 써버리면, 저 `for`문 아래에서는 파이썬 고유의 `str` 기능을 잃어버리게 돼. 실무에서 이렇게 짜면 예기치 못한 버그 터져서 난리 난다. `word`, `s`, `text` 같은 다른 이름으로 바꿔야 해.
2. **리턴 타입 불일치:**
`key_dict.values()`를 하면 리스트가 나오는 게 아니라 `dict_values([...])`라는 파이썬 특유의 뷰(View) 객체가 나와. LeetCode 채점기는 똑똑해서 대충 리스트로 찰떡같이 알아먹고 패스시켜주지만, 함수 정의부(`-> List[List[str]]`)에 맞추려면 명시적으로 `list(key_dict.values())`라고 감싸서 리스트로 형변환을 해주는 게 찐 파이써닉한 태도야.



#### 🎯 2. 오늘 부술 for문 (Big-O 견적 & 최적화)

형님이 짠 코드가 왜 빠른지 수치로 다시 확인하자.

* 단어 개수가 $N$개, 단어 최대 길이가 $K$라고 칠 때.
* 무식하게 일일이 비교하는 이중 `for`문: $O(N^2 \times K)$ $\rightarrow$ $10^8 \times 100 = 10^{10}$ (터짐)
* **형님이 짠 해시 맵 + 정렬 코드:** 단어 하나 정렬하는 데 $O(K \log K)$, 이걸 $N$번 반복하니까 전체 시간 복잡도는 **$O(N \cdot K \log K)$**로 끝남. $N$이 $10^4$라도 충분히 1초 안에 돌아가는 아주 훌륭한 최적화야!

#### ✨ 3. Pythonic & Pro 찐최종 코드

위 피드백을 반영해서 불필요한 변수 할당을 줄이고 깔끔하게 다듬은 코드다.

```python
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        # str 대신 word를 변수명으로 사용 (예약어 보호)
        for word in strs:
            # 정렬한 결과를 key로 삼아 딕셔너리에 추가
            anagrams["".join(sorted(word))].append(word)

        # dict_values 객체를 깔끔하게 list로 감싸서 리턴
        return list(anagrams.values())

```

---

자, 이렇게 해서 STEP 1의 5번 문제도 격파 완료! 예약어(`str`, `list`, `dict`, `int` 등)를 변수명으로 쓰지 않는 것만 명심하면 완벽해.

이제 **STEP 1의 6번 문제: 두 수의 합 (LeetCode 1)** 차례다. 코테계의 근본 중의 근본, 바이블 같은 문제지. 이것도 `for`문 두 개로 풀면 하수 소리 듣는 문제인데, 딕셔너리(해시)의 진가를 한 번 더 보여줄 준비 됐냐? 바로 다음 문제 던져줄까?