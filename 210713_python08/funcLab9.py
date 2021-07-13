def sumEven1(*nums):    # tuple 로 packing 되어 들어감!!
    even_sum = 0
    if len(nums) >= 1:
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        return even_sum
    else:
        return -1


print(sumEven1())
print(sumEven1(0))
print(sumEven1(1, 3, 5, 7, 9))
print(sumEven1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
