listnum = [10, 5, 7, 21, 4, 8, 18]
max_num = listnum[0]

for num in listnum:
    if max_num < num:
        max_num = num

print("최댓값 : ", max_num)
