import datetime, os

if not os.path.exists("C:/iotest"):
    os.makedirs("C:/iotest")
now = datetime.datetime.now()
f = open("c:/iotest/today.txt", "wt", encoding="UTF-8")
days = ['월', '화', '수', '목', '금', '토', '일']
f.write(f"""오늘은 {now.year}년 {now.month:02d}월 {now.day}일입니다.
오늘은 {days[now.weekday()]}요일입니다.
나는 {days[datetime.date(1993, 4, 28).weekday()]}요일에 태어났습니다.""")
f.close()
print("저장이 완료되었습니다.")


"""
if not os.path.exists("C:/iotest"):
    os.makedirs("C:/iotest")
os.chdir("C:/iotest")
now = datetime.datetime.now()
f = open("today.txt", "wt", encoding="UTF-8")
...
"""