# 7.1.1 메타문자 - 정규표현식에서 일정한 의미를 가지고 있는 특수 문자
# ※ 메타 문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다.
# . ^ $ * + ? { } [ ] \ | ( )

"""
.x 또는 x. : 임의의 한 문자가 x 앞이나 뒤에 오는 패턴 지정
^x : x로 시작하는 문자열
x$ : x로 끝나는 문자열
x* : x가 0번이상 반복
x+ : x가 1번이상 반복
x? : x가 0개 또는 1개 존재
abc|ABC : abc 또는 ABC 두개중 하나 선택
[x] : x문자 한개 일치
[^x] : x문자 제외
x{n} : x문자 n개 연속
x{n,} : x문자 n개 이상 연속
x{m,n} : x문자 ㅡ~n개 사이 연속
"""

import re # 정규표현식 모듈 - 방법1
from re import findall, match, sub  # - 방법2

st2 = 'test1abcABC 123mbc 45test'

# 접두어/접미어
print(findall('^test', st2))    # ^:접두어 - ['test']
print()
print(findall('st$', st2))  # $:접미어 - ['st']
print()

# 종료 문자 찾기 : abc, mbc
print(findall('.bc', st2))  # '.bc':bc로 끝나는 3자리 문자 ['abc', 'mbc']
print()

# 시작 문자 찾기
print(findall('t.', st2))   # 't.': t로 시작되는 2자리 문자 ['te', 't1', 'te']

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
print(st1)

print(findall('[가-힣]{1,}', st1))    # 이름 찾기 - ['홍길동', '이사도시']
print()
print(findall('[a-z]{3}', st1)) # ['abc']
print()
print(findall('[A-Z]{3}', st1)) # ['abc', 'ABC']
print()
print(findall('[a-z|A-Z]{3}', st1)) # ['abc', 'ABC']
print()

# 4. 단어 찾기(\\w) - 한글,영문,숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{2,}', st3) # '\\w{3,}:한글,영문,숫자가 3자리 이상인 문자열
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']

# 5. 문자열 제외 : x+(x가 1개 이상 반복)
print(findall('[^t]+', st3))    # [^t]:t 문자 제거 '[^t]+':t 반복 문자 제거 ['es', '^홍길동 abc 대한*민국 123$', 'bc']
print()

# 특수문자 제외
print(findall('[^^*$]+', st3))
