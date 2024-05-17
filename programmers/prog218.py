# 문자열안에 문자열

str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"

def solution(str1, str2):   
    return 1 if str2 in str1 else 2

#print(solution(str1,str2))

# 제곱수 판별하기
n = 144
def solution(n):
    import math
    return  1 if math.sqrt(n) % 1 == 0 else 2

#print(solution(n))

#세균 증식
n = 2
t = 10

def solution(n, t):
    i = 0
    while i < t:
        i+=1
        n=n*2
    return n

print(solution(n,t))