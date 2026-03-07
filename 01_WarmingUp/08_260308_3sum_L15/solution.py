from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        # 1. 여기서부터 뭔가 처리를 하고 시작해야 함 (투 포인터를 쓰기 위해)
        nums.sort()
        
        # 2. X를 고정하는 for문 + Y, Z를 찾는 투 포인터 설계
        for X_idx in range(len(nums) - 2):
            
            # print(X_idx)
            if X_idx > 0 :
                if nums[X_idx-1] == nums[X_idx]:
                    continue
            
            Y_idx = X_idx + 1
            Z_idx = len(nums) - 1
            
            while(Y_idx < Z_idx):
                
                # print(X_idx, Y_idx, Z_idx)
                
                if nums[X_idx] + nums[Y_idx] + nums[Z_idx] == 0:
                    results.append([nums[X_idx], nums[Y_idx], nums[Z_idx]])
                    
                    Y_idx += 1
                    Z_idx -= 1
                    
                    
                elif nums[X_idx] + nums[Y_idx] + nums[Z_idx] > 0:
                    
                    Z_idx -= 1
                    while(nums[Z_idx] == nums[Z_idx+1]):
                        Z_idx -= 1
                    
                    
                else:
                    
                    Y_idx += 1    
                    while(nums[Y_idx-1] == nums[Y_idx]):
                        Y_idx += 1  
                    
            
        return results
    
    #--------------

    def threeSum_pt_refactored(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        # [PT쌤 칭찬👍] 아주 좋아. 투 포인터의 1원칙, 데이터에 '방향성' 부여 완벽해.
        nums.sort()
        
        for X_idx in range(len(nums) - 2):
            
            # [PT쌤 훈수 1 🛠️] 로직은 완벽해! 
            # 근데 파이썬은 if문 두 개 안 나누고 `and`로 묶어서 한 줄로 치는 게 훨씬 Pythonic해.
            # 변경 추천: if X_idx > 0 and nums[X_idx-1] == nums[X_idx]: continue
            if X_idx > 0 :
                if nums[X_idx-1] == nums[X_idx]:
                    continue
            
            Y_idx = X_idx + 1
            Z_idx = len(nums) - 1
            
            # [PT쌤 훈수 2 🛠️] 파이썬 while문이나 if문엔 조건 괄호() 안 써도 돼! R 버릇 나왔네 ㅋㅋㅋ
            while Y_idx < Z_idx:
                
                # [PT쌤 훈수 3 🛠️] 이 긴 수식을 밑에서 3번이나 반복하잖아?
                # total = nums[X_idx] + nums[Y_idx] + nums[Z_idx] 이렇게 변수로 하나 빼두면 
                # 연산도 줄고 코드도 훨씬 예뻐져.
                
                if nums[X_idx] + nums[Y_idx] + nums[Z_idx] == 0:
                    results.append([nums[X_idx], nums[Y_idx], nums[Z_idx]])
                    
                    Y_idx += 1
                    Z_idx -= 1
                    
                    # 🔥 [PT쌤 치명적 팩폭 1 - 오답 사유] 
                    # 여기서 정답 찾았다고 그냥 한 칸만 옮기고 끝내면 대참사 나!
                    # 만약 다음 Y_idx 숫자도 방금 거랑 똑같으면 똑같은 정답 조합이 또 들어가버려.
                    # 무조건 여기서 중복 스킵 while문이 들어가야 해. (Y_idx랑 Z_idx 둘 다!)
                    
                    
                elif nums[X_idx] + nums[Y_idx] + nums[Z_idx] > 0:
                    
                    Z_idx -= 1
                    # 🔥 [PT쌤 치명적 팩폭 2 - IndexError 시한폭탄]
                    # while문에 인덱스 범위를 제어하는 (Y_idx < Z_idx) 조건이 없지?
                    # 이러면 배열 끝까지 똑같은 숫자일 때 Z_idx가 마이너스 뚫고 지하까지 파고들어 가.
                    # 수정: while Y_idx < Z_idx and nums[Z_idx] == nums[Z_idx+1]:
                    while(nums[Z_idx] == nums[Z_idx+1]):
                        Z_idx -= 1
                    
                    # 💡 [꿀팁] 사실 크거나 작을 땐 굳이 while로 중복 안 건너뛰고 
                    # 딱 한 칸(Z_idx -= 1)만 옮겨도 알아서 바깥 while문이 또 돌면서 처리해 줘.
                    
                    
                else:
                    
                    Y_idx += 1    
                    # 🔥 [PT쌤 팩폭 2 동일] 
                    # 여기도 인덱스 아웃 오브 바운즈(Index Out of Bounds) 위험!
                    # 수정: while Y_idx < Z_idx and nums[Y_idx-1] == nums[Y_idx]:
                    while(nums[Y_idx-1] == nums[Y_idx]):
                        Y_idx += 1  
                    
        return results



if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [-1,0,1,2,-1,-4]
    print("Test 1:", sol.threeSum(nums1)) # [[-1,-1,2], [-1,0,1]] 나와야 함
    
    # Test Case 2
    nums2 = [0,1,1]
    print("Test 2:", sol.threeSum(nums2)) # [] 나와야 함

    # Test Case 3
    nums3 = [0,0,0]
    print("Test 3:", sol.threeSum(nums3)) # [[0,0,0]] 나와야 함