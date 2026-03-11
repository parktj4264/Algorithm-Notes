from typing import List

class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        
        # 여기에 로직을 구현해봐!
        # answer 배열 초기화와 stack 활용이 핵심이야.

        answer = [0] * len(temperatures)
        stack = []

        for i, tem in enumerate(temperatures):

            while( stack and (tem > temperatures[stack[-1]]) ):
                # 계속 덮어쓰기의도 (..?)
                idx = stack.pop()
                answer[idx] = i - idx

            stack.append(i)

        return answer

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 기본 케이스 (문제 예시)
    print("TC 1:", sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Test Case 2: 계속 추워지기만 하는 경우 (Stack에 쌓이기만 함)
    print("TC 2:", sol.dailyTemperatures([80, 70, 60, 50]))
    # Expected: [0, 0, 0, 0]
    
    # Test Case 3: 계속 더워지기만 하는 경우 (넣자마자 Pop 됨)
    print("TC 3:", sol.dailyTemperatures([50, 60, 70, 80]))
    # Expected: [1, 1, 1, 0]
    
    # Test Case 4: 동일한 온도만 반복되는 경우
    print("TC 4:", sol.dailyTemperatures([70, 70, 70, 70]))
    # Expected: [0, 0, 0, 0]