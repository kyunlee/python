#문자열 포매팅
#숫자대입
print("I eat %d apples." % 3)
#문자열대입
print("I eat %s apples." % "five")
#숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." %number)
#2개 이상의 값 넣기
number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days." % (number,day))

#포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
print("Error is %d%%." % 98)

#정렬과 공백
print("%10s" % "hi")      #         hi
print("%-10sjane." %'hi') #hi        jane.
#hi를 왼쪽으로 정렬하고 나머지는 공백으로 채웠다는 것을 알 수 있다.

#소수점 표현하기
print("%0.4f" % 3.42134234)  #3.4213
print("%10.4f" % 3.42134234) #    3.4213

#format 함수를 사용한 포매팅
print("I eat {0} apples." .format(3))
print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples" .format(number))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))

print("I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days." .format(10,day=3))

#f 문자열 포매팅 
#파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용가능
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

#표현식이란 중괄호 안의 변수를 계산식과 함께 사용하는 것
print(f'나는 내년이면 {age +1}살이 된다.')

#딕셔너리는 f문자열 포매팅에서 사용가능
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

#왼쪽정렬
print("{0:<10}" .format("hi"))
print(f'{"hi":<10}')

#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞춤

#오른쪽정렬
print("{0:>10}".format("hi"))
print(f'{"hi":>10}')

#오른쪽 정렬은 :< 대신 :>을 사용하면 됨.
#화살표의 방향을 생각하면 어느 쪽으로 정렬되는지 알수 있음.
#가운데 정렬
print("{0:^10}".format("hi"))
print(f'{"hi":^10}')

#출력결과
'''
hi
hi
        hi
        hi
    hi
    hi
'''

#공백 채우기
print("{0:=^10}" .format("hi")) #====hi====

print("{0:!<10}" .format("hi")) #hi!!!!!!!!
print("{0:!>10}" .format("hi")) #!!!!!!!!hi

#소수점표현하기
y=3.42134234
print("{0:0.4f}" .format(y))
print("{0:10.4f}".format(y))

#{ 또는 } 문자 표현하기
print("{{ and }}" .format())


#문자열 관련 함수들
#문자 개수 세기 - count
a = "hobby"
print(a.count('b'))

#위치 알려 주기1 - find
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) #찾는 문자나 문자열이 존재하지 않는다면 -1을 반환

#위치 알려 주기2 - index
a = "Life is too short"
print(a.index('t')) 

#find 와 index 의 차이? 
#find는 찾는문자 없으면 -1반환
#index는 찾는문자 없으면 오류

#문자열 삽입 - join
print("," .join('abcd'))

print("," .join(['a','b','c','d'])) # a,b,c,d
print(['a','b','c','d'])            # ['a', 'b', 'c', 'd']

#소문자를 대문자로 바꾸기 - upper
a = "hi"
print(a.upper())

#대문자를 소문자로 바꾸기 - lower
a = "HI"
print(a.lower())

#왼쪽 공백 지우기 - lstrip
a = " hi "
print(a.lstrip())

#오른쪽 공배 지우기 - rstrip
a = " hi "
print(a.rstrip())

#양쪽 공배 직우기 - strip
a = " hi "
print(a.strip())

#문자열 바꾸기 - replace
a = "Life is too short"
print(a.replace("Life","Your leg"))
a.replace("Life","Your leg")
print(a)


#문자열 나누기 - split
a = "Life is too short"
print(a.split())
b="a:b:c:d"
print(b.split(":"))
