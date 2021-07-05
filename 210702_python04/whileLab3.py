import random
count = 0
while True:
    n = random.randint(0, 30)
    if 1 <= n <= 26:
        print(chr(64 + n), "(", n, ")", sep="")
        count += 1
    else:
        break
print("수행횟수는 ", count, " 번 입니다.")

"""
import random
count = 0
while True:
    n = random.randint(0, 30)
    if 1 <= n <= 26:
        print(chr(64 + n), "(", n, ")")
        count += 1
    else:
        break
print("수행횟수는 ", count, " 번 입니다.")
"""
