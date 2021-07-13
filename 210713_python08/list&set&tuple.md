# list

변수에 의미있는 이름 지정!!

```python
# index => i
# data => d
```

### 이중 리스트(2차원 리스트)

> 리스트의 요소로 리스트를 넣어 중첩한 경우
>
> => 이중 리스트 순회하여 최종 값을 읽으려면 loop도 이중으로 하여야 함

```python
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


"""
# 3x3 matric라고 생각할 수 있음!
lst1:	1	2	3	# lst1[0]	1행 리스트
		4	5	6	# lst1[1]	2행 리스트
		7	8	9	# lst1[2]	3행 리스트
		
# 각 행의 열 수는 다를 수 있음
lst2:	1	2	3
		4	5
		6	7	8	9
lst2[0][2] = 3 	# 1행 3열 value
lst2[행][열]
"""

for row in lst1:			# 이중 리스트의 행 리스트
    for col in row:			# 각 행의 열 리스트
        print(item, end=' ')
    print()
```

> list를 하나의 요소로 생각

```python
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

print(len(lst1))	# lst1의 요소 개수(행의 개수) : 3
print(len(lst2))	# lst2의 요소 개수(행의 개수) : 3
print(len(lst1[0]))	# lst1의 1 행 요소 개수(1 행의 열의 개수) : 3
print(len(lst2[1]))	# lst2의 2 행 요소 개수(2 행의 열의 개수) : 2
```



# set

> 중괄호를 사용하여 생성 or set() 함수 사용

```python
set1 = {1, 2, 3, 4, 5, ...}
# set1 = {} 불가능!!!
# 빈 set을 만들고 싶으면 set() 함수 사용
# why? dict 때문에!!! dictionary가 우선이라 set = {}라 하면 set이라는 딕셔너리가 만들어지는 것 

"""
lst = [1, 2, 3, 4, 5, ...]
# lst = [] or list()

tup = (1, 2, 3, 4, 5, ...)
# tup = () 그런데 굳이 빈 튜플을 만들 일은 없다!! why? 변경할 수 없음

dic = {k1 : v1, k2 : v2, k3 : v3, ...}
# dic = {}
"""
```

* set은 중복되는 요소 X

* set() 함수로 만들기 위해서는 tuple이나 list 형식으로 전달

* 저장된 순서와 상관없음

  ```python
  a = set()
  b = set([1, 2, 3, 3, 4])
  c = {1, 4, 5, 6, 1, 4}
  d = set([1, 2, 'Pen', 'Cap', 'Plate'])
  e = set((10,))	# , : 앞으로 더 들어갈거야!!!
  f = {100,}
  g = set([1, 2, 3, 4, 5, ])
  
  print(a)	# set()
  print(b)	# {1, 2, 3, 4} - 중복 용납 못하지!!
  print(c)	# {1, 4, 5, 6}
  print(d)	# {1, 2, 'Pen', 'Plate', 'Cap'} - 저장된 순서 무시!!
  print(e)	# {10}
  print(f)	# {100}
  print(g)	# {1, 2, 3, 4, 5}
  ```

### method

* add

  ```python
  s1 = set()
  
  s1.add(10); s1.add(20); s1.add(30); s1.add(40); s1.add(50)
  print(s1)	# {40, 10, 50, 20, 30}
  
  s1.add(10)
  print(s1)	# {40, 10, 50, 20, 30} why? 이미 있으니까 X
  ```

* update

  ```python
  s1.update([40,50,60,70])
  print(s1)	# {70, 40, 10, 50, 20, 60, 30}
  ```

* remove

  ```python
  s1.remove(30)
  print(s1)	# {70, 40, 10, 50, 20, 60}
  print(len(s1))	# 6
  ```

### set 집합연산

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1, s2)	# {1, 2, 3, 4, 5, 6} {4, 5, 6, 7, 8, 9}

print(s1 & s2)	# {4, 5, 6} => & : intersect
print(s1 | s2)	# {1, 2, 3, 4, 5, 6, 7, 8, 9} => | : union
print(s1 - s2)	# {1, 2, 3} => - : difference
print(s1 ^ s2)	# {1, 2, 3, 7, 8, 9} => ^ : exclusive
```

# tuple(튜플)

> 기본적으로 immutable한 list라고 생각하면 됨
>
> => **Only READ**

* 기본적으로 변수 하나에 값이 여러개 할당된 경우 => tuple로 packing 됨!!

  ```python
  tuple_test = 10, 20, 30, 40
  
  print(tuple_test)	# (10, 20, 30, 40)
  print(type(tuple_test))	# <class 'tuple'>
  ```

