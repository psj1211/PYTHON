#로그인 한도 만들기(클로드 사용_시간관련만)
import time

Backup_ID = input("아이디를 입력하세요: ")
Backup_PASSWORD = input("비밀번호를 입력하세요: ")
attempts = 0
max_attempts = 3

while True:
    while attempts < max_attempts:
        ID = input("아이디를 입력하세요(확인용): ")

        if ID != Backup_ID:
            print("아이디가 잘못되었습니다.")
            attempts += 1
            continue  

        while attempts < max_attempts:
            PASSWORD = input("비밀번호를 입력하세요(확인용): ")

            if PASSWORD == Backup_PASSWORD:
                print("로그인 성공!")
                break
            else:
                print("비밀번호가 잘못되었습니다.")
                attempts += 1
        break 

    if attempts == max_attempts:
        print("로그인 시도 회수를 초과하여 20초의 대기 시간이 필요합니다.")

        wait_time = 20
        while wait_time > 0:
            print(f"{wait_time}초 남았습니다.")
            time.sleep(1)
            wait_time -= 1
        print("시간이 충족되었습니다.")

        attempts = 0
    else:
        break