# 210712 python review

## 함수

### 인수(argument)

> 또는 매개변수(parameter) 라고도 함

: 함수의 입력값으로 들어가는 값

```python
# 함수에 따라 argument 개수가 달라짐(0, 1, 2, ..)
def func0():			# argument 0
    for _ in range(10):
        print("hello")
        
def func1(num):			# argument 1
    # num이 argument
    for _ in range(num):
        print("hello")
        
# ex. name = ['ha', 'jay', 'py', 'thon']
def func2(num, name):	# argument 2
    for _ in range(num):
        for i in name:
            print(i, end = ' ')
        print()
```

### 가변 인수

> 고정되지 않은 임의 개수의 인수를 받음 = 0 개 이상의 positional argument 를 전달 가능
>
> \* 기호를 인수 이름 앞에 붙임
>
> python, R, JavaScript에서 모두 쓰임

```python
print()
print(10)
print('abc')
print(10, 20, '가나다')
print(10, 20, 30, sep='@', end='\n\n')
print(...)

def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum
    
# * : 전달받은 argument는 모두 내꺼야!!
# 그래서 가변인수는 마지막에 와야함
intsum(s, *ints)		# OK
intsum(*ints, s)		# Error
intsum(*ints, *nums)	# Error
```

### 키워드 가변 인수

> 0개 이상의 keyword argument 를 전달 가능
>
> \** 기호를 인수 이름 앞에 붙임

#### 키워드 인수

> 인수 이름 지정하여 대입 형태로 전달하는 방식
>
> positional argument : 위치에 따라 mapping 되는 형식으로 인수 지정됨

```python
def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print("3 ~ 5 = ", calcstep(3, 5, 1))	# positional argument 이용
print("3 ~ 5 = ", calcstep(begin = 3, end = 5, step = 1))
print("3 ~ 5 = ", calcstep(step = 1, end = 5, begin = 3))
print("3 ~ 5 = ", calcstep(3, 5, step = 1))	# keyword 인수가 없는 경우 순서대로 positional argument
print("3 ~ 5 = ", calcstep(3, step = 1, end = 5))
'''
print("3 ~ 5 = ", calcstep(begin = 3, 5, 1))
# Error : keyword 인수를 먼저 사용한 경우 그 이후는 무조건 keyword 인수 사용해야 함
'''
```

### return [식]

​					**리터럴, 변수, 연산식, 리턴값이 있는 함수의 호출식**

:  함수로부터 반환되는 값

```python
# 함수에 따라 return value 개수가 달라짐
def til_num_print(num):
    for i in range(num + 1):
        print(i)
    return	# return value 0 == NONE -> 생략가능

def til_num_sum(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum	# return value 1

def til_num_sum_mul(num):
    sum = 0
    mul = 1
    for i in range(1, num + 1):
        sum += i
        mul *= i
    return sum, mul	# return value 2
```



## 연산자

### 이항 연산자

> 항이 2개, 피연산자 2개

```
비교식 and 비교식
숫자 + 숫자
문자열 + 문자열
```

### 단항 연산자

> (항이 1개, 피연산자 1개)

```
not bool 식
```

bool 타입 : 특별한 형태의 숫자 타입

​					True --> 1

​					False --> 0



## 변수의 범위(scope)

> 변수가 생성된 후 언제까지 이 변수를 사용할 수 있는지 정한 범위

### 전역 코드

* 생성되는 변수 : 전역 변수

  * 어떤 지역에서나 사용할 수 있는 변수

  * **함수 내부에서 value 변환 안됨. 단, `global`로 하면 가능!!**

    ```python
    def func1(p1, p2, p3, p4):
        global a, b, d
        a = p1
        b = p2
        c = p3
        d = p4
        print('[지역] a=', a, ' b=', b, ' c=', c, ' d=', d, sep='', end='\n\n')
    
    a = 10
    b = 20
    c = 30
    print('[전역(함수호출전)] a=', a, ' b=', b, ' c=', c, sep='', end='\n\n')
    func1('A', 'B', 'C', 'D')
    print('[전역(함수호출후)] a=', a, ' b=', b, ' c=', c, ' d=', d, sep='', end='\n\n')
    
    
    # 실행 결과
    [전역(함수호출전)] a=10 b=20 c=30
    
    [지역] a=A b=B c=C d=D
    
    [전역(함수호출후)] a=A b=B c=30 d=D
    ```

### 함수 코드 블럭

> 함수 내부 코드 블럭

* 생성되는 변수 : 지역 변수

  - 특정 지역(함수 내)에서만 사용 가능한 변수

  - **같은 이름의 전역변수와 지역변수가 있을 경우, 이름만 같은 다른 변수임!!(동명이변)**

```python
price = 1000

def kim():
    print("오늘의 가격 : ", price)	# r-value(값) : 지역변수가 없으면 전역변수를 찾아서 사용


def sale():
    price = 500					# l-value(값) : 지역변수를 새로 만듦
    print("price = ", price)	# r-value(값) : 지역변수가 있으므로 지역변수 사용


kim()			# 오늘의 가격 : 1000
sale()			# price = 500
print(price)	# 1000
```