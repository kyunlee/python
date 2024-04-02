
ineq = ">"
eq = "!"
n = 41
m = 78

def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            return 1 if (n>=m) else 0
        else:
            return 1 if (n>m) else 0
    else:
        if eq == "=":
            return 1 if (n<=m) else 0
        else:
            return 1 if (n<m) else 0

'''

def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
'''
print("4-3=",solution(ineq, eq, n, m))

a= -4
b = 7
flag = 'true'

if flag:
    answer = a + b
else:
    answer = a - b