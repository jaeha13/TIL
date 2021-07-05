"""
실습 6
1. score 라는 변수에 0 부터 100 사이의 숫자를 랜덤으로 추출학 저장한다.
2. score 변수의 값의 크기에 따라서 다음을 출력한다. -> print() 함수를 5개 사용하여 해결한다.
   score 변수의 값이 90~100 이면 xx 점은 A 등급입니다.
   score 변수의 값이 80~89 이면 xx 점은 B 등급입니다.
   score 변수의 값이 70~79 이면 xx 점은 C 등급입니다.
   score 변수의 값이 60~69 이면 xx 점은 D 등급입니다.
   score 변수의 값이 0~59 이면 xx 점은 F 등급입니다.
3. print 함수는 한번만 사용한다.

1) score 변수에 random.randint(0, 100)을 통해 0 ~ 100 사이의 값을 랜덤 추출한다.
2) if 조건문을 통해 score 의 범위에 따라 grade 를 다르게 준다
   - 점수는 연속적인 수치이고 특정 수를 기준으로 나누기 때문에 100 부터 하나씩 걸러서 다음 조건문 수행
   - 의미 없는 비교식을 계속 수행하는 것을 방지하기 위해 if - if - if ..로 하지 않고
   - if - elif - elif - .. - else 로!!
3) 변수를 통해 조건에 따라 grade 를 할당하고 마지막에 print 함수를 사용!
"""

import random
score = random.randint(0, 100)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(score, "점은 ", grade, "등급 입니다.")
