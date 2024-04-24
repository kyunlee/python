#1.모음제거

my_string1 = "nice to meet you"

def solution(my_string):
    모음 = ['a', 'e', 'i', 'o', 'u']
    answer = ''

    for i in my_string:
        if i not in 모음:
            answer += i                          
    return answer

#print(solution(my_string1))

#2.문자열 정렬하기(1)
my_string2 = "hi12392"

def solution(my_string):
    answer =[]
    for i in my_string:
        if i.isalpha() == False:
            answer.append(int(i))    
    return sorted(answer)

#print(solution(my_string2))

#3숨어있는 숫자의 덧셈 (1)
 
my_string3= "aAb1B2cC34oOp"

def solution(my_string):    
    return sum([int(i) for i in my_string if i.isdigit()])

#print(solution(my_string3))

# 소인수분해
n = 420

def solution(n):
    i = 2
    answer = []
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n= n/i
        else:
            i += 1
    return sorted(list(set(answer)))

print(solution(n))