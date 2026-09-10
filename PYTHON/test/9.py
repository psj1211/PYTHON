#계산기
a = int(input("어떤 계산을 하시겠습니까? (1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈): "))
b = int(input("첫 번째 숫자를 입력하세요: "))
c = int(input("두 번째 숫자를 입력하세요: "))

if a == 1:
    result = b + c
    print(f"{b} + {c} = {result}")
elif a == 2:
    result = b - c
    print(f"{b} - {c} = {result}")
elif a == 3:
    result = b * c
    print(f"{b} * {c} = {result}")
elif a == 4:
    if c == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result = b / c
        print(f"{b} / {c} = {result}")
if a not in [1, 2, 3, 4]:
    print("잘못된 입력입니다. 1, 2, 3, 4 중 하나를 선택하세요.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   