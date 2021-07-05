"""
실습 8
1. oper_num 이라는 변수에 1 부터 10 사이의 랜덤값을 추출하여 대입한다.
2. 추출된 값이 1이거나 6이면 300과 50의 덧셈 연산을 처리한다.
   추출된 값이 2이거나 7이면 300과 50의 뺄셈 연산을 처리한다.
   추출된 값이 3이거나 8이면 300과 50의 곱셈 연산을 처리한다.
   추출된 값이 4이거나 9이면 300과 50의 나눗셈 연산을 처리한다.
   추출된 값이 5이거나 10이면 300과 50의 나머지 연산을 처리한다.
3. 출력 형식(단, 결과를 출력하는 수행문장은 한번만 구현한다.)
   결과값 : XX

1) oper_num 이라는 변수에 randint(1, 10)을 통해 랜덤 추출하여 저장
2) if 조건문을 통해 적절한 연산 수행과 변수에 값 저장
   - if-elif-else 를 통해 해결
3) print 함수를 통해 결과값 출력
"""

import random
oper_num = random.randint(1, 10)
if oper_num == 1 or oper_num == 6:
    result = 300 + 50
elif oper_num == 2 or oper_num == 7:
    result = 300 - 50
elif oper_num == 3 or oper_num == 8:
    result = 300 * 50
elif oper_num == 4 or oper_num == 9:
    result = 300 / 50
else:
    result = 300 % 50
print("결과값 : ", result)
