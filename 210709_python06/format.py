var = 1235
print("%s" % var)
print("%d" % var)
print("%f" % var)


var = 123.56
print("%d" % var)


price = [30, 13500, 2000]
for p in price:
    print("가격 : %-7d원" % p)
# -7d : 왼쪽부터 시작 7칸
"""
가격 : 30     원
가격 : 13500  원
가격 : 2000   원
"""

pie = 3.14159265
print("%10f" % pie)         # 10 칸으로 나타낼거야 소수점 default = 6
print("%10.6f" % pie)       # 10 칸으로 나타낼거야 소수점은 6자리까지
print("%10.8f" % pie)       # 10 칸으로 나타낼거야 소수점은 8자리까지
print("%10.5f" % pie)       # 10 칸으로 나타낼거야 소수점은 5자리까지
print("%10.2f" % pie)       # 10 칸으로 나타낼거야 소수점은 2자리까지
print("pie = ", pie)
"""
  3.141593
  3.141593
3.14159265
   3.14159
      3.14
pie =  3.14159265
"""

# round()
print(round(3.1515))        # 3 : 두번째 인자 없으면 소수 첫째 자리에서 반올림
print(round(3.1515, 2))     # 3.15 : 두번째 인자 소수점까지 나타냄
print(round(31.415, -1))    # 30.0

# round() 함수는 사사오입 원칙을 따름
# 반올림할 자리의 수가 5이면 앞자리의 숫자가 짝수면 내림, 홀수면 올림
print(round(4.5))           # 4
print(round(3.5))           # 4
