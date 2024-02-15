# 모듈

# 모듈이란? 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

# import 모듈_이름
import mod1
print("모듈")
print(mod1.add(3,4))
print(mod1.sub(4,2))

# from 모듈_이름 import 모듈_함수
from mod1 import add
print(add(3,4))

from mod1 import add, sub
print(sub(4,1))

# from 모듈_이름 import 모듈_함수1, 모듈_함수2
# from mod1 import *

# if __name__ == "__main__":의 의미
# 출력 차이
'''
5
2
모듈
7
2
7
3

모듈
7
2
7
3
'''
print(mod1.__name__)

# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름
