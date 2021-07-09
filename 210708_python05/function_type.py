# 인수가 없는 경우
def userFunc1():
    for _ in range(30):
        print("=", end="=")


userFunc1()


# 인수가 2개 return 0개
def userFunc2(x, y):
    print()
    z = x + y
    print("z = ", z)


userFunc2(10, 20)


# 인수가 2개 return 4개
def userFunc3(x, y):
    print("userFunc3")
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div


x = int(input("x 입력 : "))
y = int(input("y 입력 : "))

t, s, m, d = userFunc3(x, y)
print("tot = ", t)
print("sub = ", s)
print("mul = ", m)
print("div = ", d)
