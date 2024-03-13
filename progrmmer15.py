
#코드처리하기
code = "abc1abc1abc"
'''
def solution(code):
    mode = 0
    answer = ''
    for i in code:
        if(i%2 == 0):
            answer += i
            print(answer)
    return answer

'''

"".join(code.split("1"))[::2] or "EMPTY"

'''
code = ''
mode = 0
answer = ''
for i, a in enumerate(code):
    print('i',i,'i % 2=',i % 2,'mode=',mode, 'a=',a)
    if a == '1' and mode == 0:
        mode = 1        
    elif a == '1' and mode == 1:
        mode = 0
    elif mode == 0 and i%2== 0:
        answer += a
    elif mode == 1 and i%2== 1:
        answer += a
    elif answer == '' :
        answer = "EMPTY"

if answer == '' :
        answer = "EMPTY" 
print(answer)

'''

# 등차수열의 특정한 항만 더하기
a = 3
d = 4
included = [True, False, False, True, True]

answer = 0
sum = [a]

for i, b in enumerate(included):   
    print(sum)
    if b: answer+= sum[i]      
    sum.append(sum[i]+d)

print(answer)

sum(a + i * d for i, f in enumerate(included) if f)
