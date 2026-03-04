from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: # 빈 배열 예외 처리
            return 0

        # 1. 투 포인터 초기화
        left = 0
        right = len(height) - 1
        
        # 2. 양쪽 최대 벽 높이 초기화
        left_max = height[left]
        right_max = height[right]
        
        volume = 0 # 정답 (총 물의 양)

        # 3. 투 포인터 교차 전까지 반복
        while left < right:
            
            # 4. 왼쪽 벽이 더 낮거나 같을 때 (왼쪽 포인터 이동)
            if left_max <= right_max:
                # 4-1. 현재 위치에 고일 물 계산해서 volume에 더하기
                volume += left_max - height[left]
                
                # 4-2. 포인터 이동
                left += 1
                
                # 4-3. left_max 갱신
                left_max = max(left_max, height[left])


            # 5. 오른쪽 벽이 더 낮을 때 (오른쪽 포인터 이동)
            else:
                # 5-1. 현재 위치에 고일 물 계산해서 volume에 더하기
                volume += right_max - height[right]
                
                # 5-2. 포인터 이동
                right -= 1
                
                # 5-3. right_max 갱신
                right_max = max(right_max, height[right])
                
                
        return volume

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height1) == 6)  # True 나와야 함
    
    # Test Case 2
    height2 = [4,2,0,3,2,5]
    print(sol.trap(height2) == 9)  # True 나와야 함