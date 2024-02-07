# Day1 
# 1.문자열 출력하기
# 입력문자 HelloWorld!
# str = input()
str = "HelloWorld!"
str = input()
print(str)

# 다른사람풀이
print(input())

# 2.a와 b 출력하기
# a, b = map(int, input().strip().split(' '))
a, b = 4, 5
print('a =', a)
print('b =', b)

# 다른사람풀이
print(f"a = {a}\nb = {b}")

# 3.문자열 반복해서 출력하기
# a, b = input().strip().split(' ')
a, b = 'string', 5
b = int(b)

print(a*b)

# 4.대소문자 바꿔서 출력하기 
#    aBcDeFg
# -> AbCdEfG
# str = input()

str = 'aBcDeFg'
aaa = ''
i=0
while i < len(str):
    if str[i].isupper() == True:
        aaa +=str[i].lower()
    elif str[i].islower() == True:
        aaa +=str[i].upper()
    i = i+1
print('aaa=',aaa)

# 다른사람풀이
print(str.swapcase())
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))

import string
str = input()
for i in str:
    if i.isupper():
        print(i.lower(), end='')
    if i.islower():
        print(i.upper(), end='')

# 5. 특수문자 출력하기
# !@#$%^&*(\'"<>?:;
print( '''!@#$%^&*(\\'"<>?:;''' )

#다른사람풀이
print(r'!@#$%^&*(\'"<>?:;')
#raw 를 의미하는 r로, regex 에서 pattern 설정 시 escape 문자를 많이 써야해서 자주 사용
print('\u0021\u0040\u0023\u0024\u0025\u005e\u0026\u002a\u0028\u005c\u0027\u0022\u003c\u003e\u003f\u003a\u003b')