height = int(input("height : "))
count_star = 0
for i in range(1, height + 1):
    count_star += i
    print("*" * i)
print("star 개수 : ", count_star)
