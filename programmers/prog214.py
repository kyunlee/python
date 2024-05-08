# 1.가까운 수

array =   [6, 7, 10, 2, 4]
n = 5

def solution(array, n):
   array.sort()
   dif = [abs(n - i) for i in array]

   return array[dif.index(min(dif))]
        

print(solution(array, n)) 
        

# 2.369게임
order = 29423

def solution(order):
    su = 0
    for i in str(order):
        if i in ('3','6','9'):
            su +=1
    return su

#print(solution(order))

# 3.암호 해독
cipher = "dfjardstddetckdaccccdegk"
code = 4

def solution(cipher, code):    
    return cipher[code-1::code]

#print(solution(cipher, code))

# 4.대문자와 소문자
my_string1 ="cccCCC"

def solution(my_string):    
    return ''.join([i.lower() if i.isupper() else i.upper() for i in my_string ])

#print(solution(my_string1))