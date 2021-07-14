# 1
s1 = "pythonjavascript"
print(len(s1))
# 2
s2 = "010-7777-9999"
print(*s2.split('-'), sep="")
# 3
s3 = "PYTHON"
print(s3[::-1])
# 4
s4 = "Python"
print(s4.lower())
# 5
s5 = "https://www.python.org/"
i = s5.find('w')
print(s5[i:-1])
# 6
s6 = '891022-2473837'
print("남성" if s6[7] == 1 or s6[7] == 3 else "여성")
# 7
s7 = '100'
print(int(s7), float(s7), sep=", ")
# 8
s8 = 'The Zen of Python'
print(s8.count('n'))
# 9
print(s8.find('Z'))
# 10
lower = s8.lower().split(" ")
UPPER = s8.upper().split(" ")
total = lower + UPPER
print(lower, UPPER, total)
