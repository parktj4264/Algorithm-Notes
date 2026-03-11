오늘 진도는 **[STEP 2 (자료구조 1 - 속도)]** 의 12번 문제야. 삼성 메모리에서 데이터 깎느라 고생했다. 퇴근하고 피곤하겠지만 딱 30분만 빡집중해서 뇌 근육 좀 찢어보자고.

오늘은 컴퓨터 공학의 근본인 **스택(Stack)** 을 다룰 거다. 최신 관측치가 제일 먼저 튀어나오는 LIFO(Last In, First Out) 구조지.

---

### # 1단계: 환경 세팅 지시 (Setup First)

IDE 켜고, 아래 이름으로 폴더랑 파일부터 만들어라.

* **📂 찐최종 네이밍 룰:** `12_260310_valid_parentheses_L20`
* **📄 파일 구성:**
* `solution.py` 
* `note.md`



---

### # 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 20: 유효한 괄호 (Valid Parentheses)

### 🔗 **링크:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## **📜 문제 설명 (Mission Briefing):**

문자열 `s`가 주어질 건데, 이 안에는 딱 6가지 괄호 `'(', ')', '{', '}', '[', ']'` 만 들어있어. 이 문자열이 '수학적으로/문법적으로 유효한' 괄호 구조인지 판별해서 `True` / `False`를 뱉으면 돼.

규칙은 간단해.

1. 여는 괄호는 같은 타입의 닫는 괄호로만 닫혀야 한다.
2. 여는 괄호는 올바른 순서대로 닫혀야 한다. (즉, 안쪽 괄호가 먼저 닫혀야 바깥쪽 괄호가 닫힐 수 있음)

**예시 보면서 감 잡아:**

* `"()"` ➔ `True` (깔끔)
* `"()[]{}"` ➔ `True` (끼리끼리 잘 놈)
* `"(]"` ➔ `False` (모양 안 맞음)
* `"([)]"` ➔ `False` (순서 꼬임. `[`가 열렸으면 `]`가 먼저 닫혀야지 중간에 `)`가 왜 껴?)
* `"{[]}"` ➔ `True` (마치 양파껍질처럼 안쪽 `[]`부터 예쁘게 닫히고 바깥쪽 `{}` 닫힘)

## **🎯 오늘 부술 for문 (Big-O 관점):**

문제에서 주어지는 문자열 `s`의 최대 길이는 $10^4$ 야.
무지성으로 문자열 안에서 `"()"`, `"{}"`, `"[]"` 짝을 찾아서 파이썬의 `.replace('()', '')` 같은 걸로 빈 문자열로 지우는 짓을 문자열이 텅 빌 때까지 반복한다고 쳐보자. 최악의 경우 문자열을 계속 처음부터 끝까지 훑어야 하니까 시간 복잡도가 $O(N^2)$이 찍혀버려. 길이가 $10^4$면 연산량이 $10^8$인데, 파이썬에선 아슬아슬하거나 Time Out 뜰 수 있어.

그래서 오늘은 **Stack 메모리를 제물로 바쳐서(공간 복잡도 $O(N)$)**, 문자열을 **딱 한 번만 순회(시간 복잡도 $O(N)$)** 하는 기적의 교환 연성을 할 거다.

## **🛠️ 네가 해야 할 것:**

시계열 데이터 한 틱씩 읽어들이듯이 문자열을 앞에서부터 하나씩 순회해.
여는 괄호면 어딘가에 차곡차곡 쌓아둬 (Push). 그러다가 닫는 괄호가 등장하면? 가장 최근에 쌓아둔 놈(Pop)이랑 방금 만난 닫는 괄호가 '짝꿍'인지 확인해라.
짝이 안 맞으면? 바로 `False` 뱉고 컷.
루프 다 돌았는데 쌓아둔 창고에 괄호가 남아있으면? 그것도 닫히지 않은 거니까 `False` 컷.

## **🧰 필요한 파이썬 내장 함수/문법:**

* **리스트를 스택처럼 쓰기:** 파이썬은 Stack 자료구조가 따로 없고 그냥 `list`를 쓰면 된다.
```python
stack = []
stack.append(1)  # O(1)로 맨 뒤에 추가 (Push)
top = stack.pop() # O(1)로 맨 뒤 요소 빼서 반환 (Pop)

```


* **해시 맵 (Dictionary):** 괄호 짝꿍 매핑용으로 써라. R의 Named Vector나 List랑 비슷한데 훨씬 빠르지.
닫는 괄호를 Key로, 여는 괄호를 Value로 두면 탐색할 때 찢어지게 빠르다. (해시 테이블 조회는 $O(1)$)
```python
mapping = {")": "(", "}": "{", "]": "["}
if char in mapping:  # char가 닫는 괄호인지 O(1)로 확인
    # 여기서 짝꿍 검사

```



---

### # 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

아래 코드 복사해서 `solution.py`에 붙여넣고 빈칸 채워서 로직 완성해라. 엣지 케이스도 다 넣어놨으니까 실행시켜서 전부 `True` 뜨는지 확인하고.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # 여기에 네가 짠 코드를 들이부어라.
        # 시간 복잡도 O(N), 공간 복잡도 O(N) 맞춰라.
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # Test Cases
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("[", False),      # 엣지 케이스: 여는 괄호만 있을 때
        ("]", False),      # 엣지 케이스: 닫는 괄호만 있을 때
        ("((", False)      # 엣지 케이스: 여는 괄호만 여러 개 남을 때
    ]
    
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = sol.isValid(s)
        status = "✅ PASS" if result == expected else f"❌ FAIL (Expected: {expected}, Got: {result})"
        print(f"Test {idx} ['{s}']: {status}")

```











<br>
<br>
<br>
<br>
<br>
<br>


---


# 📝 [오답 및 최적화 노트] 12_260310_valid_parentheses_L20

## 1. 💡 나의 초기 접근 (Working, but Not Pythonic)
- **핵심 아이디어:** `for`문으로 문자열을 한 번만 순회하며, 여는 괄호는 `stack`에 넣고 닫는 괄호를 만나면 짝을 맞춰본다.
- **결과:** 정답은 맞췄고, 시간 복잡도도 $O(N)$으로 잘 방어함. 
- **문제점:** R에서 `length() == 0`으로 검사하던 버릇, 명제를 조건문으로 한 번 더 감싸는 버릇 때문에 들여쓰기(Depth)가 깊어지고 코드가 지저분해짐.

## 2. 🔨 PT쌤의 팩트 폭격 & 최적화 포인트

### ① 빈 리스트 검사는 무조건 `not` (Truthy/Falsy)
파이썬은 빈 리스트 `[]`, 빈 문자열 `""`, `0`, `None` 등을 조건문에서 자동으로 `False`로 취급한다.
- ❌ 하수: `if len(stack) == 0:` (R 스타일)
- ✅ 고수: `if not stack:` (Pythonic)

### ② 불필요한 `pass`와 `else` 쳐내기 (Early Return)
조건이 맞을 때 통과(`pass`)시키고 아닐 때 `False`를 뱉는 구조는 코드를 무겁게 만든다. **방어적 프로그래밍** 관점에서 "조건에 안 맞으면 바로 `Return`으로 컷" 해버려야 들여쓰기가 줄어든다.
- ❌ 하수: 짝이 맞으면 `pass`, 아니면 `return False`
- ✅ 고수: 짝이 안 맞으면 바로 `return False`

### ③ 불리언(Boolean) 명제의 직접 반환
명제 자체가 참/거짓인데 굳이 `if/else`를 태울 필요가 없다. 스택이 비었으면 `True`, 남아있으면 `False`를 뱉어야 하는 상황.
- ❌ 하수: `if not stack: return True else: return False`
- ✅ 고수: `return not stack`

## 3. ✨ 찐최종 찢어버린 코드
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char not in mapping: 
                # 1. 여는 괄호면 무지성 Push
                stack.append(char)
            else: 
                # 2. 닫는 괄호일 때: 스택이 비었거나 짝이 안 맞으면 즉시 컷
                if not stack or mapping[char] != stack.pop():
                    return False
        
        # 3. 순회 끝난 후 스택이 예쁘게 비었으면 True, 찌꺼기 남았으면 False
        return not stack

```

## 4. 📊 Big-O 복기 (시간/공간 복잡도 Trade-off)

* **시간 복잡도:** $O(N)$
* 무지성으로 `.replace('()', '')`를 반복했다면 $O(N^2)$이 나왔을 것.
* 하지만 `for char in s:`로 문자열을 딱 한 번만 순회 (1 Pass). 딕셔너리 조회의 해시 테이블 탐색 속도는 $O(1)$, 리스트의 `append()`와 `pop()`도 $O(1)$이므로 전체 시간 복잡도는 $O(N)$으로 방어 성공.


* **공간 복잡도:** $O(N)$
* 최악의 경우(예: `"(((((("`) 모든 문자가 스택에 쌓이므로 $O(N)$의 추가 메모리를 사용함. **메모리를 제물로 바쳐 속도를 연성한 전형적인 Trade-off.**



## 5. 🧠 오늘의 통계/데이터 비유

* **Stack과 해시맵의 콜라보:** 스택은 시계열 데이터에서 가장 최근에 관측된 노이즈를 먼저 처리(LIFO)하기 위한 임시 버퍼 공간과 같다. 해시맵(`mapping`)은 괄호의 짝을 찾기 위한 조인(Join) 키 역할을 수행하여 탐색 비용을 $O(1)$로 압살했다.
