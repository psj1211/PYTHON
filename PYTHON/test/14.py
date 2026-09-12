#최대공약수,최소공배수 구하기
a = int(input("첫번째 숫자를 입력하세요(숫자 비교를 위해 더 큰 수를 입력해주세요): "))
b = int(input("두번째 숫자를 입력하세요(첫번째 숫자보다 작은 수를 입력해주세요): "))
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

# LCM = (a * b) / GCD
lcm = (a * b) // gcd

print(f"최대공약수(GCD): {gcd}")
print(f"최소공배수(LCM): {lcm}")