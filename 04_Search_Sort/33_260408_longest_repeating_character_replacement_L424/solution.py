import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = collections.defaultdict(int)
        max_count = 0 
        max_len = 0   
        
        # right 포인터가 0부터 끝까지 한 칸씩 전진 (윈도우 확장)
        for right in range(len(s)):
            # 1. 새로 윈도우에 들어온 알파벳(s[right])의 개수를 1 증가시킨다.
            counts[s[right]] += 1
            
            # 2. 현재 윈도우 내 단일 알파벳 최대 빈도수(max_count) 갱신
            # 힌트: 기존 max_count와 방금 추가된 알파벳의 개수 중 큰 값을 선택
            max_count = max(max_count, counts[s[right]])
            
            # 3. 🚨 치트키 한도 초과 검사! 
            # (현재 윈도우 크기) - (가장 많이 나온 알파벳 개수) > k 라면?
            if (right - left + 1) - max_count > k:
                # 3-1. 윈도우에서 빠져나갈 맨 왼쪽 알파벳(s[left])의 개수를 1 뺀다.
                counts[s[left]] -= 1
                
                # 3-2. left 포인터를 한 칸 오른쪽으로 당겨서 윈도우를 줄인다.
                left += 1
                
            # 4. 안전한 윈도우가 되었으므로, 최대 길이(max_len)를 갱신
            max_len = max(max_len, right - left + 1)
            
        return max_len

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    print("TC 1:", sol.characterReplacement("ABAB", 2)) # 예상 결과: 4
    
    # Test Case 2
    print("TC 2:", sol.characterReplacement("AABABBA", 1)) # 예상 결과: 4