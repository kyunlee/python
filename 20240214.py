# 파일 읽고 쓰기
# newfile.py
f = open("새파일.txt", 'w')
f.write("Life is too short, you need python")
f.close()

# 파일_객체 = open(파일_이름, 파일_열기_모드)
# r - 읽기모드 : 파일을 읽기만 할 때 사용한다.
# w - 쓰기모드 : 파일에 내용을 쓸 때 사용한다.
# a - 추가모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

with open("foo.txt","w") as f:
    f.write("Life is too short, you need python")
