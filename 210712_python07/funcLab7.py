import random


def differtwovalue(num1, num2):
    return abs(num1 - num2)


"""
def differtwovalue(num1, num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1
"""

for _ in range(5):
    x, y = random.randint(1, 30), random.randint(1, 30)
    print(x, '와 ', y, '의 차는 ', differtwovalue(x, y), '입니다.')

