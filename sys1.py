# sys모듈 사용하기

import sys
#파이썬에서는 sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다.

'''
args = sys.argv[1:]

for i in args:
    print(i)
'''

numbers = sys.argv[1:] #파일 이름을 제외한 며령 행의 모든입력

result = 0
for number in numbers:
    result += int(number)

print(result)