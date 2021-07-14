def mycompredict(**kwargs):
    my_dict = {f"my{k}": v for k, v in kwargs.items()}
    return my_dict


print(mycompredict())
print(mycompredict(one='1', two='2', three='3', four='4'))
