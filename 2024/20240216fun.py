# 내장함수

# abs(x) : 절댓값
print ( abs(3) )     # 3
print ( abs(-3) )    # 3
print ( abs(-1.2) )  # 1.2

# all(x) : 의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴
print( all([1, 2, 3]) )    # True
print( all([1, 2, 3, 0]) ) # False
print( all([]) )           # True

# any(x) : x의 요소 중 하나라도 참이 있으면 True를 리턴하고 x가 모두 거짓일 때만 False를 리턴
print( any([1, 2, 3, 0]) ) # True
print( any([0,""]) )       # False
print( any([]) )           # False

# chr(i) : 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수
print( chr(97) )
print( chr(44032) )

# dir : 객체가 지닌 변수나 함수를 보여 주는 함수
print( dir([1, 2, 3]) )
print( dir({'1':'a'}) )

# divmod : divmod(a,b) a를 b로 나눈 몫가 나머지를 튜플로 리턴
print( divmod(7,3) ) # (2, 1)
print( 7 // 3 )      # 2 
print( 7 % 3 )       # 1

# enumerate : 함수는 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는  enumerate 객체를 리턴
#              보통 enumerate 함수는 for 문과 함께 사용

for i, name in enumerate(['body','foo','bar']):
    print(i, name)

'''
0 body
1 foo
2 bar
'''

# eval : 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값
print( eval('1+2') )           # 3
print( eval("'hi'+'a'"))       # 'hia'
print( eval( 'divmod(4,3)') )  # (1,1)

# filter(함수, 반복_가능한_데이터)
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
        
    return result

print( positive([1,-3,2,0,-5,6]) ) # [1, 2, 6]

def positive(x):
    return x > 0

print( list(filter(positive, [1, -3, 2, 0, -5, 6])) )

print( list(filter(lambda x:x>0,[1,-3,2,0,-5,6])) )

# hex(X) : 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수
print( hex(234) )

# id(object) :  객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수
a = 3
print(id(3))
print(id(a))

# input : input([prompt])는 사용자 입력을 받는 함수
a = input("Enter:")

# int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수
print( int('3') )
print( int('11',2) )  # 2진수를 10진수로
print( int('1A',16) ) # 16진수를 10진수로  

# isinstance : isinstance(object, class) 함수는 첫 번째 인수로 객체, 두 번째 인수로 클래스
class Person : pass

a = Person()
print( isinstance(a, Person) )

# len(s) : 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수 
print( len("python") )
print( len([1,2,3,4]) )
print( len((1,'a')) )

# list : list(literable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수
print( list("python") )
print( list((1,2)))
# list 함수에 리스트를 입력하면 똑같은 리스트를 복사
a = [1,2,3]
b = list(a)
print(b)

# map(f, iterable): 함수(f)와 반복 가능한 데이터를 입력으로 받는다. map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print('result =',result)

def two_times(x):
    return x*2
result2 = list(map(two_times,[1,2,3,4]))
print('result2=',result2)

result3 = list(map(lambda a: a*2, [1,2,3,4]))
print('result3=',result3)

# max(iterable) : 인수로 반복 가능한 데이터를 입력받아 그 최댓값 리턴하는 함수
print( max([1,2,3]) )
print( max("python") )

# min (iterable) : max 함수와 반대로, 인수로 반복 가능한 데이터를 입력받아 그 최솟값을 리턴하는 함수
print( min([1,2,3]) ) 
print( min("python") )

# oct(X): 정수를 8진수 문자열로 바꾸어 리턴하는 함수
print(oct(12345))

# open(filename, [mode]) : ‘파일 이름’과 ‘읽기 방법’을 입력받아 파일 객체를 리턴하는 함수 
'''
w - 쓰기모드로 파일 열기
r - 일기모드로 파일 열기
a - 추가 모드로 파일 열기
b -  바이너리 모드로 파일 열기
'''
f = open("test.txt", "rb")
f.close()

# ord(c) : 문자의 유니코드 숫자 값을 리턴하는 함수
print( ord('가') )

# pow(x,y): x를 y를 제곱한 결괏값을 리턴하는 함수
print( pow(2, 4) )

# range([start,] stop [,step]) : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴
# 인수가 하나일 경우
print( list(range(5)) )
# 인수가 2개일 경우
print( list(range(5,10)) )
# 인수가 3개일 경우 : 세 번째 인수는 숫자 사이의 거리
print( list(range(1,10,2)) )

# round(number [,ndigits]) : 숫자를 입력받아 반올림해 린턴하는 함수
print( round(4.6 ) )     # 5
print( round(4.2) )      # 4
print( round(5.678, 2) ) #5.68

# sorted(iterable) : 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수 
print( sorted([3,1,2]) )

# str(object) : 문자열 형태로 객체를 변환하여 리턴하는 함수
print( str(3) )

# sum(iterable) : 입력 데이터의 합을 리턴하는 함수
print( sum([1,2,3]) )

# tuple(iterable)
print (tuple("abc"))

# type(object) : 입력값으 ㅣ자료형이 무엇인지 알려 주는 함수
print( type("abc"))
print( type( open("test.txt",'w')) )

# zip(*iterable): 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수
print( list( zip([1,2,3],[4,5,6]) ) )
print( list(zip([1,2,3],[4,5,6],[7,8,9])) )