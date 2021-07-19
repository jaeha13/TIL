# 객체 지향 프로그래밍(OOP)

>OOP(Object Oriented Programming)
>
>프로그램에서 필요한 객체들의 역할을 정해 놓고 이 객체 안에 관련된 변수와 함수를 정의하여 객체 단위로 기능이 처리되도록 하는 프로그래밍 기법으로 **`재사용성`**이 좋은 컴퓨터 공학의 프로그래밍 기법 중 하나이다.

실 세계의 통념을 **추상화**하여 하나의 클래스로 정의

1. 만들고자 하는 프로그램에서 필요한 객체 찾기
2. 그 객체에 멤버들을 모델링(추상화) 하여 클래스 정의

### 클래스

> 하나의 통념
>
> 속성(변수) + 행동(함수)

* 모델링 - 사물을 분석하여 필요한 속성과 동작을 추출하는 것
* 캡슐화 - 모델링한 결과를 클래스로 포장

### 객체

> 클래스를 메모리할당하여 member들을 사용 가능한 상태로 만든것

#### 클래스 정의 방법

```python
class UserInfo:	# class 이름은 대문자로 시작할 것을 권장
    변수
    변수
    함수			# class 내부 함수 = method
    함수
    함수
```

#### 객체 생성 방법

> instance 생성 -> 각각 메모리에 id 값(주소값)을 할당 받음

```python
변수 = 클래스명()
```

#### 객체 사용 방법

```python
변수.멤버변수
변수.메서드
```

#### member없는 class 생성

당장은 member들을 정의할 생각은 없지만 객체가 필요한 경우 사용

```python
class Student:
    pass
```

## Method

> 함수와 같음!
>
> 단지, 객체를 통해서만 사용 가능

### 특수 메서드

> \__init__ : 초기화 메서드 -> 객체 호출시 만들어지는 초기화된 객체 생성
>
> \__del__ : 삭제 메서드 -> 프로그램 수행 끝나기 전에 미리 객체 삭제
>
> 프로그램 수행 끝나면 모든 객체는 자동 삭제 됨
>
> \__str__ : 객체를 문자열로 변화하는 특수 메소드

```python
class Student:
    def __init__(self):		# self: 변수 - id 참조값 저장
		print("인스턴스 생성!")
    def __del__(self):
		print("인스턴스 삭제!")
    def __str__(self):	# 따로 설정하지 않을 경우: object 클래스가 default 부모 클래스이므로 부모 클래스 내부 __str__ 사용!
        return "***객체를 문자열로 변환: 변환결과로 원하는 문자열***"
        
# class 호출은 마치 함수 호출과 마찬가지로 함 = class 내 __init__ 함수가 저절로 호출되어 생성!
st1 = Student()
st2 = Student()
st3 = Student()

print("[st1이 참조하고 있는 Student 인스턴스 삭제]")
del st1

print(st2)

print("종료")

# 실행 결과
인스턴스 생성!
인스턴스 생성!
인스턴스 생성!
[st1이 참조하고 있는 Student 인스턴스 삭제]
인스턴스 삭제!
***객체를 문자열로 변환: 변환결과로 원하는 문자열***
종료
인스턴스 삭제!	# 프로그램이 종료되면 자동으로 __del__ method 호출됨
인스턴스 삭제!
```

#### class 고유 변수 정의

```python
class Student:
    def __init__(self, name, age, subject):		# class 고유 변수 name, age, subject
        self.name = name	# instance의 name 변수에 name argument
        self.age = age
        self.subject = subject
```



### garbage

> 아무도 참조하고 있지 않지만 메모리 공간을 차지 하고 있는 경우

![Screenshot (24)](../images_file/Screenshot%20(24).png)

도우너, 또치 = garbage 즉, 사용은 안되는데 메모리 공간에는 존재

> cf+
>
> 모듈과 class는 같은 것인가??	**NO**
>
> 모듈에 class 가 포함됨 -> 모듈은 특정 목적을 위한 class와 함수들을 모아놓은 집합!!