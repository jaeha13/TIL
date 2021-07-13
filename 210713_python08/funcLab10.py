def sumAll(*nums):
    int_check = False
    sum = 0
    for i in nums:
        if type(i) == int:
            sum += i
            int_check = True
    if len(nums) == 0 or not int_check:
        return None
    return sum


print(sumAll())
print(sumAll(0))
print(sumAll('1', '2', 3, 4, 5))
print(sumAll(1.8, 2, '8', 'str', 3))
print(sumAll(1, 2, 3, 4, 5, 6, 7))
