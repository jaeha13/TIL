import datetime

now = datetime.datetime.now()
f = open(f"sample_{now.year}_{now.month:02d}_{now.day}.txt", "at", encoding="UTF-8")
sample = open("sample.txt", "rt", encoding="UTF-8")
text = sample.read()
f.write(text)
f.write('\n')
sample.close()
f.close()
print("저장이 완료되었습니다.")