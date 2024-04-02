import math
'''
def solution(n):
    return 7%n

print(math.ceil(15/7))

n=15

def solutionex(n):
    return (n - 1) // 7 + 1

print( (n - 1) // 7 )



n=10

print(math.gcd(n, 6))
print( round((n * 6 // math.gcd(n, 6))/6) )
    
slice =  7
n = 10
print(math.ceil(n/slice))
print(  math.gcd(n, slice) )
print( round((n * slice // math.gcd(n, slice))/slice) )
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def solution(numbers):
    answer = 0
    for i in numbers:
        answer +=i        
    return answer/len(numbers)

print(solution(numbers))