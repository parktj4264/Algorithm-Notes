import re
from typing import List
from collections import Counter

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    """
    :param paragraph: 분석할 텍스트 단락
    :param banned: 제외할 금지어 리스트
    :return: 금지어를 제외하고 가장 많이 등장한 단어
    """
    
    

    
    pass

if __name__ == "__main__":
    # 예제 테스트 케이스 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(f"Test Input 1: '{paragraph1}' | banned: {banned1}")
    print(f"Result 1: {mostCommonWord(paragraph1, banned1)}") 
    # 정답: "ball"
    
    print("-" * 40)
    
    # 예제 테스트 케이스 2
    paragraph2 = "a."
    banned2 = []
    print(f"Test Input 2: '{paragraph2}' | banned: {banned2}")
    print(f"Result 2: {mostCommonWord(paragraph2, banned2)}") 
    # 정답: "a"