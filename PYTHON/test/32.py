hit = 0
damage = 100
while damage * hit <1000:
    hit = hit + 1
    print(f"{hit * damage}의 데미지를 넣었습니다")
    if damage * hit >= 1000:
        print("적을 처치했습니다")