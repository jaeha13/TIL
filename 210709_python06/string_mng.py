# 문자열
# 인덱스
var = "0123456789"
print(var[0])       # 0


# 슬라이싱(slicing)
var = "abcdefg"
print(var[:])       # abcdefg
print(var[:5])      # abcde
print(var[-4:])     # defg
print(var[-4])      # d


lst = [[1, 2, 3, 4], 5, 6, ["a", "b"]]
print(lst[3])       # ['a', 'b']
print(lst[-3:4:2])  # [5, ['a', 'b']]


# upper(), lower(), capitalize()
a = "apple"
b = "APPLE"
print(a.upper())    # APPLE
print(b.lower())    # apple
print(a.capitalize())   # Apple


# isdecimal(), isdigit(), isnumeric()
a = "1234"
b = "12alei3"
c = "aera135"
print(a.isdecimal())        # True
print(a.isdigit())          # True
print(a.isnumeric())        # True
print(b.isdecimal())        # False
print(b.isdigit())          # False
print(b.isnumeric())        # False
print(c.isdecimal())        # False
print(c.isdigit())          # False
print(c.isnumeric())        # False


# split(), replace()
s1 = "짜장/짬뽕/탕수육"
print(s1.split("/"))     # ['짜장', '짬뽕', '탕수육']

s2 = "서울->대전->대구->부산"
print(s2.split("->"))   # ['서울', '대전', '대구', '부산']
print(s2.replace("->", " 찍고 "))     # 서울 찍고 대전 찍고 대구 찍고 부산

s3 = """hello world!!!
I'm Jay
Nice to meet you guys"""
print(s3.split("\n"))       # ['hello world!!!', "I'm Jay", 'Nice to meet you guys']

s3 = "apple pear banana strawberry blueberry"
fruit = s3.split(" ")
print(fruit)


# join()
s = ", "
print(s.join(fruit))
