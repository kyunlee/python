# 숫자 찾기

num = 29183
k = 1

def solution(num, k):
    for i,j in enumerate(str(num)):
        if j == str(k):
            return i-1
    return -1   

#print(solution(num, k))

# n의 배수 고르기

n= 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
def solution(n, numlist):  
    return [i for i in numlist if i%n==0 ]

print(solution(n,numlist))

# 자릿수 더하기

n = 1234
def solution(n):    
    return sum(int(i) for i in str(n))

print(solution(n))

# OX퀴즈
quiz = ["3 - 4 = -3", "5 + 6 = 11"]

def solution(quiz):
    return ["O" if eval(i.split("=")[0]) == int(i.split("=")[1]) else "X" for i in quiz]
        
print(solution(quiz))
