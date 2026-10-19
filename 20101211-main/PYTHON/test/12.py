#BMI계산기
weight = float(input("체중(kg)을 입력하세요: "))
height = float(input("키(m)를 입력하세요: "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")