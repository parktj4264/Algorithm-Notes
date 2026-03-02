자, PT 시작하자. 주말 잘 쉬었냐?
오늘 날짜 26년 2월 23일 기준, 드디어 4번째 문제 들어간다.

현재 진도: **STEP 1 (워밍업) ➔ [진행 중: 4/38]**

이번 문제는 형님이 R에서 텍스트 마이닝 패키지(`tm`이나 `tidytext`) 써서 **워드 클라우드(Word Cloud)** 만들 때 지겹게 하던 짓거리야. 그걸 파이썬으로 얼마나 우아하게 짤 수 있는지 보는 거다. 바로 간다!

### 🚀 문제 819: Most Common Word (가장 흔한 단어)

🔗 **링크:** [https://leetcode.com/problems/most-common-word/](https://leetcode.com/problems/most-common-word/)

---

**1단계: 환경 세팅 지시 (Setup First)**

터미널 켜고 우리가 정한 '찐찐찐 최종 네이밍 룰'에 맞춰서 폴더 파라.

* 📂 **폴더:** `04_260223_most_common_word_L819`
* 📄 **파일:** `solution.py`, `note.md`

만들었으면 `solution.py` 열어.

---

**2단계: 작전 및 가이드**

### 🎯 (1) 너가 해야 할 것 (Mission Objective)

주어진 단락(`paragraph`)에서 **금지된 단어(`banned`)를 제외하고**, 가장 자주 등장하는 단어를 찾아라.

1. **정규화 (Normalization):** 대소문자 구분 안 함. 무조건 소문자로 싹 다 바꿔라.
2. **클렌징 (Cleansing):** 구두점(`!`, `?`, `'`, `,`, `;`, `.`) 무시. 전부 공백으로 날려버리고 단어만 남겨라.
3. **불용어 처리 (Stopwords Filtering):** 쪼갠 단어들 중에서 `banned` 리스트에 있는 놈들은 빼고 카운트해라.
4. **빈도수 계산 (Term Frequency):** 살아남은 단어 중 가장 많이 나온 놈 1개를 리턴해라.

### 🛠️ (2) 필요한 함수 (Required Tools)

R의 `table()` 함수나 `dplyr::count()` 역할을 파이썬에선 이놈들이 한다.

* **`re.sub()`:** 정규식으로 불순물 날리기 (1일 차에 해봤지?)
* **리스트 컴프리헨션 (List Comprehension):** 파이썬의 꽃. `for`문과 `if`문을 한 줄로 압축해서 리스트를 필터링하는 개사기 문법.
* **`collections.Counter`:** 데이터 사이언티스트라면 무조건 외워야 하는 파이썬 딕셔너리의 상위 호환 모듈. 빈도수 세기의 신(神)이다.

### 📖 (3) 사용법 (Syntax & Examples)

**1. 문자열 클렌징 (정규식 꿀팁)**
1일 차에는 `[^a-z0-9]` 썼지? 이번엔 단어(Word) 문자가 아닌 걸 날릴 때 더 짧은 정규식이 있어. `\w`는 단어 문자(알파벳+숫자+_)를 의미해. `[^\w]` 라고 쓰면 **"단어 문자가 아닌 것(구두점 등)을 전부 매칭해라"**라는 뜻이야.

```python
import re
text = "Bob hit a ball, the hit BALL flew."
# 단어 문자가 아닌 것([^\w])을 전부 공백(' ')으로 바꿔라!
clean_text = re.sub(r'[^\w]', ' ', text.lower()) 
# 결과: "bob hit a ball  the hit ball flew "

```

**2. 리스트 컴프리헨션 (필터링)**
R에서 `subset(df, !word %in% banned)` 하던 걸 파이썬에선 이렇게 해.

```python
words = ["bob", "hit", "a", "ball", "hit"]
banned = ["hit"]

# words 안의 단어(w)들을 꺼내는데, banned에 없는(not in) 놈들만 리스트로 묶어라!
filtered = [w for w in words if w not in banned]
# 결과: ['bob', 'a', 'ball']

```

**3. `Counter` (빈도수 추출기)**
파이썬에서 개수 셀 때는 묻지도 따지지도 말고 이거 써라.

```python
from collections import Counter
filtered = ['bob', 'ball', 'ball']

counts = Counter(filtered)
# 결과: Counter({'ball': 2, 'bob': 1})

# 가장 흔한 단어 1개 뽑기
top_1 = counts.most_common(1)
# 결과: [('ball', 2)]  <-- 리스트 안에 튜플 형태로 나옴!

print(top_1[0][0]) # 'ball' 추출 완료

```

---

**3단계: 실행 가능한 코드 스켈레톤**

자, 재료는 다 줬다. 조립은 형님이 해라! 아래 코드 복사해서 `solution.py`에 넣고 시작.

```python
import re
from typing import List
from collections import Counter

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    """
    :param paragraph: 분석할 텍스트 단락
    :param banned: 제외할 금지어 리스트
    :return: 금지어를 제외하고 가장 많이 등장한 단어
    """
    
    # 💡 쌤의 조립 설명서:
    # 1. 정규식(re.sub)으로 paragraph 안의 구두점을 공백으로 바꾸고 소문자(.lower())로 만든다.
    # 2. .split() 으로 쪼개서 단어 리스트를 만든다.
    # 3. 리스트 컴프리헨션을 써서 banned에 없는 단어만 남긴 새로운 리스트를 만든다.
    # 4. Counter를 써서 1등 단어를 뽑아 리턴한다.
    
    pass

if __name__ == "__main__":
    # 예제 테스트 케이스 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(f"Test Input 1: '{paragraph1}' | banned: {banned1}")
    print(f"Result 1: {mostCommonWord(paragraph1, banned1)}") 
    # 정답: "ball"
    
    print("-" * 40)
    
    # 예제 테스트 케이스 2
    paragraph2 = "a."
    banned2 = []
    print(f"Test Input 2: '{paragraph2}' | banned: {banned2}")
    print(f"Result 2: {mostCommonWord(paragraph2, banned2)}") 
    # 정답: "a"

```

**[Next Step]**
자, 데이터 전처리와 빈도 분석 파이프라인이다. `solution.py` 채우고 예제 1, 2번 다 통과하면 코드 복사해서 올려!
