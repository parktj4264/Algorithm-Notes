import sys
import re

def isPalindrome(s: str) -> bool:
    """
    :param s: 입력 문자열
    :return: 팰린드롬 여부 (True/False)
    """
    # 💡 쌤의 힌트: 
    # 1. 정규식(re)으로 불순물(특수문자) 제거하고 소문자로 변환 (Data Cleaning)
    # 2. Python의 리스트 슬라이싱을 활용하면 코드가 섹시해진다. (s[::-1] 같은 거)
    # 3. R처럼 for loop 돌리면서 하나씩 비교하면 시간 복잡도 O(N)이라도 코드가 구려.
    
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)

    rev_s = s[::-1]

    return s == rev_s

if __name__ == "__main__":
    # 예제 테스트 케이스
    s1 = "A man, a plan, a canal: Panama" # True 나와야 함
    s2 = "race a car"                     # False 나와야 함
    
    print(f"Test Input 1: '{s1}'")
    print(f"Result 1: {isPalindrome(s1)}")
    
    print("-" * 20)
    
    print(f"Test Input 2: '{s2}'")
    print(f"Result 2: {isPalindrome(s2)}")