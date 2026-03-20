from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        # start: 이번 탐색에서 시작할 숫자 (이전 숫자는 쳐다보지 않음)
        # path: 현재까지 뽑은 조합 리스트

        def dfs(start: int, path: List[int]):
            # 1. 종료 조건: path의 길이가 k와 같다면 정답에 추가 (값 복사 필수!)
            if len(path) == k: 
                result.append(path[:])
                return

            # 2. 백트래킹: start부터 n까지 반복
            # 넣고 -> 재귀 호출(다음 시작점 주의) -> 빼기
            for i in range(start, n+1):
                path.append(i)
                dfs(i+1, path)
                path.pop()
            
        dfs(1, []) # 1부터 시작, 빈 책상으로 출발!
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 기본 케이스 (4C2)
    print("TC 1:", sol.combine(4, 2))
    # 예상 결과: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    
    # Test Case 2: n과 k가 같은 경우 (3C3) - 엣지 케이스
    print("TC 2:", sol.combine(3, 3))
    # 예상 결과: [[1, 2, 3]]
    
    # Test Case 3: 최소값 (1C1)
    print("TC 3:", sol.combine(1, 1))
    # 예상 결과: [[1]]
    
    # Test Case 4: n은 크고 k는 작은 경우 (5C1)
    print("TC 4:", sol.combine(5, 1))
    # 예상 결과: [[1], [2], [3], [4], [5]]