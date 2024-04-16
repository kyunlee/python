#문자열의 앞의 n글자
my_string = 'ProgrammerS123'
n=11
def solution(my_string, n):
    return my_string[:n]

#print(solution(my_string, n))

# 접두사인지 확인하기
my_string = "banana"
is_prefix = "bananan"

def solution(my_string, is_prefix):    
   return 1 if my_string[:len(is_prefix)] == is_prefix else 0

#print(solution(my_string, is_prefix))

#문자열뒤집기
my_string = "Progra21Sremm3"
s = 6
e = 12

def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]

#print(solution(my_string, s, e)) 
#2

#세로읽기
my_string = "ihrhbakrfpndopljhygc"
m = 4
c = 2
def solution(my_string, m, c):
    return ''.join([my_string[i+c-1] for i in range(0,len(my_string),m)])

#print(solution(my_string, m, c))
#2

#qr code
q = 3
r = 1
code = "qjnwezgrpirldywt"
def solution(q, r, code):
    return ''.join([code[i] for i in range(len(code)) if i%q == r])

print(solution(q, r, code))

