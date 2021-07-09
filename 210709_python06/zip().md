## zip()

`zip()` 함수는 여러개의 순회 가능한 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근. `iterator`를 반환

```python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)
    
# 실행
(1, 'A')
(2, 'B')
(3, 'C')
```

> zip 파일처럼 하나로 묶어준다고 생각하면 될 듯
>
> => 각 원소에서 하나 하나 떼서 튜플로 묶음!!!

```python
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
    
# 실행
1 A a
2 B b
3 C c
4 D d
5 E e
```

> 반드시 묶음으로 해야하는 것은 아님!!