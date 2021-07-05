while True:
    word = input("문자열을 입력하세요: ")
    word_length = len(word)
    if not word_length:
        break
    elif 5 <= word_length <= 8:
        continue
    elif word_length < 5:
        result = "*" + word + "*"
    else:
        result = "$" + word + "$"
    print("유효한 입력 결과: ", result)
