import random

s = set()
while len(s) < 6:
    s.add(random.randint(1, 45))

print("행운의 로또번호 : ", end="")
for d in s:
    print(d, end=" ")
print()