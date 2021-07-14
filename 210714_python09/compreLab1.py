def createList(type=1, *args):
    if len(args) == 0:
        args = [i for i in range(1, 31)]
    if type == 1:
        lst = [*args]
    elif type == 2:
        lst = [i for i in args if not i % 2]
    elif type == 3:
        lst = [i for i in args if i % 2]
    elif type == 4:
        lst = [i for i in args if i > 10]
    return lst


print(createList(type=1))
print(createList(2, 1))
print(createList(3, 1))
print(createList(4, 1))
print(createList(2, 1, 2, 3, 4, 5, 6, 80, 30, 2))
print(createList(3, 34, 25, 12, 245))
print(createList(4, 36, 24, 21, 35, 46, 57, 68, 23))