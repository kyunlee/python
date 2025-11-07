# 04장 파이썬으 입출력
# 04-1 함수
# 함수란 무엇인가?
# 함수를 사용하는 이유는 무엇일까?

# 파이썬 함수의 구조
'''
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2
    ...
'''

def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b) # add(3,4)의 리턴값을 c에 대입
print(c)

# 매개변수(parameter)와 인수(arguments)
def add(a, b): # a, b는 매개변수: 함수에 입력으로 전달된 값을 받는 변수
    return a+b
print(add(3,4)) # 3, 4는 인수: 함수를 호출할 때 전달하는 입력값을 의미

# 입력값과 리턴값에 따른 함수의 형태

# 1.일반적인 함수 : 입력값이 있고 리턴값이 있는 함수가 일반적인 함수
'''
def 함수_이름(매개변수)
    수행할_문장
    ...
    return 리턴값
'''

def add(a,b):
    result = a + b
    return result

a = add(3,4)
print(a)

# 리턴값을_받을_변수 = 함수_이름(입력_인수1, 입력_인수2, ..)

# 2.입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)
# 리턴값을_받을_변수 = 함수_이름()

# 3.리턴값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

add(3,4) 
#함수_이름(입력_인수1, 입력_인수2, ...)

a = add(3,4)
print(a) # None

# 4.입력값도, 리턴값도 없는 함수
def say():
    print('Hi')

say()
#함수_이름()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result =  sub(a=7, b=3) # a에 7, b에 3을 전달
print(result)

result = sub(b=5, a=3) # b에, a에 3을 전달
print(result)

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
'''
def 함수_이름(*매개변수):
    수행할_문장
'''

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값을 더한다.
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul": # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) 
print_kwargs(name='foo', age=3)

# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result) # (7, 12)

result1, result2 = add_and_mul(3, 4)
print(result1, result2) # 7 12

# return의 또 다른 쓰임새

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('바보')

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a) # 1
# 매개변수는 함수 안에서만 사용하는 ‘함수만의 변수’이기 때문
# 즉, def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관없다는 뜻

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
# vartest_return.py
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
# vartest_global.py
a = 1
def vartest():
    global a
    a = a+1
    
vartest()
print(a)

# lambda 예약어
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식

add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a,b):
    return a+b

result = add(3,4)
print(result)