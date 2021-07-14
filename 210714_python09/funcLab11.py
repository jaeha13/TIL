def mydict(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        my_dict["my" + str(k)] = v
    return my_dict


print(mydict())
print(mydict(one='1', two='2', three='3', four='4'))
