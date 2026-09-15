#숫자 맞추기 게임
import random

secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자 입력: "))
    attempts += 1

    if guess < secret_number:
        print("UP! 더 큰 숫자입니다.")
    elif guess > secret_number:
        print("DOWN! 더 작은 숫자입니다.")
    else:
        print(f"정답입니다! {attempts}번 만에 맞추셨습니다.")
        break