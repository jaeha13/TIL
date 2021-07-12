def print_gugudan(dan):
    if type(dan) != int:
        return
    elif not 1 <= dan <= 9:
        return
    else:
        for i in range(1, 10):
            print(dan, ' * ', i, ' = ', dan * i)


print_gugudan(11)
print_gugudan(7)
print_gugudan(1.3)
print_gugudan("8")
print_gugudan(9)


"""
참고
def print_gugudan(dan):
    if type(dan) != int or not 1 <= dan <= 9:
        return
    else:
        for i in range(1, 10):
            print(dan, ' * ', i, ' = ', dan * i)
"""