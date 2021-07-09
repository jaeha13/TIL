# 2. 축약함수(Lambda)
# - 한 줄 함수
# 형식) 변수 = (lambda 인수 : 리턴값).upper().split()
# ex) lambda x, y : x + y

print('add=', (lambda x, y: x + y)(10, 20))

(lambda x, y, z: x + y + z)(10, 20, 30).print()


def func(x, y, z):
    sum1 = x + y + z
    return sum1


add = func(10, 20, 30)
print('add= ', add)
