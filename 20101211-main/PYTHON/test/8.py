# 회원가입하기
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

while True:
    password = input("비밀번호를 입력하세요: ")

    if len(password) < 8:
        print("비밀번호는 8자 이상이어야 합니다. 다시 입력하세요.\n")
        continue 
    has_upper = False
    has_lower = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if has_upper and has_lower:
            break

    if has_upper and has_lower:
        print("안전한 비밀번호 입니다.")
        break
    else:
        print("대문자 또는 소문자가 부족합니다. 다른 비밀번호를 입력하세요.\n")