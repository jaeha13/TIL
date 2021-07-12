def print_triangle(num):
    if 1 <= num <= 10:
        for n in range(1, num + 1):
            print('*' * n)
# else 문의 역할이 없기 때문에 생략 가능!!
#    else:
#        return


print_triangle(2)
print_triangle(11)
print_triangle(5)

