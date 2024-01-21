#개요
print('Hello world')
print('Hello, python')

a = 1 + 2 # 더하기
print(a,'입니다.')

#들여쓰기
if a==10:
    print(a,'입니다.')
else:
    print(a,'입니다.')
    
#숫자 계산하기 그리고 변수선언
b=0
print(b)

b=1+1
print(b)

b=1-2
print(b)

b=2*2
print(b)

b=4/2
print(b)

b=5//2 #버림나눗셈(floor division)
print(b) 

b=5%2 #나눗셈 후 나머지 구하는 % 연산자
print(b)
b=2**10 #거듭제곱을 구하는 ** 연산자
print(b)

#값을 정수로 만들기
#int는 정수(integer)를 뜻하며 값을 정수로 만들어 줌.
b=int(3.3)
print(b)

#객체의 자료형 알아내기
#type(값)
print(type(10))
