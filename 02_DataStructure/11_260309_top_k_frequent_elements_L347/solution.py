from typing import List
import collections # Counter를 쓰고 싶다면 활용해!
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums).most_common(k)

        return [x[0] for x in counts]
        


    def topKFrequent_study(self, nums: List[int], k: int) -> List[int]:  

        counts_dict = {}

        for n in nums:
            if n in counts_dict: 
                counts_dict[n] += 1
            else: 
                counts_dict[n] = 1

        sorted_counts_dict = sorted(counts_dict.items(), key = lambda x: x[1], reverse = True)


        return [x[0] for x in sorted_counts_dict[:k]]



if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 가장 기본적인 케이스
    print("Test 1 (Normal):", sol.topKFrequent([1,1,1,2,2,3], 2) == [1, 2])
    
    # Test 2: 원소가 1개일 때
    print("Test 2 (Single Element):", sol.topKFrequent([1], 1) == [1])
    
    # Test 3: 음수가 포함되어 있을 때 (음수도 정상적으로 카운트 되어야 함)
    print("Test 3 (Negative Numbers):", sol.topKFrequent([-1,-1,2,2,2,3], 2) == [2, -1])
    
    # Test 4: k가 전체 고유 숫자의 개수와 같을 때 (순서는 상관없으므로 set으로 비교)
    result4 = sol.topKFrequent([4,4,4,5,5,6], 3)
    print("Test 4 (All Unique Elements):", set(result4) == {4, 5, 6})