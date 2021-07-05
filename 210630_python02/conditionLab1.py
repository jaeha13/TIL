"""
실습 1
1. num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
2. 입력받은 숫자가 10보다 큰 경우에만 'OK' 라는 문자열을 출력한다.

1) input 함수를 통해 숫자를 입력받아 num 이라는 변수에 저장
2) input 함수의 return 값은 "문자열"이므로 int 로 형변환
3) if 조건문을 통해 10보다 큰 경우 print 함수를 통해 'OK' 출력
                그렇지 않은 경우 nothing!
"""

# 데이터를 입력받아 "문자열"로 return 하는 함수 : input("지시문")
# 대화형 함수이므로 입력을 받을 때까지 기다리게 된다. -> enter = 입력 끗!!
# int 형변환 함수 : int()
# num : 변수, l-value, 데이터 상자
num = int(input("숫자를 입력하시오: "))
if num > 10:
    print("OK")

"""
input_data = input("숫자를 입력하시오: ")
num = int(input_data)
if num > 10:
    print("OK")
"""