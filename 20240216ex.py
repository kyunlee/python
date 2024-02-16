# 예외 처리
# 오류는 언제 발생하는가?

#f = open("나없는파일", 'r')
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

#4/0
# ZeroDivisionError: division by zero

a = [1, 2, 3]
# a[3]
# IndexError: list index out of range

# 오류 예외 처리 기법

# try-except 문
'''
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
'''

# 1. try-except 만 쓰는 방법
'''
try:
    ...
except:
    ...
'''

# 2. 발생 오류만 포함한 except 문
'''
try:
    ...
except 발생오류:
    ...
'''

# 3. 발생 오류와 오류 변수까지 포함한 except 문
'''
try:
    ...
except 발생오류 as 오류변수:
    ...
'''

try:
    4/0
except ZeroDivisionError  as e:
    print(e)

# try-finally 문

try:
    f = open('foo.txt','w')
    # 무언가를 수행한다.
    
    # (... 생략 ...)

finally:
    f.close() # 중간에 오류가 발새하더라도 무조건 실행됨.

# 여러 개의 오류 처리하기
'''
try
    ...
except 발생오류1:
    ...
except 발생오류2:
    ...
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

# -> 인덱싱 할 수 없습니다. 먼저 오류 발생한 부분
# 두오류 함께 처리하기 위해서.
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# try -else 문
'''
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
else:  # 오류가 없을 경우에만 수행
    ...
'''

try:
    age = int(input('나이를 입력하세요:'))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

# 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

'''
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

Traceback (most recent call last):
  File "d:\python\python-1\20240216ex.py", line 126, in <module>
    eagle.fly()
  File "d:\python\python-1\20240216ex.py", line 120, in fly
    raise NotImplementedError
NotImplementedError
'''

# 상속받는 클래스에서 메서드를 재구현하는 것을 ‘메서드 오버라이딩’이라고 함.

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

# 예외 만들기
class MyError(Exception):
    #pass
    def __str__(self):
        return "허용되지 않는 별명입니다."
    

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    #print("허용되지 않는 별명입니다.")
    print(e)


