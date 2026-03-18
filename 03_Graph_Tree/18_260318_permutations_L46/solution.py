from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # dfs 함수 설계: 
        # path는 현재까지 선택한 숫자들의 리스트
        def dfs(path: List[int]):
            # 1. 종료 조건: path의 길이가 nums의 길이와 같다면 result에 추가
            if len(path) == len(nums):
                result.append(path[:])
                return 
            
            # 2. nums를 순회하면서 아직 path에 없는 숫자를 찾아 추가하고 가지치기(재귀)
            # 넣고 -> 재귀 호출 -> 빼기(Backtracking)
            for num in nums:
                if num not in path: 
                    path.append(num)
                    dfs(path)
                    path.pop()
            
        dfs([])
        return result
    


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 일반적인 3개짜리 배열
    print("TC 1:", sol.permute([1, 2, 3]))
    # 예상 결과: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    # Test Case 2: 2개짜리 배열
    print("TC 2:", sol.permute([0, 1]))
    # 예상 결과: [[0, 1], [1, 0]]
    
    # Test Case 3: 극단값 (1개짜리 배열)
    print("TC 3:", sol.permute([1]))
    # 예상 결과: [[1]]
    
    # Test Case 4: 음수와 양수가 섞인 배열
    print("TC 4:", sol.permute([-1, 0, 1]))