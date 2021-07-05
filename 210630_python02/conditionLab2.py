"""
실습 2
1. color_name 이라는 변수에 사용자로부터 칼라 이름을 하나 입력받는다.
2. 입력받은 칼라명이 red 이면 '#ff0000'이라는 문자열을 출력한다.
   입력받은 칼라명이 red 가 아니면 '#000000'이라는 문자열을 출력한다.

1) input 함수를 통해 문자열을 압력받아 color_name 에 저장
2) if 조건문을 통해 color_name == red 인 경우 print 함수를 통해 '#ff0000' 출력
                 color_name != red 인 경우(else 인 경우) print 함수를 통해 '#000000' 출력
"""

# 파이썬은 대소문자 구분!!
# red != Red
color_name = input("색을 입력하시오: ")
if color_name == "red":
    print("#ff0000")
else:
    print("#000000")

"""
# ord('A') = 65 : ord('문자') : 아스키 코드를 숫자로 변환
# chr(65) = 'A' : chr(숫자) : 숫자를 아스키 코드로 변환

color_name = int(ord(input("색을 입력하시오: ")))
if color_name == "red":
    print("#ff0000")
else:
    print("#000000")
    
=> 결과
색을 입력하시오: r
#000000
"""