#근의 공식
a, b, c = int(input("X^2항의 계수를 입력하세요: ")), int(input("X항의 계수를 입력하세요: ")), int(input("상수항을 입력하세요: "))

print("\n근의 공식")

if a == 0:
    print("X^2항의 계수는 0이 될 수 없습니다.")
else: 
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("서로 다른 두 허근이 있습니다.")
    elif d == 0:
        print(f"중근 {(-b) / (2 * a):.2f}입니다.")
    else:
        print(f"서로 다른 두 실근 {(-b + d ** 0.5) / (2 * a):.2f}과 {(-b - d ** 0.5) / (2 * a):.2f}입니다.")