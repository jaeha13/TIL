# 파이썬 기본 타입

> type() 함수로 확인

* int

  ```python
  >>> type(10)
  <class 'int'>
  ```

* float

  ```python
  >>> type(3.4)
  <class 'float'>
  ```

* bool

  ```python
  >>> type(True)
  <class 'bool'>
  ```

* string

  ```python
  >>> type('10')
  <class 'str'>
  >>> type("")
  <class 'str'>
  
  # 숫자형과 문자열형 비교
  >>> 10 * 3
  30
  >>> '10' * 3
  '101010'
  ```

  * 불가능
    * 'I Say 'Help' to you'
    * "I Say "Help" to you"
  * 가능
    * 'I Say "Help" to you'
    * "I Say 'Help' to you"
    * "I Say \\"Help\\" to you"

  > 그래서 여러 행 주석을 """ 로 처리할 수 있다

  ```python
  """
  이렇게 여러 줄로 주석을 달고 싶을 경우
  큰 따옴표 3개를 이용하여 달 수 있다.
  """
  ```

  * 확장열(Escape Sequence)
    * \n : 개행(줄바꿈)
    * \t : 탭
    * \\" : 큰따옴표
    * \\\ : \문자

  ```python
  >>> print("abncdnef")
  abncdnef
  >>> print("ab\ncd\nef")
  ab
  cd
  ef
  >>> print("abcdef")
  abcdef
  >>> print("ab\tcd\tef")
  ab	cd	ef
  ```

  * 긴 문자열

    1. 계속 문자 \ 사용 -> 연속, 이어짐

    ```python
    >>> a = 'aaa\
    aaa\
    aaa'
    >>> a
    'aaaaaaaaa'
    ```

    2. 따옴표 3개 연속으로 사용 -> enter = 개행(\n)

    ```python
    >>> a = """aaa
    aaa
    aaa"""
    >>> a
    'aaa\naaa\naaa'
    >>> print(a)
    aaa
    aaa
    aaa
    ```

    3. 소괄호를 통해 가능 그러나, 튜플과 헷갈리므로 사용 x

       또, 해보니 닫는 괄호를 마지막에 써줘야 함.

    ```python
    >>> a = ("ai"
         "string"
         "why"
         )
    >>> a
    'aistringwhy'
    ```

  * 문자열 연산

    * \+ : 문자열을 연결

    * \* : 문자열을 정수 횟수만큼 반복

# 연산자

## 등가/비교 연산자

```python
v == v2		# (등가 연산자)v의 값과 v2의 값이 같은가?
v != v2		# v의 값과 v2의 값이 다른가?
<, >, <=, >= # 비교연산자(제어문에서 자주 사용)
```

## 대입 연산자

```python
v = 10
v = v2			# v2의 값을 v에 대입
v = 10 + 23		# 연산식의 결과값을 v에 대입
v = input("입력하소~")	# 함수를 통한 결과값을 v에 대입
```

## 산술 연산자

> 실수 vs 정수 ? 실수!!

* +, -, *, /
* ** 거듭제곱
* // 나누기 몫
* % 나누기 나머지

cf) \ : 백슬래시, / : 슬래시

> 문자열형 + 숫자형 -> error!!!! 다른 언어의 경우 자동 형변환 가능한 경우가 많음 그러나 파이썬은... 안됨

```python
>>> 'abc' + '100'
'abc100'
>>> 'abc' + 100
Traceback (most recent call last):
File "<pyshell#9>", line 1, in <module>
 'abc' + 100
TypeError: can only concatenate str (not "int") to str
```

> 형변환 함수
>
> * int() : 문자열, 실수형 -> 정수형
> * float() : 문자열, 정수형 -> 실수형
> * str() : 정수형, 실수형 -> 문자열
> * round() : 실수를 소수점 첫째 자리에서 반올림하여 정수 변환

## 복합 대입 연산자

* += : 좌변의 값에 우변의 값을 더함
* -= : 좌변의 값에 우변의 값을 뺌
* *= : 원래 값에 일정 값을 곱함
* /= : 원래 값에 일정 값을 나눔
* 그러나, ++, -- 없음!!

# 조건식

조건식 - 연산 결과가 bool 타입(True, False)이 되는 식
              비교연산자(==, != , >, <, >=, <=, ...)
              논리연산자(and, or, not)
              bool 타입으로 인식 가능한 변수 또는 리터럴

```python
if 조건식:
    코드블럭

# 숫자 : 0이 아니면 True
# 문자열 : 비어 있지 않은 상태면(""가 아니면) True
# 리스트, 튜플, 딕셔너리 : 비어 있지 않은 상태면(빈상태가 아니면) True
if True :
flag = True
if flag == True:
if flag:
```

```python
# 비교식1 and 비교식2 and 비교식3 ... => 모두 다 참이면
# 비교식1 or 비교식2 or 비교식3 ... => 그 중 하나라도 참이면
# not 비교식 => 이 비교식의 결과가 거짓이면
if 비교식:		#참일 경우 수행시키고자 함
    xxxxx

if not 비교식:	#거짓일 경우 수행시키고자 함
    xxxxx
```

