#야구게임
import random

nums = random.sample(range(1, 10), 3)
count = 0

while True:
    question = input("3자리 숫자를 입력하세요: ")
    guess = list(map(int, question))
    count += 1

    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == nums[i]:
            strike += 1
        elif guess[i] in nums:
            ball += 1

    if strike == 3:
        print(f"정답! {count}번 만에 맞혔습니다.")
        break

    print(f"{strike}스트라이크 {ball}볼")