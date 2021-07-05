# 반복문(while)

```python
while 조건식:
    수행문장

"""
while False:
    수행문장
# 무의미: 한번도 실행되지 않을 것이다. => True이거나 not False로 해야함. 그러나 굳이 not False라고 하진 않겠지요!!
"""
```

> 산술 -> 비교 -> 논리 -> 대입 순

# 함수

1. 함수를 정의하는 방법
2. 정의된 함수를 필요에 따라 사용(호출)하는 방법

```wiki
print(), input(), int(), chr(), len(), range()
random.randint()
----> 파이썬에서 미리 정의해서 제공하는 함수들 - API
* 변수는 명칭만 함수는 ()!! (관례)
   - a, b, v, num, result : 변수
   - a(), b(), v(), num(), result() : 함수
```

## 함수 호출

* range(10)
* range(3, 7)
* range(1, 10, 2)
  * 함수 호출시 입력하는 데이터 값 = 아규먼트 또는 인수라고 부른다
* print()
* print(100)
* print(1, 2, 3, 4, 5)
* print("abc", 100, True)
* print(1, 2, 3, 4, 5, sep = "@")
  * 데이터 값만 나열하여 전달하는 경우 : 포지셔널 아규먼트(위치 아규먼트)
  * 변수명 = 데이터 값 형식으로 전달하는 경우 : 키워드 아규먼트

```python
input_data = input("이름을 입력하세요...")
name_length = len(input_data)

print(len("abc")) => 3
print(len("가나다")) => 3
```

## 함수 생성

```python
** def 함수명(매개변수):	# 매개 변수 : 아규먼트를 받는 변수
        함수 내용(코드블럭)

   def myFunction1():
        함수 내용(코드블럭)

   def myFunction2(p):
        함수 내용(코드블럭)

   def myFunction3(deco, num):
        함수 내용(코드블럭)

   cf) print()의 매개 변수는 가변형 매개 변수 -> 다음주에 배움!!

True, False, None(아무값도 없음)
```

