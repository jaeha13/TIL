"""
실습 7
1. num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
   입력 받을 때의 메시지 - 1 부터 10 사이의 숫자를 하나 입력하세요 :
2. 입력 받은 숫자가 1 부터 10 사이의 숫자가 아니면 다음과 같이 처리한다.
   - 1 부터 10 사이의 숫자를 하나 입력하세요 : 13
     1 부터 10 사이의 값이 아닙니다.
3. 입력 받은 숫자가 1 부터 10 사이의 숫자이면 다음과 같이 처리한다.
   - 1 부터 10 사이의 숫자를 하나 입력하세요 : 5
     5 : 홀수
   - 1 부터 10 사이의 숫자를 하나 입력하세요 : 8
     8 : 짝수

1) input 함수와 int 함수를 통해 숫자를 입력받아 num 에 저장
2) if 조건문을 통해 1 ~ 10 사이 수인지 판단
3) 아니면 "1부터 10사이의 값이 아닙니다." print 함수통해 출력
   맞을 경우 짝*홀수 판단 후 print 함수를 통해 출력
"""

num = int(input("1부터 10사이의 숫자를 하나 입력하세요: "))
if (num < 1) or (num > 10):
    print("1부터 10사이의 값이 아닙니다.")
else:
    if num % 2 == 0:
        print(num, " : 짝수")
    else:
        print(num, " : 홀수")