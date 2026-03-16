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
                dfs(index + 1, path + letter)
                # 힌트: dfs(?, ?) 형태가 될 거야.
        

        # 여기서 함수가 시작 됨 #
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