# 반복문(for)

```python
# range(시작, 끝 + 1, 증가치) => default = range(0, 끝 + 1, 1)
# range(11) --> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# range(1, 11) --> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# range(1, 11, 2) --> 1, 3, 5, 7, 9
sum_value = 0
for value in range(1, 101, 1):
    sum_value = sum_value + value
print(sum_value)
```

```python
# _(언더바)  : i  변수를 사용하지 않을 경우 _(언더바) 사용 가능!!
for _ in range(0, 3, 1):
     print("안녕하세요? for 문을 공부 중입니다.^^")

# i 변수 사용할 경우,
for i in range(0, 3, 1):
     print(i, ": 안녕하세요? for 문을 공부 중입니다.^^")

# i 변수 + 포맷 문자 사용할 경우,
for i in range(0, 3, 1):
    print("%d : 안녕하세요? for 문을 공부 중입니다.^^" %i)
              - 포맷문자
```

> 10, 15, 3, 8, 1
> max_value = 10 -> 15
> min_value = 10 -> 3 -> 1

```python
# <1>
for x in range(1, 51):          # 1 ~ 50
    if (x % 10) == 0:           # 10의 배수이면
        print('+', end='')      # + 출력
    else:                       # 아니면
        print('-', end='')      # - 출력
print()     # enter
print()     # enter
=> ---------+---------+---------+---------+---------+
=>
=>

# <2>
for x in range(1, 6):           # 1 ~ 5
    print('-' * 9, end='')      # ---------
    print('+', end='')            # +
print('\n')
=> ---------+---------+---------+---------+---------+
=>
=>

# <3>
for x in range(1, 51):          # 1 ~ 50
    if (x % 5) == 0:            # 5의 배수이면
        print('+', end='')      # + 출력
    else:                       # 아니면
        print('-', end='')      # - 출력
print('\n\n')   # enter * 3
=> ----+----+----+----+----+----+----+----+----+----+
=>
=>
=>

# <4>
for x in range(1, 51):          # 1 ~ 50
    if (x % 10) == 5:           # 일의 자리가 5이면
        print('+', end='')      # + 출력
    else:                       # 아니면
        print('-', end='')      # - 출력
=> ----+---------+---------+---------+---------+-----
```

