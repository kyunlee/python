# 주사위의 개수
box = [10,8,6]
n = 3

def solution(box, n):
    return (box[0]//n)*(box[1]//n)*(box[2]//n)

#print(solution(box, n))

# 합성수 찾기

n = 10

def solution(n):
    return len([i for i in range(1,n+1) if len([j for j in range(1,i+1)if i % j == 0]) >= 3])                     

#print(solution(n))

# 최대값 만들기(1)

numbers = [1,2,3,4,5]
def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers[0]*numbers[1]

#print(solution(numbers))

#팩토리얼

n= 3
def solution(n):
    f= 1
    for i in range(1,n+1):        
        f = f*i
        print(f,i)
        if f > n:
            return i-1
    return i
    
print(solution(n))