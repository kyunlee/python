'''
import math

numer1 = 9
denom1 = 2
numer2 = 1
denom2 = 3

def solution(numer1, denom1, numer2, denom2):
    bja= (numer1*denom2)+(denom1*numer2)
    bmo= denom1*denom2
    gcd = math.gcd(bja,bmo)
    bjabja = int(bja/gcd)
    bmobmo = int(bmo/gcd)
    answer = [bjabja, bmobmo]
    return answer

print( solution(numer1, denom1, numer2, denom2) )
'''
numbers = [1,2,3,4,5]

def solution(numbers):
    return list(map(lambda a: a*2, numbers))

print(solution(numbers))