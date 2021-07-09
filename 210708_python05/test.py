num = 5   # 전역변수


def 함수1():
    mul = 1
    for i in range(1, num):
        mul *= i
    return mul


print(함수1())


def 함수1():
    a, b = 2, 3		# 지역변수 - 함수 외부에서 사용 X
    n = a + b
    return n


def 함수2():
    n = 2 ** 10		# 함수1의 n과 이름만 같은 다른 변수!!
    return n


print(함수1())
print(함수2())


def plus(a, b, c):
    z = a + b + c
    return z


add = plus(1, 2, 3)
print(add)
print("add = ", add)


def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return factorial(n - 1) * n
    else:
        return


print(factorial(5))


def func(x, y):
    z = x + y
    return z


print(func(10, 20))
print((lambda x, y: x + y)(10, 20))
