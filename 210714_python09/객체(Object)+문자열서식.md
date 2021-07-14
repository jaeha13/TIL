# 객체(Object)

## 객체의 멤버

> . 연산자를 사용하여 사용!!

### 속성(Field)

= 객체를 구성하는 변수(`상태`)

### 함수(Method)

= 객체 고유 함수(`동작`)



## 문자열

### 포맷팅

> 문자열 사이사이에 다른 정보 삽입하여 조립하는 기법
>
> format % value

```python
price = 500
print("궁금하면" + str(price) + "원!")

print("궁금하면 %d원!" % price)
```

* %d : 정수
* %f : 실수
* %s : 문자열
* %c : 문자하나
* %h : 16진수
* %o : 8진수
* %%: %문자

여러 값을 한번에 하려면 => tuple로 packing

```python
day = 14
mon = 7
year = 2021
print("오늘은 %d년 %월 %일입니다." % (year, mon, day))
```

서식

* %[-]폭[.유효자리수] 서식

  ```python
  price = [30, 13500, 2000]
  for p in price:
      print("가격: %d원" % p)
      
  # 실행 결과
  가격: 30원
  가격: 13500원
  가격: 2000원
  
  for p in price:
      print("가격: %7d원" % p)	# 7자리 오른쪽정렬
  
  # 실행 결과
  가격:      30원
  가격:   13500원
  가격:    2000원
  ```

* \- 를 사용하면 왼쪽정렬

  ```python
  price = [30, 13500, 2000]
  for p in price:
      print("가격: %-7d원" % p)	# 7자리 왼쪽정렬
      
  # 실행 결과
  가격: 30     원
  가격: 13500  원
  가격: 2000   원
  ```

* . 기호로 소수점 이하 표시 자리수 설정

  ```python
  pie = 3.14159265
  print("%10f" % pie)		# 10자리 + 소수점은 default = 6자리!!
  print("%10.8f" % pie)	# 10자리 + 소수점은 8자리 => 소수점 9자리에서 반올림
  print("%10.5f" % pie)	# 10자리 + 소수점은 5자리
  print("%10.2f" % pie)	# 10자리 + 소수점은 2자리
  
  # 실행 결과
    3.141593
  3.14159265
     3.14159
        3.14
  ```

### 5가지 방법

```python
# 1
print(stname + "학생은 나이가 " + str(age) + "이고 평균은 " + str(stavg) + "입니다.")
# 2
print(stname, "학생은 나이가 ", stage, "이고 평균은 ", stavg, "입니다.", sep="")
# 3
print("%s학생은 나이가 %d이고 평균은 %.2f입니다." % (stname, stage, stavg))
# 4
print("{}학생은 나이가 {}이고 평균은 {:.2f}입니다.".format(stname, stage, stavg))
# 5
print(f"{stname}학생은 나이가 {stage}이고 평균은 {stavg:.2f}입니다.")
```

