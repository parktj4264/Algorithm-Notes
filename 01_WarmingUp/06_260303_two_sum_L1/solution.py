from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 지나온 숫자들의 값과 인덱스를 저장할 딕셔너리 생성
        seen = {}
        # 흠 여기서 dict을 미리 만드는 거겠지...? 방법이??
        # 한줄로 추가할 수 있을거같은데.. 못하겠다 일단은 이렇게!!
        # for i, num in enumerate(nums):
        #     seen[num] = i
        # 밑에 힌트보면 아닌거같긴하다...

        # seen = {i,num for i,num in enumerate(nums)} <- 안되네...

        
        # 2. enumerate를 활용해 nums를 순회
        # for i, num in enumerate(nums):
            
            # 3. 내가 필요한 짝꿍 숫자 계산
            
            # 4. 짝꿍 숫자가 seen 딕셔너리에 있는지 확인
            # 4-1. 있다면? 정답 리턴!
            
            # 4-2. 없다면? 현재 숫자(num)와 인덱스(i)를 seen 딕셔너리에 저장

        for i, num in enumerate(nums):
            # print(i, num)
            pair_num = target - num
            # print(pair_num)

            if pair_num in seen:
                # print("good")
                # print([i, seen[pair_num]])
                return sorted([i, seen[pair_num]])
                break
                
            else: 
                # print("no")
                seen[num] = i
                
        #return []
    





if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    # print(sol.twoSum(nums1, target1))
    print(sol.twoSum(nums1, target1) == [0, 1])  # True 나와야 함
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(sol.twoSum(nums2, target2) == [1, 2])  # True 나와야 함

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(sol.twoSum(nums3, target3) == [0, 1])  # True 나와야 함