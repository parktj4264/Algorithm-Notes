import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [] # K명만 들어갈 VIP 대기실 (Min-Heap)
        
        for num in nums:
            # 1. 일단 현재 숫자(num)를 대기실(hq)에 밀어 넣기 (heappush 사용)
            heapq.heappush(hq, num)
            
            # 2. 만약 대기실 인원(len)이 K명을 초과했다면?
            # 제일 만만한 놈(최솟값)을 쫓아내기! (heappop 사용)
            if len(hq) > k: 
                heapq.heappop(hq)
            
        # 3. 배열을 다 돌고 나면, 대기실(hq)에는 가장 큰 K명만 남고,
        # 그중 가장 작은 값(문지기)이 hq[0]에 위치하게 됨! 그 값을 리턴!
        return hq[0]


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print("TC 1:", sol.findKthLargest(nums1, k1)) # 예상 결과: 5
    
    # Test Case 2 (중복 데이터 포함)
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print("TC 2:", sol.findKthLargest(nums2, k2)) # 예상 결과: 4