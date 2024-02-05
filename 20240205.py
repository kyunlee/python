#if문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

'''
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
else:
    수행할_문장A
    수행할_문장B
    ...
'''

#조건문이란 무엇인가?
#if 조건문에서 '조건문'이란 참과 거짓을 판단하는 문장을 말함

money = True
if money:
    print('money=',money)

#비교연산자
    
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

money = 2000

if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# and, or, not
'''
x  or y - x와 y 둘 중 하나만 참이어도 참
x and y - x와 y 모두 참이어야 참
not x   -x가 거짓이면 참
'''
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# in, not in
'''
  in              not in
x in 리스트     x not in 리스트
X in 튜플       x not in 튜플
x in 문자열     x not in 문자열
'''
print( 1 in [1, 2, 3] )
print( 1 not in [1, 2, 3] )

print( 'a' in ('a','b','c') )
print( 'j' not in 'python' )

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#조건문에서 아무 일도 하지 않게 설정하고 싶다면?
poket = ['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#다양한 조건을 판단하는 elif
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

# 위 예시를 elif를 사용하면
'''
if 조건문:
    수행할_문장1 
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else:
   수행할_문장1
   수행할_문장2
   ... 
'''
#if문을 한 줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

if 'money' in poket:pass
else: print("카드를 꺼내라")

#조건부 표현식
#score가 60 이상일 경우 message에 문자열 "success",
#아닐 경우에는 문자열 "failure"를 대입하는 코드이다.

score = 65

if score >= 60:
    message = "success"
else:
    message = "failure"

print('message1=',message)

message = "success" if score >= 60 else "failure"
print('message2=',message)

#변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
#조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.
