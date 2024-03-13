
# 주사위 게임 2

a=4
b=4
c=4

def solution(a, b, c):
    answer = 0
    if a != b and a != c and b != c:
        answer = (a+b+c)
    elif a==b and a==c and b==c:
        answer =  (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)  
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)
    return answer

print(solution(a, b, c))

#print( (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)  )

check=set([a,b,c])
print('check=',check)

# 원소들의 곱과 합

num_list = [3,4,5,2,1]
num_list = [5,7,8,3]
def solution(num_list):
    mul= 1
    dsum = 0
    for i in num_list:
        mul *= i
        dsum += i

    if mul < (dsum**2):
        answer = 1
    else:
        answer = 0
    return answer
        
#print( solution(num_list) )

# 이어 붙인 수
num_list = [3, 4, 5, 2, 1]

def solution(num_list):
    a = ''
    b = ''
    for i in num_list:
        if i % 2 == 0:
            a = a+str(i)
        else:
            b = b+str(i)    
    return int(a)+int(b)

print( solution(num_list) )