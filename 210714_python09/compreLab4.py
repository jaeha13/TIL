import random

lst = [random.randint(0, 100) for _ in range(10)]
pass_nonpass_dict = {k: "pass" if lst[k - 1] >= 60 else "nopass" for k in range(1, 11)}

print(lst)  # 확인을 위해서!!
print(pass_nonpass_dict)
