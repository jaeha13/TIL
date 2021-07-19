import calendar

while True:
    try:
        year = int(input("현재 년도수를 입력하세요: "))
        mon = int(input("현재 월을 입력하세요: "))
    except ValueError:
        print("숫자만 입력하세요!")
    else:
        break
print()
calendar.prmonth(year, mon)