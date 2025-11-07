# 표준 라이브러리

# datetime.date : 연, 월, 일로 날짜를 표현할 때 사용하는 함수

import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

diff = day2 - day1
print(diff.days)

day = datetime.date(2024,2,20)
print( day.weekday() )
# 0 월요일 ...

print( day.isoweekday() )
# 1 월요일 ...

# time
import time
print( time.time() )

# time.localtime :  time.time()이 리턴한 실숫값을 사용해서 연, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수
print( time.localtime(time.time()) )
print( "localtime 인수없이",time.localtime() )

# time.asctime
print( time.asctime(time.localtime(time.time())) )
print( "asctime 인수없이",time.asctime() )

# time.ctime : ctime이 asctime과 다른 점은 항상 현재 시간만을 리턴한다는 점
print( time.ctime() )

# time.strftime  : time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
print( time.strftime('%x', time.localtime(time.time())) )
print( time.strftime('%c') )
'''
for i in range(10):
    print(i)
    time.sleep(1)
'''

# math
import math

# math.gcd : 최대 공약수(gcd, greatest common divisor)
print('math.gcd=', math.gcd(60, 100, 80) )

# math.lcm : 최소 공배수(lcm, least common multiple)
print('math.lcm=',math.lcm(15,25)  )

# random : random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
import random 

print( 'random=',random.random() )
print( 'randint=', random.randint(1,10) )

def random_pop(data):
    number = random.randint(0, len(data) -1 )
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print('random_pop=',random_pop(data))

def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print('random_pop2=',random_pop2(data))

#random.sample 함수에서 두 번째 인수인 len(data)는 무작위로 추출할 원소의 개수를 의미
data = [1, 2, 3, 4, 5]
print('random.sample=',random.sample(data,len(data)) )

#itertools.zip_longest
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = zip(students, snacks)
print(list(result))

import itertools
students = ['하민서','황지민','이영철','이광수','김승민']
snacks = ['사탕','초컬릿','젤리']

# itertools.zip_longest(*iterables, fillvalue=None) 
result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))

# itertools.permutations(iterable, r) : 반복 가능 객체 중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수
print ( list(itertools.permutations(['1','2','3'],2)) )


for a, b in itertools.permutations(['1','2','3'],2):
    print('a+b=',a+b)

# itertools.combinations(iterable, r):  반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 리턴하는 함수
print( list( itertools.combinations(['1','2','3'],2) ) )

it = itertools.combinations(range(1,46),6)
'''
print( list(it) )

for num in it:
    print(num)
'''
#print( len(list(itertools.combinations(range(1, 46), 6))) )
#print( len(list(itertools.combinations_with_replacement(range(1, 46), 6))) )

# functools.reduce(function, iterable)

def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1,2,3,4,5]
result = add(data)
print(result)

import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x+y, data)
print(result) # ((((1+2)+3)+4)+5)

num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y : x if x > y else y , num_list)
print('max_num=',max_num)
min_num = functools.reduce(lambda x, y : x if x < y else y , num_list)
print('min_num=',min_num)

# operator.itemgetter는 주로 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈

from operator import itemgetter

students = [ 
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, "B"),
]

result = sorted(students, key=itemgetter(1))
print(result)

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

result = sorted( students, key=itemgetter('age'))
print(result)

# operator.attrgetter()
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result = sorted(students, key=attrgetter('age') )

# shutil : shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈
import shutil

#shutil.copy("d:\\python\\python-1\\doit\\a.txt", "d:\\python\\python-1\\temp\\a.txt.bak")
#shutil.move("d:\\python\\python-1\\doit\\a.txt", "d:\\python\\python-1\\temp\\a.txt")

# glob : 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
import glob
a = glob.glob("d:\\python\\python-1\\foo*")
print( list(a) )

# pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

import pickle
f = open("test.txt", "wb")
data = {1:'python', 2:"you need"}
pickle.dump(data, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

# os : 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈

import os

# 내 시스템의 환경 변숫값을 알고 싶을 때 - os.environ
#print( os.environ )
#print( os.environ['PATH'] )

# 디렉터리 위치 변경하기 - os.chdir
#os.chdir("D:\\python")
#os.chdir("D:\\python")

# 디렉터리 위치 돌려받기 - os.getcwd
#print( os.getcwd() ) # D:\python\python-1

# 시스템 명령어 호출하기 - os.system
# print( os.system("dir") )

# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen

f = os.popen("dir")
# print( f.read() )

# zipfile : 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용하는 모듈

# threading
'''
컴퓨터에서 동작하고 있는 프로그램을 프로세스(process)
보통 1개의 프로세스는 1가지 일만 하지만, 스레드(thread)를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행
'''
'''
# thread_test.py
import time

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("working:%s\n" % i)

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")

import time
import threading # 스레드를 생성하기 위해서 threading 모듈이 필요

def long_task(): # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) # 1초간 대기한다.
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5): # long_task를 5회 수행한다.
    t = threading.Thread(target=long_task) # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start() # 스레드를 실행한다.

for t in threads:
    t.join() # join으로 스레드가 종료될때까지 기다린다.

print("End")
'''

# tempfile : 파일을 임시로 만들어서 사용할 때 유용한 모듈
'''
import tempfile
filename = tempfile.mkstemp()
# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴

print(filename)

f = tempfile.TemporaryFile()
f.close()
'''

# traceback : 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())

main()