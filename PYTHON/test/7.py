# 여자친구가 생길 확률 구하기
print(input("당신의 이름을 입력하세요: ") + "님, 안녕하세요! 여자친구가 생길 확률을 계산해드리겠습니다.")
a = int(input("주변에 관심있는 여자가 몇 명인지 입력하세요: "))

all_fail_prob = 1.0

for i in range(a):
    answer = input(f"{i + 1}번째 여자와 사귈 수 있는 확률은 얼마인것 같나요? (0~100 사이의 숫자로 입력하세요): ")
    all_fail_prob *= (1 - float(answer) / 100)

success_prob = (1 - all_fail_prob) * 100

print(f"\n그 중 한 명이라도 여자친구가 될 확률: {success_prob:.2f}% ({all_fail_prob:.4f})")