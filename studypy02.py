#2024.01.22
#자료형의 종류
a = 1             # 정수형 자료 -> integer
b = 2.0           # 실수형 자료 -> float
c = "안녕하세요"   # 문자형 -> string
d = [1,2,3,4,5]   # 리스트 자료 -> list 
e = (6,7,8)       # 튜플 자료 -> tuple
f = {9,10,11}     # 세트 자료 -> set
g = { 1:"참", 2:"거짓"} # 딕셔너리 자료 -> dictionary

print(a,b,c,d,e,f,g)

a = "Hello World"
b = [1,2,[5,6,7]]
print(a[0])

b = [1,2,[a,b,c]]

#문자열
multiline = "Life is too short\nYou need python"
print(multiline)

multiline='''
Life is too short
You need python
'''
print(multiline)

head = "python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a*2)

print("=" * 50)
print("My Program")
print("=" * 50)

a =  "Life is too short"
print(len(a))

a = "Life is too short, You need Python"
print( a[19:]) #You need Python
print( a[:17]) #Life is too short
print( a[:] )  #Life is too short, You need Python
print( a[19:-7] ) #You need
 