#1. 홀수, 짝수 판별하기
# 주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 is_odd를 작성해 보자.
# is_odd 함수는 홀수이면 True, 짝수이면 False를 리턴해야 한다.
def is_odd(number):
    if ( number % 2 == 0 ):
        return True
    else:
        return False

print(is_odd(2))

#2. 모든 입력의 평균값 구하기
# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자.
# 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.

def avg_numbers( *args ):
    result = 0
    for i in args:
        result += i
    return result/i

print( avg_numbers(1, 2) )      #<- 1.5 출력
print( avg_numbers(1,2,3,4,5) ) #<- 3.0 출력

#3. 프로그램 오류 수정하기1
# 다음은 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램

input1 = input("첫 번째 숫자를 입력하세요 :")
input2 = input("두 번째 숫자를 입력하세요 :")

total = int(input1) + int(input2)
#print("두 수의 합은 %s 입니다." % total) -> 두 수의 합은 36 입니다.

print("두 수의 합은 %d 입니다." % total) 

#4. 출력 결과가 다른 것은? 3번
print("you" "need" "python")
print("you"+"need"+"python")
print("you","nedd","python")
print("".join(["you","need","python"]))

#5. 프로그램 오류 수정하기 2
#다음은 파일(test.txt)에 "Life is too short" 문자열을 저장한 후 다시 그파일을 읽어 출력하는 프로그램
f1 = open("test.txt", 'w')
f1.write("Life is too short")

#😃👌
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

#6. 사용자 입력저장하기
user_input = input("저장할 내용을 입력하세요:")
f = open('test6.txt', 'a') # <-내용을 추가하기 위해 'a'를 사용
f.write(user_input) 
f.write("\n") #<- 입력한 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()   

#7. 파일의 문자열 바꾸기
#다음과 같은 내용을 지난 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어 저장해보자

'''
Life is too short
you need java
'''
f = open('test7.txt', 'w')
f.write("Life is too short you need java")
f.close()

f = open('test7.txt', 'r')
body =  f.read()  # <- test.txt의 내용을 body 변수에 저장
f.close()
print(body)
# replace 함수를 써볼까!
body = body.replace("java","python") # <-body 문자열에서 "java"를 "python"으로 변경
print('body=',body)

f= open('test7.txt', 'w') #<- 파일을 쓰기모드로 다시 실행
f.write(body)
f.close()

#8. 입력값을 모두 더해 출력하기
# d:\python\python-1\myargv.py 작성해보자.
# d:\python\python-1> python myargv.py 1 2 3 4 5 6 7 8 9 10
import sys

numbers = sys.argv[1:] #파일 이름을 제외한 며령 행의 모든입력

result = 0
for number in numbers:
    result += int(number)
print(result)