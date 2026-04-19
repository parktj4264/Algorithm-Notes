from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels_set = set(jewels)

        ans = 0
        
        for s in stones:
            if s in jewels_set:
                ans += 1
        
        return ans
        

if __name__ == "__main__":
    sol = Solution()
    
    # 1. Normal Case (기본)
    print("Test 1 (Normal):", sol.numJewelsInStones("aA", "aAAbbbb") == 3)
    
    # 2. Edge Case: 겹치는 보석이 하나도 없을 때
    print("Test 2 (No Match):", sol.numJewelsInStones("z", "ZZ") == 0)
    
    # 3. Edge Case: 내가 가진 돌이 전부 보석일 때
    print("Test 3 (All Jewels):", sol.numJewelsInStones("abc", "abcabc") == 6)
    
    # 4. Edge Case: 대소문자 낚시 (대문자 S는 보석이 아님)
    print("Test 4 (Case Sensitive):", sol.numJewelsInStones("s", "SssS") == 2)
    
    # 5. Edge Case: 가진 돌이 아예 없을 때 (빈 문자열)
    print("Test 5 (Empty Stones):", sol.numJewelsInStones("aA", "") == 0)