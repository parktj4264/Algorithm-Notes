
---

# **1단계: 환경 세팅 지시 (Setup First)**

오늘 날짜(260302) 맞춰서 각 잡고 폴더 하나 파자.

* **📂 찐최종 네이밍 룰:** `04_260302_most_common_word_L819`
* **📄 파일 구성:** 안에 `solution.py`랑 `note.md` (아이디어 메모용) 딱 두 개 만들어.

---

# **2단계: 문제 및 가이드 제시**

### 🚀 문제 819: 가장 흔한 단어 (Most Common Word)

### 🔗 **링크:** [https://leetcode.com/problems/most-common-word/](https://leetcode.com/problems/most-common-word/)

## **📜 문제 설명 (Mission Briefing):**
금지된 단어(Banned Words)를 제외하고 가장 자주 등장하는 단어를 출력하는 거다.
* **Input:** `paragraph` = "Bob hit a ball, the hit BALL flew far after it was hit." (문자열, 길이 1000 이하)
* `banned` = ["hit"] (리스트)
* **Output:** "ball"

## **핵심 규칙:** 1. 대소문자 구분 안 함 (전부 소문자로 퉁쳐야 함).
2. 구두점(마침표, 쉼표 등) 무시. 오직 영문자만 단어로 취급.
3. 금지된 단어는 정답이 될 수 없음.
4. 정답은 유일하게 하나만 존재함.


## **🎯 오늘 부술 for문 (Big-O 견적):**
* **입력 크기 역산:** 텍스트 길이 $N$이 최대 1000, `banned` 리스트 길이 $M$이 최대 100.
* R에서 하던 습관대로 "문자열 하나씩 돌면서 구두점인지 확인하는 `for`문" $\rightarrow$ "단어 리스트 만들어서 `banned`에 있는지 하나씩 찾는 이중 `for`문" $\rightarrow$ "개수 센다고 또 `for`문" 쓰면 $O(N \times M)$ 혹은 그 이상으로 코드가 엄청 지저분해지고 느려져.
* **해결책:** 파이썬은 문자열 처리의 치트키인 **정규표현식(Regex)**과, R의 `table()` 함수 뺨치는 **해시 맵(Hash Map) 기반의 카운터**를 쓸 거다. 이중, 삼중 `for`문 다 박살 내고 $O(N + M)$ 수준으로 타협 본다.  통계에서 키(Key)에 값(Value)을 1:1 매핑하는 원리랑 똑같아.


## **🛠️ 네가 해야 할 것 (Step-by-Step 설계):**
1. **데이터 클렌징 (Data Cleansing):** `paragraph` 문자열에서 정규표현식을 써서 단어 문자(알파벳)가 아닌 애들을 싹 다 공백으로 치환해라. 그리고 소문자로 싹 내려버려.
2. **토큰화 (Tokenization):** 공백 기준으로 문자열을 쪼개서 단어 리스트로 만들어.
3. **필터링 (Filtering):** 쪼갠 단어 리스트 중에서 `banned`에 없는 단어들만 남겨. (여기서 파이썬 특유의 '리스트 컴프리헨션'을 쓰면 코드가 한 줄로 예뻐진다.)
4. **카운팅 (Counting):** 남은 단어들의 빈도를 세고, 최빈값을 뽑아내.


## **🧰 필요한 파이썬 내장 함수/문법 (범용 사용법):**
* **정규표현식 치환 (`re.sub`):** 

```python
import re
# \w는 단어 문자, ^는 NOT을 의미. 즉 "단어 문자가 아닌 것"을 "공백"으로 바꿈.
clean_text = re.sub(r'[^\\w]', ' ', 'test123string!@#')
```


* **리스트 컴프리헨션 (List Comprehension):** R의 벡터화 연산처럼 파이썬에서 `for`문 속도를 끌어올리는 핵심 문법이야.

```python
numbers = [1, 2, 3, 4, 5]
# numbers에서 3보다 큰 것만 뽑아서 리스트 생성
filtered = [x for x in numbers if x > 3] 

```


* **빈도수 세기 (`collections.Counter`):**

```python
import collections
words = ['apple', 'banana', 'apple', 'orange']
counts = collections.Counter(words) # {'apple': 2, 'banana': 1, 'orange': 1}
most_common_1 = counts.most_common(1) # [('apple', 2)] (가장 흔한 거 1개 튜플로 리턴)
```





---

# **3단계: 실행 가능한 코드 스켈레톤 제공**

아래 코드를 `solution.py`에 복붙하고 `def mostCommonWord` 안쪽 논리만 형님 스스로 채워봐. `for`문 덕지덕지 붙여서 가져오면 C/Java 아재라고 놀릴 거니까 파이썬답게 짜보라고!

```python
import re
import collections
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. 정규표현식으로 구두점 날리고 소문자로 변경 후 리스트로 쪼개기
        
        # 2. banned에 없는 단어만 남기기 (리스트 컴프리헨션 활용)
        
        # 3. Counter 객체 써서 가장 흔한 단어 뽑아내기
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print("Test 1:", sol.mostCommonWord(paragraph1, banned1)) 
    # 예상 출력: "ball"

    # Test Case 2
    paragraph2 = "a."
    banned2 = []
    print("Test 2:", sol.mostCommonWord(paragraph2, banned2)) 
    # 예상 출력: "a"

```

자, 데이터 사이언티스트 형님의 텍스트 클렌징 솜씨 좀 볼까? 코드 짜보고 막히거나 고민되는 부분 있으면 바로 가져와. 답안 훔쳐볼 생각은 절대 말고! 다 짜면 코드 리뷰 들어간다. 시작해!




<br>
<br>
<br>
<br>
<br>



특히 조건문에 쓴 `&` 기호! R에서는 벡터 연산할 때 `&` 쓰지만, 파이썬에서 논리 연산자는 무조건 `and`야. `&`는 비트 연산자(Bitwise operator)라서 지금은 어찌어찌 돌아갔어도 나중에 치명적인 버그 터진다. 그리고 `split(" ")` 쓴 다음에 빈 문자열 지우려고 `len(word) > 0` 꾸역꾸역 넣은 것도 파이썬의 우아함을 해치는 짓이야.

가장 중요한 **Big-O 견적**에서도 아쉬운 부분이 있어. 자, 바로 `note.md` 파일에 들어갈 오답노트 겸 코드 리뷰 정리해 준다. 이거 그대로 복붙해서 저장해 둬.

---

### 📄 `note.md` (오답노트 및 코드 리뷰)

#### 📝 1. 내 코드의 잘한 점과 아쉬운 점

* **👍 잘한 점:** * 파이썬의 강력한 무기인 `collections.Counter`와 `re.sub`를 적절히 사용함.
* 리스트 컴프리헨션을 써서 데이터를 필터링하려는 시도 자체는 아주 훌륭함.


* **🤦 아쉬운 점 (R 냄새 빼기):**
1. **논리 연산자 오류:** `(word not in banned) & (len(word) > 0)`에서 `&` 대신 `and`를 써야 함.
2. **`split()`의 비밀:** `.split(" ")`처럼 띄어쓰기 하나를 명시하면 공백이 여러 개일 때 `""` 같은 빈 문자열이 리스트에 들어감. 그냥 `.split()`이라고 아무것도 안 넣고 쓰면, 파이썬이 알아서 연속된 공백, 탭, 엔터 등을 전부 무시하고 깔끔하게 단어만 쪼개줌. 그럼 `len(word) > 0` 같은 군더더기 조건이 필요 없어짐.
3. **변수 선언 낭비:** `clean_parag`, `clean_low_parag` 등 변수를 계속 새로 파는 건 메모리 낭비. 파이썬은 메서드 체이닝(Method Chaining)으로 한 줄에 쭉 이어서 쓰는 게 국룰임.



#### 🎯 2. 오늘 부술 for문 (Big-O 견적 & 최적화)

형님 코드에서 가장 위험한 부분이 바로 여기야.

```python
word not in banned

```

`banned`는 현재 **리스트(List)** 자료형이지? 길이가 $M$인 리스트에서 어떤 단어가 있는지 찾으려면 최악의 경우 리스트를 처음부터 끝까지 다 뒤져야 해 ($O(M)$). 이걸 문서의 단어 개수 $N$만큼 반복하면 전체 시간 복잡도가 $O(N \times M)$이 돼버려.

**🛠️ 해결책: 해시 테이블(Set)로 $O(1)$ 매핑**
통계에서 딕셔너리로 Key-Value 매핑하면 탐색 시간 0초에 수렴하는 거 알지? 파이썬의 `set` 자료형은 내부적으로 **해시 테이블(Hash Table)**로 구현되어 있어.
`banned` 리스트를 `set(banned)`로 한 번만 변환해 주면, `word not in set(banned)`를 할 때 단어를 찾는 시간이 **$O(1)$**로 확 줄어들어.
결국 전체 시간 복잡도를 $O(N \times M)$에서 **$O(N + M)$**으로 멱살 잡고 끌어내릴 수 있는 거지. 이게 바로 엔지니어링 퀄리티 차이야.

#### ✨ 3. Pythonic & Pro 찐최종 코드

위의 피드백을 전부 반영한, 면접관이 봤을 때 "오, 파이썬 좀 치는데?" 할 만한 코드야. 눈으로 비교해 봐.

```python
import re
import collections
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. banned 리스트를 Set으로 변환하여 탐색 속도를 O(1)로 단축 (해시 테이블)
        banned_set = set(banned)
        
        # 2. 정규식 변환 -> 소문자 변환 -> 쪼개기 (메서드 체이닝 & split() 자동 공백 제거)
        # [^\w] 대신 \W 도 "단어 문자가 아닌 것"을 의미하는 같은 표현임
        words = [
            word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
            if word not in banned_set
        ]
        
        # 3. Counter로 최빈값 추출
        return collections.Counter(words).most_common(1)[0][0]

```

---

어때, 코드가 훨씬 날씬하고 섹시해졌지? R에서 데이터프레임 파이프라인(`%>%`) 타듯이, 파이썬에서도 문자열은 `.lower().split()` 이렇게 체이닝으로 쭉쭉 뽑아내는 맛이 있어야 돼. 그리고 무엇보다 **조회(Lookup)할 땐 무조건 `set`이나 `dict`를 써서 $O(1)$로 만든다**는 거 절대 잊지 마라.

자, 4번 문제 깔끔하게 클리어했다!
내일은 **STEP 1의 5번 문제: 그룹 애너그램 (LeetCode 49)** 조질 차례야. 슬슬 딕셔너리(Hash Map) 다루는 법을 빡세게 굴려볼 텐데, 내일 이어서 갈까? 아니면 오늘 진도 여기까지 하고 쉴래? 선택해 형님!