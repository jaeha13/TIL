class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return "Book 클래스로 생성된 객체"

    def getBookInfo(self):
        return f"{self.title}, {self.author}, %s" % format(self.price, ',')


b1 = Book("파이썬 정복", "김상형", 22000)
b2 = Book("생활코딩! HTML+CSS+자바스크립트", "이고잉", 27000)
b3 = Book("빅데이터를 지배하는 통계의 힘", "니시우치 히로무", 15000)
b4 = Book("쓸만한 인간", "박정민", 13500)
b5 = Book("돈의 역사", "홍춘욱", 17800)

book = {'1': b1, '2': b2, '3': b3, '4': b4, '5': b5}
for i, b_class in book.items():
    print(f"[ 객체{i} : {b_class} ]")
    book_info = list(b_class.getBookInfo().split(', '))
    for j in range(len(book_info)):
        print(book_info[j])
    print('-' * 30)

