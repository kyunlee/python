# 수열과 구간 쿼리 4
arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
'''
for s,e,k in queries:
    for i in range(s,e+1):
        if(i%k==0):
            arr[i] +=1

#print(arr)

for q in queries:
        #print((q[0] + q[2] - 1) // q[2] * q[2])
        #print(q[1] + 1)
        #print(q[2])
        for i in range((q[0] + q[2] - 1) // q[2] * q[2], q[1] + 1, q[2]):
            arr[i] += 1
'''

l = 5
r = 55
j = 0
answer =[]
'''
for n in range(l, r+1):
    print(set(str(n)))
    if set(str(n)) & {'0','5','50'} != {}  :
        answer.append(n)

for n in range(l, r+1):
    if all(j in str(n) for j in  ['5','0']):
        print(n)

for n in range(l, r+1):
    if all(j in ['5','0'] for j in str(n)):
        answer.append(n)
    
if answer == []:
    answer.append(-1)

#print(answer)


for num in range(l,r+1):
    if set(str(num)).issubset <= {'0', '5'}:        
        print(num)
        #if set(str(num)).issubset({'0','5'}):
        #    num_list.append(num)

'''

'''
def solution(start_num, end_num):
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer

start_num =3
end_num =10
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num+1)]

#print(solution(start_num, end_num))

n = 10
#result [10, 5, 16, 8, 4, 2, 1]
# 짝 n/2
# 홀 3*n+1

def solution(n):
    answer.append(n)
    if n == 1: return answer
    while n > 1:        
        if n % 2 == 0:        
            n = int(n/2)
            answer.append(n)
        else:
            n = 3*n+1
            answer.append(n)
    
    return answer

#print(solution(n))
'''
arr = [1,4,2,5,3]

def solution(arr):
    stk = []
    i=0     
    while i < len(arr):        
        if stk == []:
            stk.append(arr[i])
            i+=1
        elif stk != [] and stk[-1] < arr[i]:
            stk.append(arr[i])
            i+=1
        elif stk !=[] and stk[-1] >= arr[i]:
            stk.pop()
            
    return stk

print(solution(arr))
