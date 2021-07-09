def star(x):
    count_star = 0
    for i in range(1, x + 1):
        count_star += i
        print("*" * i)
    print("star 개수 : ", count_star)


height = int(input("height : "))
star(height)
