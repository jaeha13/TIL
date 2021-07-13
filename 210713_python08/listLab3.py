listnum = [10, 5, 7, 21, 4, 8, 18]
min_num, max_num = listnum[0], listnum[0]

for num in listnum:
    if max_num < num:
        max_num = num
    elif min_num > num:
        min_num = num

print("최솟값 : ", min_num, ", 최댓값 : ", max_num)
