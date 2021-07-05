while True:
    mon = int(input("원하는 달을 선택하세요: "))
    if mon > 12 or mon < 1:
        print("1~12 사이의 값을 입력하세요!")
        break
    elif 3 <= mon <= 5:
        print(mon, "월은 봄")
    elif 6 <= mon <= 8:
        print(mon, "월은 여름")
    elif 9 <= mon <= 11:
        print(mon, "월은 가을")
    else:
        print(mon, "월은 겨울")

"""
while True:
    mon = int(input("원하는 달을 선택하세요: "))
    if 1 <= mon <= 12:
        if 3 <= mon <= 5:
            print(mon, "월은 봄")
        elif 6 <= mon <= 8:
            print(mon, "월은 여름")
        elif 9 <= mon <= 11:
            print(mon, "월은 가을")
        else:
            print(mon, "월은 겨울")
    else:
        print("1~12 사이의 값을 입력하세요!")
        break
"""
