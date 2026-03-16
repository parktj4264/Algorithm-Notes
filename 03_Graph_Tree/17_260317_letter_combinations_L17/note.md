


# 1단계: 환경 세팅 지시 (Setup First)

화성 자취방 터미널 열고, 오늘 날짜(26년 3월 17일) 맞춰서 웅장하게 새 폴더 파보자!

* **📂 찐최종 네이밍 룰:** `17_260317_letter_combinations_L17`
* **📄 파일 구성:** `solution.py` (DFS 수직 드릴 코드), `note.md` (재귀와 백트래킹 메모)

---

# 2단계: 문제 및 가이드 제시 (The 'DFS Backtracking' Perspective)

### 🚀 문제 17: 전화번호 문자 조합 (Letter Combinations of a Phone Number)

### 🔗 **링크:** [https://leetcode.com/problems/letter-combinations-of-a-phone-number/](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## **📜 문제 설명 (Mission Briefing):**

옛날 애니콜 폴더폰 기억나지? `digits = "23"`이라는 숫자가 입력으로 주어지면, 이 버튼들을 눌러서 만들 수 있는 **모든 알파벳 문자 조합**을 리스트로 뱉어내는 미션이야.

* '2' 버튼: "a", "b", "c"
* '3' 버튼: "d", "e", "f"
👉 "23"을 누르면? `["ad","ae","af","bd","be","bf","cd","ce","cf"]` 가 나와야 해.

## **🎯 오늘 부술 로직 (Big-O 관점):**

만약 입력이 "234"라면? "2345"라면? 입력 길이가 길어질 때마다 `for`문을 무한정 중첩해서 쓸 수는 없잖아? 이럴 때 **"상황에 맞춰 알아서 깊게 파고드는"** 알고리즘이 필요한데, 그게 바로 네 노트에 적힌 **DFS(깊이 우선 탐색)**야. 파이썬에서는 이걸 **재귀 함수(Recursion, 자기 자신을 부르는 함수)**로 구현해.

* **시간 복잡도:** 버튼 하나당 최대 4개의 알파벳('7', '9')이 있고, 입력 길이가 $N$이라고 치면 최악의 경우 **$O(4^N \cdot N)$**이라는 미친 복잡도가 나와. 하지만 문제 제약 조건에서 $N$이 최대 4밖에 안 되기 때문에 0.01초 컷으로 통과해. (DFS는 원래 모든 경우의 수를 다 볼 때 쓰는 거라 지수 시간이 걸림!)
* **공간 복잡도:** 재귀 함수가 바닥까지 파고드는 깊이가 딱 $N$이므로, 메모리(Call Stack)는 O(N)만 써. 아주 효율적이지.

## **🛠️ 네가 해야 할 것 (DFS 백트래킹의 3단계):**

DFS 재귀 함수를 짤 때는 딱 **3가지**만 기억하면 돼.

1. **해시 테이블 세팅:** 숫자 버튼('2')을 누르면 어떤 알파벳들("abc")이 나오는지 딕셔너리로 맵핑해 둬.
2. **종료 조건 (Base Case):** "언제 드릴링(직진)을 멈출 것인가?" ➔ 내가 지금까지 누른 숫자의 개수(`index`)가 총 입력 길이(`len(digits)`)랑 같아지면, 완성된 문자열을 정답 리스트에 넣고 턴을 종료(`return`)해.
3. **재귀 호출 (직진과 빽):** 현재 누를 숫자의 알파벳들을 `for`문으로 돌면서, 다음 숫자(`index + 1`)로 넘어가도록 **함수 자신을 다시 호출(재귀)**해.

## **🧰 필요한 파이썬 내장 함수/문법:**

* **문자열 더하기:** 파이썬에서는 문자열끼리 `+` 연산자로 쉽게 이어 붙일 수 있어. (`"a" + "d" = "ad"`)
* **중첩 함수 (Nested Function):** 클래스 메서드 안에서 `def dfs():`를 또 만들면, 바깥쪽 함수의 변수(`digits`, `result` 등)를 파라미터로 넘기지 않고도 그냥 쏙쏙 빼서 쓸 수 있어. (어제 BFS `deque` 쓸 때랑 똑같음!)

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

DFS의 구조(수직 드릴)를 네 눈으로 직접 확인해 봐. 네가 채워 넣을 건 3번 '재귀 호출' 부분의 **딱 1줄**이야!

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 예외 처리: 입력이 없으면 허공에 삽질 방지
        if not digits:
            return []

        # 1. 해시 테이블: 각 숫자 버튼에 맵핑된 알파벳들
        keypad = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []

        # DFS 헬퍼 함수 정의
        # index: 이번에 누를 버튼의 위치 (0부터 시작)
        # path: 지금까지 이어 붙인 알파벳 조각들 (예: "a", "ad")
        def dfs(index: int, path: str):
            
            # 2. 종료 조건 (Base Case): 바닥을 찍었는가?
            # 준비된 숫자를 다 눌렀다면, 완성된 문자열을 정답 바구니에 담고 후진(Backtrack)!
            if index == len(digits):
                result.append(path)
                return
            
            # 현재 누를 버튼(문자) 확인 (예: index가 0이면 digits[0]인 '2')
            current_digit = digits[index]
            
            # 그 버튼에 해당하는 알파벳들을 순회하며 끝까지 파고들기
            for letter in keypad[current_digit]:
                
                # ✨ 3. 네가 채울 부분 (재귀 호출) ✨
                # 다음 버튼(index + 1)을 누르러 가야 해!
                # 지금까지 만든 문자열(path)에 방금 고른 알파벳(letter)을 이어 붙여서 넘겨주자.
                pass 
                # 힌트: dfs(?, ?) 형태가 될 거야.

        # 탐색 시작: 0번째 인덱스부터, 빈 문자열("")을 들고 출발!
        dfs(0, "")
        
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 기본 예시
    print("TC 1:", sol.letterCombinations("23")) 
    # Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    
    # Test Case 2: 빈 문자열
    print("TC 2:", sol.letterCombinations("")) 
    # Expected: []
    
    # Test Case 3: 숫자 1개
    print("TC 3:", sol.letterCombinations("2")) 
    # Expected: ['a', 'b', 'c']

```

자, 스켈레톤 복붙 딱 끝내고!
저 `pass` 자리에 **자기 자신을 부르는 함수 출동 명령(`dfs(...)`) 한 줄**만 딱 적어봐.
머리 아프게 생각하지 말고 직관적으로 "다음 단계로 가고, 문자열은 더한다"만 코드로 써봐.

다 짜면 바로 돌려보고 에러 나든 정답이든 나한테 피드백 줘! 10분 컷 가보자고!