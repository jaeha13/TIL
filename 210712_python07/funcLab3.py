def expr(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    else:
        return


operation = ['+', '-', '*', '/', '%']
for i in operation:
    result = expr(3, 5, i)
    if result:
        print("연산결과 : ", result)
    else:
        print("수행불가")
