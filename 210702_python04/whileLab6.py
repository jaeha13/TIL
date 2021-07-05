while True:
    result = 1
    n = int(input("숫자를 입력하세요: "))
    if not n:
        print("종료")
        break
    elif n < -10 or n > 10:
        continue
    elif n > 0:
        print("입력값 : ", n)
    else:
        n = -n  # n = n * -1
        print("입력값(부호변경) : ", n)
    for i in range(1, n + 1):
        result *= i
    print(result)

"""
while True:
    result = 1
    n = int(input("숫자를 입력하세요: "))
    if not n:
        print("종료")
        break
    elif n < -10 or n > 10:
        continue
    elif n > 0:
        print("입력값 : ", n)
        for i in range(1, n + 1):
            result *= i
        print(result)
    else:
        print("입력값(부호변경) : ", -n)
        for i in range(1, -n + 1):
            result *= i
        print(result)
"""
