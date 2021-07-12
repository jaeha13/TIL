def get_book_title():
    return "Python 파이썬 정복"


def get_book_publisher():
    return "한빛미디어"


name = get_book_title()
# 수정 : 2번 호출!!
for _ in range(2):
    print(name)
print(get_book_publisher())
