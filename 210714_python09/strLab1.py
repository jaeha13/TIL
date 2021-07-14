def myemail_info(mail_address):
    if '@' not in mail_address:
        return None
    result = tuple(mail_address.split('@'))
    return result


print(myemail_info("asdfhanmail.net"))
print(myemail_info("qwer@hanmail.net"))
print(myemail_info("zxcv23@gmail.com"))
