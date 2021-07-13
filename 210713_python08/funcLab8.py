def print_triangle_withdeco(num, deco='%'):
    if 1 <= num <= 10:
        for i in range(1, num + 1):
            for _ in range(num - i):
                print(end=' ')
            for _ in range(i):
                print(deco, end=' ')
            print()


print_triangle_withdeco(0)
print_triangle_withdeco(2)
print_triangle_withdeco(5, '*')
print_triangle_withdeco(11)


"""
def print_triangle_withdeco(num, deco = '%'):
    if 1 <= num <= 10:
        for i in range(1, num + 1):
            print(' ' * (num - i), end="")
            print(deco * i)


print_triangle_withdeco(0)
print_triangle_withdeco(2)
print_triangle_withdeco(5, '*')
print_triangle_withdeco(11)
"""