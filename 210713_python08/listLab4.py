import random
# 2
listnum = []    # list()
# 3
for _ in range(10):
    listnum.append(random.randint(1, 50))
# 4
print(listnum)
# 5
for i in range(len(listnum)):
    if listnum[i] < 10:
        listnum[i] = 100
# 6
print(listnum)
# 7
print(listnum[0])
# 8
print(listnum[9])   # listnum[-1]
# 9
print(listnum[1:6])
# 10
print(listnum[::-1])
# 11
print(listnum[:])   # listnum[::1]
# 12
del listnum[4]
# 13
print(listnum[:])
# 14
listnum[1:3] = []
# 15
print(listnum[:])
