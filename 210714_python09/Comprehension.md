# 리스트 컴프리헨션(List Comprehension)

> `지능형 리스트` 라고도 함
>
> **[값에 대한 수식 for 변수 in 대상(Sequence) if 조건]**

```python
nums1 = []
for n in range(1, 11):
    nums.append(n * 2)

# 결과
nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 동일 결과 list comprehension
nums2 = [n * 2 for n in range(1, 11)]	# nums1 == nums2
```

### 조건식 if 만 사용

* for 문이 앞에 위치!

```python
lst = [i * i for i in range(10) if i % 2]
# 0 ~ 9까지의 숫자 중 홀수이면 제곱하여 lst의 원소로!!
```

### 조건식 if-else 같이 사용

* for 문이 뒤에 위치!

```python
result = [i if i % 2 == 0 else 10 for i in range(10)]
# if 가 참이면 앞의 값, 거짓이면 else 뒤의 값을 취함
```



# 사전 컴프리헨션(Dictionary Comprehension)

> `지능형 사전` 이라고도 함
>
> **{키와 값에 대한 수식 for 변수 in 대상 if 조건}**

```python
score_dict = {t[0]:t[1] for t in score_tuples}
# tuple의 첫번째 원소는 key, 두번째 원소는 value로 하겠다!!

score_dict = {k : v for k, v in score_tuples}

score_dict = {k : v for k, v in score_tuples if len(k) > 5}
```



# 집합 컴프리헨션(Set Comprehension)

> `지능형 집합` 이라고도 함
>
> {값에 대한 수식 for 변수 in 대상 if 조건}

```python
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

# 이중 for문 밖 -> 안
listv = [dan * num for dan in range(1, 10), for num in range(1, 10)]	# 모든 결과 다 나옴
setv = {dan * num for dan in range(1, 10) for num in range(1, 10)} # 중복된 애들은 제외됨!! - set의 특징
```



## 형식 정리

### 리스트

[값 표현식 for 요소 in 입력Sequence]

[값 표현식 for 요소 in 입력Sequence if 조건식]

[값 표현식(참) if 조건식 else 값 표현식(거짓) for 요소 in 입력Sequence]



### 집합

{값 표현식 for 요소 in 입력Sequence}

{값 표현식 for 요소 in 입력Sequence if 조건식}

{값 표현식(참) if 조건식 else 값 표현식(거짓) for 요소 in 입력Sequence}



### 사전

{키 표현식 : 값 표현식 for 요소 in 입력Sequence}

{키 표현식 : 값 표현식 for 요소 in 입력Sequence if 조건식}

{키 표현식 : 값 표현식(참) if 조건식 else 키 표현식 : 값 표현식(거짓) for 요소 in 입력Sequence}

