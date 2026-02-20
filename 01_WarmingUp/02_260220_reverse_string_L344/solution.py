import sys
from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    :param s: 문자열 리스트
    """
    
    # note that how to swap in python: a, b = b, a
    # note that index: 0~len(s)
    # 짝수와 홀수 접근법이 살짝 다를 수도 있음

    for i in range(len(s)): # 이건 loop 용도 문법으로 써야하는데 legacy다 #While이 더 효율적??


        front_index = i
        end_index   = len(s) - (i+1)
        
        if front_index >= end_index:
            break

        s[front_index], s[end_index] = s[end_index], s[front_index]


    pass



if __name__ == "__main__":
    # 예제 테스트 케이스 1
    s1 = ["h","e","l","l","o"]
    print(f"Test Input 1 (Before): {s1}")
    reverseString(s1)
    print(f"Result 1 (After)   : {s1}") # ["o","l","l","e","h"] 나와야 함
    
    print("-" * 30)
    
    # 예제 테스트 케이스 2
    s2 = ["H","a","n","n","a","h"]
    print(f"Test Input 2 (Before): {s2}")
    reverseString(s2)
    print(f"Result 2 (After)   : {s2}") # ["h","a","n","n","a","H"] 나와야 함