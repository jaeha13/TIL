# 1. tuple list 로부터 dict 생성
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
my_dict = dict(persons)
print(my_dict)

age = my_dict["홍대길"]
print(age)  # 35


# 2. list 인덱스 이용
a = [1.4, 2.5, 3.7, 4.2, 5.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)    # [1, 2, 3, 4, 5]


# 3. map 함수 이용
a = [1.4, 2.5, 3.7, 4.2, 5.6]
a = list(map(int, a))
print(a)    # [1, 2, 3, 4, 5]

numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)


for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
"""
1 A a
2 B b
3 C c
4 D d
5 E e
"""

print(type(number))     # <class 'str'>
