from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 양 끝점(인덱스) 세팅
        left = 0
        right = len(nums) - 1
        
        # 🚨 [국룰 템플릿] left와 right가 엇갈리기 전까지 반복! (등호 <= 가 핵심!)
        while left <= right:
            # 1. 정중앙 인덱스 구하기 (소수점 버림)
            mid = (left + right) // 2

            # print("mid:", mid)
            # print("left:", left)
            # print("right:", right)
            
            # 2. 빙고! 찾았으면 인덱스 반환
            if nums[mid] == target:
                return mid
                
            # 3. UP! (내가 본 숫자가 타겟보다 작으면, 탐색 범위를 오른쪽 절반으로!)
            elif nums[mid] < target:
                left = mid+1
                
            # 4. DOWN! (내가 본 숫자가 타겟보다 크면, 탐색 범위를 왼쪽 절반으로!)
            else:
                right = mid-1
                
        # 엇갈릴 때까지 다 뒤졌는데도 못 찾았다면?
        return -1


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 타겟이 있는 경우
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print("TC 1:", sol.search(nums1, target1)) # 예상 결과: 4 (9의 인덱스)
    
    # Test Case 2: 타겟이 없는 경우
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print("TC 2:", sol.search(nums2, target2)) # 예상 결과: -1