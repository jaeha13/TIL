try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
except FileNotFoundError:
    print("파일을 읽을 수 없어요")
else:
    count = 0
    while True:
        row = f.readline()
        if not row:
            break
        count += row.lower().count("yesterday")
        # 다른 방식: count = row.count("Yesterday") + row.count("yesterday")
    print("Number of a Word 'Yesterday'", count)
    f.close()
finally:
    print("수행완료!!")

"""
try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
except FileNotFoundError:
    print("파일을 읽을 수 없어요")
else:
    count = 0
    row = f.read()
    count = row.count("Yesterday") + row.count("yesterday")
    print("Number of a Word 'Yesterday'", count)
    f.close()
finally:
    print("수행완료!!")
"""