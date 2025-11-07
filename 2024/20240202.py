#불 자료형
'''
불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형
 - True  : 참을 의미한다.
 - False : 거짓을 의미한다.
'''

a = True
b = False

print(type(a))
print(type(b))
#type(x)는 x의 자료형을 확인하는 파이썬의 내장 함수

print(1==1)
print(2>1)
print(2<1)

a = [1,2,3,4]
while a:
    print(a.pop())

'''
while 조건문:
    수행할_문장
'''

if []:
    print("참")
else:
    print("거짓")

print(bool('python'))

#변수란?
a = [1, 2, 3]
print(id(a)) #2424648489152
b = a
print(id(b)) #2424648489152

print(a is b)  # a와 b가 가리키는 객체가 같을까?

a[1] = 4
print(a) #[1, 4, 3]
print(b) #[1, 4, 3]

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a) #[1, 4, 3]
print(b) #[1, 2, 3]
print (b is a)

from copy import copy
a = [1,2,3]
b = copy(a)
print (b is a)
b=a.copy()
print(a is b)

#변수를 만드는 여러가지 방법
a, b = ('python','life')
print(a,b)

(c,d)= 'Python','life'
print(c,d)

[a,b] = ['python','life']
print([a,b])

a=b='veronica'
print(a,b)