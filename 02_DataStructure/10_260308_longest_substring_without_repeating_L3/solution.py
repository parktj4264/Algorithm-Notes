class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        print("============================")
        
        used = {}
        max_length = 0
        start = 0
        
        # enumerate를 써서 문자(char)와 인덱스(idx)를 동시에 뽑으며 순회
        for idx, char in enumerate(s):
            
            # print(idx, char)
            # print("start: ", start)
            
            if (char in used) and (used[char] >= start):
                start = used[char] + 1
            else:
                max_length = idx - start + 1

            # print("start2: ", start)
                
            used[char] = idx

            # print("used: ",used)
            # print("max_length: ",max_length)
            # print("___")
            
            # 1. 만약 char가 이미 used에 있고, 
            #    그 위치가 현재 윈도우의 start보다 크거나 같다면? (중복 발생!)
            #    -> start 포인터를 중복된 문자의 다음 위치로 이동시킨다.
            
            # 2. 그렇지 않다면?
            #    -> max_length를 현재 윈도우 길이(idx - start + 1)와 비교하여 갱신한다.
            
            # 3. 현재 문자(char)의 최신 인덱스(idx)를 used 딕셔너리에 기록한다.
            
        return max_length
    
    def lengthOfLongestSubstring_TRUE(self, s: str) -> int:
        used = {}
        max_length = 0
        start = 0
        
        for idx, char in enumerate(s):
            
            # 1. 중복 발생 시 윈도우 시작점(start) 확 당기기
            if char in used and used[char] >= start:
                start = used[char] + 1
                
            # 🔥 [팩폭 해결] else로 묶어서 무지성 덮어쓰기 금지!
            # 중복이 발생했든 안 했든, '현재 윈도우 길이'와 '기존 최대 길이' 중 큰 걸 유지한다!
            max_length = max(max_length, idx - start + 1)
            
            # 3. 문자의 최신 인덱스 기록
            used[char] = idx
            
        return max_length
    
    

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 기본 케이스 (abc가 반복됨 -> 3)
    print("Test 1 (Normal):", sol.lengthOfLongestSubstring("abcabcbb") == 3)
    
    # Test 2: 전부 같은 문자 (b 하나만 됨 -> 1)
    print("Test 2 (All Same):", sol.lengthOfLongestSubstring("bbbbb") == 1)
    
    # Test 3: 중간에 끊기는 경우 (wke -> 3)
    print("Test 3 (Substring):", sol.lengthOfLongestSubstring("pwwkew") == 3)
    
    # Test 4: 빈 문자열 (-> 0)
    print("Test 4 (Empty):", sol.lengthOfLongestSubstring("") == 0)
    
    # 🔥 Test 5: 악랄한 Edge Case (tmmzuxt -> 5, m에서 start가 2로 가고, 마지막 t에서 start가 1로 후진하면 안 됨!)
    print("Test 5 (Edge Case):", sol.lengthOfLongestSubstring("tmmzuxt") == 5)