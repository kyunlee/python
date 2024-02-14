# 파일 읽고 쓰기
# newfile.py
f = open("새파일.txt", 'w')
f.write("Life is too short, you need python")
f.close()

# 파일_객체 = open(파일_이름, 파일_열기_모드)
# r - 읽기모드 : 파일을 읽기만 할 때 사용한다.
# w - 쓰기모드 : 파일에 내용을 쓸 때 사용한다.
# a - 추가모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

f = open("d:/python/새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일을 읽는 여러 가지 방법
# 1. readline 함수 이용하기

f = open("d:/python/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# 출력결과-> 1번째 줄입니다.
# 만약 모든 줄을 읽어 화면에 출력하고 싶다면 다음과 같이 작성
f = open("d:/python/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close

# 2.readlines 함수 사용하기
f = open("d:/python/새파일.txt", 'r')
line = f.readlines()
print(line)
f.close()
#줄 바꿈(\n) 문자 제거하기
#파일을 읽을 때 줄 끝의 줄 바꿈(\n) 문자를 제거하고 사용해야 할 경우가 많다. 
#다음처럼 strip 함수를 사용하면 줄 바꿈 문자를 제거할 수 있다
'''
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()
'''
# 3. read 함수 사용하기
f = open("d:/python/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 4.파일 객체를 for 문과 함께 사용하기
# 파일 객체(f)는 기본적으로 위와 같이 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다.
f = open("d:/python/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

# with 문과 함께 사용하기
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close

#파일을 열면(open) 항상 닫아(close) 주어야 한다. 
# -> 파이썬의 with 문이 바로 이런 역할을 해 준다
with open("foo.txt","w") as f:
    f.write("Life is too short, you need python")

