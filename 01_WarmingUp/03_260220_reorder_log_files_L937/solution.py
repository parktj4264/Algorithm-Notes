import sys
from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    """
    :param logs: 로그 문자열 리스트
    :return: 조건에 맞게 재정렬된 로그 리스트
    """
    letters, digits = [], []

    # 일단 logs의 item 별로 불러와서 쪼개야지
    for log in logs:
        id, content = log.split(" ", 1)

        if content[0].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key = lambda x:(x.split(" ", 1)[1], x.split(" ", 1)[0]))

    results = letters + digits

    # 뭔가 비효율적으로 같은걸 계속한듯... 그리고 lambda 정말 이해 안 된다

    return results





if __name__ == "__main__":
    # 예제 테스트 케이스 1
    logs1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print("Test Input 1:")
    for log in logs1: print(f"  {log}")
    
    result1 = reorderLogFiles(logs1)
    print("\nResult 1:")
    for log in result1: print(f"  {log}")
    # 정답: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    
    print("-" * 40)
    
    # 예제 테스트 케이스 2
    logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print("Test Input 2:")
    for log in logs2: print(f"  {log}")
    
    result2 = reorderLogFiles(logs2)
    print("\nResult 2:")
    for log in result2: print(f"  {log}")
    # 정답: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

    