#출석 체크
day = 0

print("=== 출석체크 프로그램 ===")
print("'출석'을 입력하세요. (종료하려면 '종료' 입력)\n")

while True:
    user_input = input("입력: ")

    if user_input == "출석":
        day += 1
        print(f"{day}일차 출석 완료!\n")
    elif user_input == "종료":
        print("프로그램을 종료합니다.")
        break
    else:
        print("'출석'이라고 정확히 입력해 주세요.\n")