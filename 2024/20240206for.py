# for문

#1.for문의 기본 구조
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
'''

#2.예제를 통해 for문 이해하기
#2-1.전형적인 for문
test_list = ['one','two','three']
for i in test_list:
    print(i)

#2-2.다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first + last)

#2-3.for문의 응용
'''
총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격
그렇지 않으면 불합격. 합격인지, 불합격인지 결과
'''
marks = [90,25,67,45,80]

#marks1.py

# for 문과 continue 문

'''
60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는
아무런 메시지도 전하지 않는 프로그램
'''
# marks2.py

# for 문과 함께 자주 사용하는 range 함수
a = range(10)
print(range(0,10))
#range(시작_숫자, 끝_숫자) 형태를 사용하는데
#이때 끝 숫자는 포함되지 않는다.
a = range(1, 11)
print(a)

# range 함수의 예시 살펴보기
# for와 range 함수를 사용하면 1부터 10까지 더하는 것을 다음과 같이 쉽게 구현 할 수 있다.
add = 0
for i in range(1, 11):
    add = add + 1

print(add)

#marks3.py

#for와 range를 이용한 구구단

for i in range(2,10):       # 1번 for문
    for j in range(1, 10):  # 2번 for문
        print(i*j,end=" ")
    print('')

#print 문의 end 매개변수에는 줄바꿈 문자(\n)가 기본값으로 설정되어 있음.

#리스트 컴프리헨션 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

#리스트 컴프리헨션을 사용하면 다음과 같이 좀 더 간단하게 작성
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

#[표현식 for 항목 in 반복_가능_객체 if 조건문]
'''
[표현식 for 항목1 in 반복_가능_객체1 if 조건문1
       for 항목2 in 반복_가능_객체2 if 조건문2
      ...
       for 항목n in 반복_가능_객체n if 조건문n]
'''

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)