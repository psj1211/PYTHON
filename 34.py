#파이썬 실험
def add(*arge):
    result = 0
    for i in arge:
        result = result + i
    return result
result = add(1,2,3,4,5,6,7,8,9,10,-34,1234)
print(result)
