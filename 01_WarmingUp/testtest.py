import sys

print(f"🐍 Python Version: {sys.version}")
print("-" * 30)

# 리스트 컴프리헨션 테스트
test_list = [n * 2 for n in range(1, 6)]
print(f"🚀 Test List: {test_list}")

if test_list == [2, 4, 6, 8, 10]:
    print("✅ 환경 설정 완벽함. PT쌤한테 가도 됨!")
else:
    print("❌ 뭔가 꼬임. 다시 체크해봐.")