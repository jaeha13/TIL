"""
실습 4
1. grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.
   조건 평가 시 and 연산자를 사용해서 해결한다.
2. grade 의 값이 1 또는 2 또는 3 이면 다음 결과를 출력한다.
   x 학년은 저학년입니다.
   grade 의 값이 4 또는 5 또는 6 이면 다음 결과를 출력한다.
   x 학년은 고학년입니다.

1) import random 을 통해 random 라이브러리를 불러온다.
2) grade 에 random.randint(1, 6)을 통해 1 ~ 6 사이의 숫자를 랜덤 추출하여 저장
3) if 조건문을 통해 학년 구분
   - or 를 이용!!
   - 1 or 2 or 3 => 저학년
"""

import random
grade = random.randint(1, 6)
if grade == 1 or grade == 2 or grade == 3:
    print(grade, "학년은 저학년입니다.")
else:
    print(grade, "학년은 고학년입니다.")
