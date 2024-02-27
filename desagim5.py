# 되새김문제 5장

# 1.클래스 상속받고 메서드 추가하기 1
# 다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val 

# 이 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자
# 즉, 다음과 같이 동작하는 클래스를 만들어야 한다.
# class 클래스_이름(상속할_클래스_이름)
    
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print( cal.value )

# 2.클래스 상속받고 메서드 추가하기 2
# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimiCalculator 클래스를 만들어보자
# 단, 반드시 위과 같은 Calculator 클래스를 상속해서 만들어야한다.   

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value  > 100:
            self.value = 100


# 즉, 다음과 같이 동작해야 한다.
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print( cal.value )

# 3.참과 거짓 예측하기
all( [1, 2, abs(-3)-3] ) # False
print(all( [1, 2, abs(-3)-3] ) )

# chr(ord('a')) == 'a' # True
print (ord('a') )      # 유니코드 숫자 값을 리턴하는 함수
print (chr(ord('a')))  # 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수

# 4.음수 제거하기
# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]
result = list(filter(lambda x : x>0 , [1, -2, 3, -5, 8, -3] ) )
print(result)

# 5.16진수를 10진수로 변경하기
# hex(234) : 0xea
print( int('0xea',16 ) )

# 6.리스트 항목마다 3곱하여 리턴하기
# map과 lambda를 사용하여 [1,2,3,4] 리스트의 각 요소값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

result2=  list(map(lambda x: x*3, [1,2,3,4]))
print(result2)

# 7.최댓값과 최솟값의 합
# 다음 리스트의 최댓값과 최솟값의 합을 구해 보자
# [-8, 2, 7, 5, -3, 5, 0, 1]

import functools
data = [-8, 2, 7, 5, -3, 5, 0, 1]
'''
max_num = functools.reduce(lambda x, y: x if x > y else y,data)
max_min = functools.reduce(lambda x, y: x if x < y else y,data)
print( max_num+max_min )
'''
print( max(data)+min(data) )

# 8. 수점반올림하기
print ( round(17/3, 4) )

# 9. 디레터리 이동하고 파일 목록 출력하기
'''
os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해보자
'''
import os
# 1. C:\doit 디렉터리로 이동한다
#os.chdir("C:\doit")

# 2. dir 명령을 실행하고 그 결과를 변수에 담는다.
f = os.popen("dir")

# 3. dir 명령의 결과를 출력한다.
print(f.read())

# 10. 파일 확장자가 .py인 파일만 찾기
# glob모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해보자.
import glob
print( glob.glob("C:\doit\*.py") )

# 11. 날짜표시하기
# time 모듈 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32

import time
print( time.strftime("%Y/%m/%d %X") ) 
print( time.strftime("%Y/%m/%d %H:%M:%S") ) 

# 12.로또번호생성하기
# random 모듈을 사용하여 로또번호(1~45 사이의 숫자 6개)를 생성해보자(단, 중복된 숫자가 있으면 안됨.)

import random

lotto= random.sample(range(1,46),6)

print('lotto=',lotto)

# random 모듈의 randint를 사용하여 다음과 같이 작성 
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)

# 13. 누나는 영철이보다 며칠 더 먼저 태어났을까?
# 영철이 누나의 생일은 1995년 11월 20일이고 영철이의 생일은 1998년 10월 6일이다.
# 영철이 누나는 영철이보다 며칠 더 먼저 태어났을까?

import datetime
day1 = datetime.date(1995, 11, 20)
day2 = datetime.date(1998, 10, 6)
diff = day2-day1
print(diff.days)

# 14.기록순으로 정렬하기
# 다음은 1학년 3반 학생들의 100m 달리기 기록이다.
# 기록순으로 data를 정렬해보자

data14 = [('윤서현', 15.25),
        ('김예지', 13.31),
        ('박예원', 15.34),
        ('송순자', 15.57),
        ('김시우', 15.48),
        ('배숙자', 17.9),
        ('전정웅', 13.39),
        ('김혜진', 16.63),
        ('최보람', 17.14),
        ('한지영', 14.83),
        ('이성호', 17.7),
        ('김옥순', 16.71),
        ('황민지', 17.65),
        ('김영철', 16.7),
        ('주병철', 15.67),
        ('박상현', 14.16),
        ('김영순', 14.81),
        ('오지아', 15.13),
        ('윤지은', 16.93),
        ('문재호', 16.39)]

from operator import itemgetter
data14 = sorted(data14, key=itemgetter(1))

for d in data14:
   print(d)

#15. 청소 당번 2명 뽑기
# 다음 4명의 학생 중 청소 당번 2명을 뽑을 수 있는 경우의 수를 모두 나열하시요.
# ['나지혜', '성성민', '윤지현', '김정숙']

import itertools

data15 = ['나지혜', '성성민', '윤지현', '김정숙']
resutl15 = list( itertools.combinations(data15,2) )
print( resutl15 )

for i in resutl15:
    print(i)

# 16. 문자열 나열하기
# "abcd" 문자열을 나열하는 경우의 수를 다음과 같이 모두 출력하시오.
# abcd, abdc, adcb (...생략...)

data16 = "abcd"

result16 = itertools.permutations(data16,4)
for i in result16:
    #print(i)
    print(''.join(i))

# 17. 5명에게 할 일 부여하기
# 다음 5명이 있다.
# ['김승현', '김진호', '강춘자', '이예준', '김현주']
# 그리고 해야 할 일은 다음처럼 3가지가 있다.
# ['청소','빨래','설거지']
# 5명을 무작위로 섞어 앞의 3명에게 차례로 해야 할 일인 ["청소","빨래","설거지"]를 
# 지정하고 나머지2명에게는 "휴식"을 지정할 수 있는 프로그램을 작성하시오.

# itertools_zip.py

import itertools
students = ['김승현', '김진호', '강춘자', '이예준', '김현주']
clean = ['청소','빨래','설거지']

result17 = itertools.zip_longest(students, clean, fillvalue='휴식')
print(list(result17))

# 18. 벽에 타일 붙이기
# 가로의 길이는 200cm이고 세로의 길이는 80cm인 벽이 있다.
# 이 벽에 되도록 큰 정사각형 모양의 타일을 붙이려고 한다. 
# 이때 붙이려는 타일 한 선의 길이와 붙이는데 필요한 타일의 개수를 구하시오.
# 최대공약수 구하는 함수

import math

width = 200
height = 80

square = math.gcd(width, height)
print(f"타일 한 선의 길이:{square}")

width_c = width/square
height_c = height/square
print(f"width_c:{width_c}")
print(f"height_c:{height_c}")
print(f"필요한 타일의 개수:{int(width_c*height_c)}")