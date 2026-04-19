import re
import collections
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. 정규표현식으로 구두점 날리고 소문자로 변경 후 리스트로 쪼개기
        # 2. banned에 없는 단어만 남기기 (리스트 컴프리헨션 활용)
        # 3. Counter 객체 써서 가장 흔한 단어 뽑아내기

        clean_parag = re.sub(r'[^\w]', ' ', paragraph)
        clean_low_parag = clean_parag.lower()
        clean_low_parag_list = clean_low_parag.split(" ")

        word_list = [word for word in clean_low_parag_list if (word not in banned) & (len(word) > 0)]

        counts = collections.Counter(word_list)
        most = counts.most_common(1)[0][0]

        return most

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print("Test 1:", sol.mostCommonWord(paragraph1, banned1)) 
    # 예상 출력: "ball"

    # Test Case 2
    paragraph2 = "a."
    banned2 = []
    print("Test 2:", sol.mostCommonWord(paragraph2, banned2)) 
    # 예상 출력: "a"
