# 상속

> 기존 클래스 확장하여 멤버 추가하거나 동작 변경
>
> ```python
> class ClassName(부모 ClassName):
>     ...
> ```
>
> 부모클래스를 지정하지 않는 경우, 
> 자동으로 `Object` class가 부모

```python
class Human:
    def __init__(self, age, name):
		self.age = age
        self.name = name
    def intro(self):
        print(f"{self.age}살 {self.name}입니다.")
        
class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum
    def intro(self):
        super().intro()
        print(f"학번: {self.stunum}")
    def study(self):
        print("하늘 천 따 지 검을 현 누를 황")
```

**super() 메서드**

* 자식 클래스에서 부모의 메서드 호출할 때 사용

## 메서드 오버라이딩 vs 오버로딩

> **오버라이딩**
> 상속받은 메서드를 재정의해서 사용
>
> **오버로딩**
> 같은 이름의 메서드 여러개 => 다른 타입에 대해 같은 기능을 하도록 만든 것



# Class member 변수

```python
class Test:
    클래스 변수
    인스턴스 변수
    
o1 = Test()
o2 = Test()
```

## 클래스 변수

모든 인스턴스가 하나의 저장공간을 공유하여 항상 공통된 값을 갖는 변수

> 트럼프 카드의 폭/높이 변수
>
> 모든 카드 객체가 공동으로 한 메모리 영역을 사용하는 변수

#### [클래스 변수 접근]

* Test.클래스 변수	(**권장**)
* o1.클래스 변수
* o2.클래스 변수

## 인스턴스 변수

인스턴스가 생성될 때마다 생성되어 인스턴스마다 각기 다른 값을 유지하는 변수

> 트럼프 카드의 무늬/숫자 변수
>
> 카드객체가 만들어질때마다 각각 메모리 영역에 할당되는 변수

#### [인스턴스 변수 접근]

* o1.인스턴스 변수
* o2.인스턴스 변수



## 클래스 메서드

특정 객체에 대한 작업을 처리하는 것이 아니라 클래스 전체에 공유
`객체 생성에 관계없이 클래스이름으로 호출이 가능`한 메서드

> @classmethod 데커레이터를 사용해서 정의
> 첫번째 인수로 클래스에 해당하는 cls 인수를 정의

```python
class Car:
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
		print(cls.count)

pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()
```



