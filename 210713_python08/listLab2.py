listnum = [10, 5, 7, 21, 4, 8, 18]
min_num = listnum[0]

for num in listnum:
    if min_num > num:
        min_num = num

print("최솟값 : ", min_num)
