'''
배열자르기
'''
numbers = [1, 2, 3, 4, 5]
num1 = 1
num2 = 3

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

#print(solution(numbers, num1, num2))

'''
외계행성나이 
'''

age = 23

def solution(age):
    answer = []
    ni = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    for i in list(str(age)):
        answer.append(ni[i])      
    return ''.join(answer)

print(solution(age))

'''
순서쌍의 개수
'''
# 속도에서 까임
n = 20

def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j == n:
                answer = answer + 1
    return answer

def solution1(n):
    answer = 0
    for i in range(1,n+1):
            if n%i == 0:
                answer = answer + 1
    return answer

#print(solution1(n))

emergency =[3, 76, 24]

copy = emergency
copy = sorted(emergency, reverse=True)
print(emergency)
print(copy)
answer =[]

def solution(emergency):
    return [copy.index(i)+1 for i in emergency]

print(solution(emergency))

