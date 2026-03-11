class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        # 전체적으로 지저분하다..
        for i in s:
            if i not in mapping: #여는 기호이면 stack에 쌓는다
                # print(i)
                stack.append(i)

            else: #닫는기호일때
                if len(stack) == 0: #열었던게 없으면 바로 False / 근데 빈 list 확인법 좋은게 있을거 같다
                    return False
                elif mapping[i] == stack.pop():
                    pass
                else:
                    return False

        if len(stack) == 0: return True
        else: return False




if __name__ == "__main__":
    sol = Solution()
    
    # 엣지 케이스 영혼까지 끌어모은 테스트 케이스
    test_cases = [
        ("()", True, "기본 열고 닫기"),
        ("()[]{}", True, "순차적 열고 닫기"),
        ("{[]}", True, "정상 중첩"),
        ("(]", False, "다른 짝으로 닫기"),
        ("([)]", False, "교차 닫기"),
        ("(", False, "열린 괄호만 하나 있음"),
        ("]", False, "닫힌 괄호만 하나 있음"),
        ("(((", False, "열린 괄호만 여러 개"),
        (")))", False, "닫힌 괄호만 여러 개"),
        ("(){}}{", False, "개수는 맞는데 순서가 개판"),
        ("[({})]", True, "깊은 중첩"),
    ]
    
    success_count = 0
    for i, (s, expected, description) in enumerate(test_cases, 1):
        result = sol.isValid(s)
        if result == expected:
            print(f"✅ 테스트 {i} 통과: {description} (입력: '{s}')")
            success_count += 1
        else:
            print(f"❌ 테스트 {i} 실패: {description}")
            print(f"   입력: '{s}'")
            print(f"   기대값: {expected}, 출력값: {result}")
            
    print("-" * 30)
    print(f"총 {len(test_cases)}개 중 {success_count}개 성공")