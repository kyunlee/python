num_list = [2, 1, 6] 

if num_list[int(len(num_list)-1)] > num_list[int(len(num_list)-2)] :
    num_list.append( num_list[int(len(num_list)-1)] - num_list[int(len(num_list)-2)]  )
else:
    num_list.append( num_list[int(len(num_list)-2)] *2 )

#print(num_list)
    
n= 0
control = "wsdawsdassw"
def solution(n, control):
    dempy = {'w':1,'s':-1,'d':10,'a':-10}
    for a in control: n += dempy.get(a) 
    return n
    
#print(n)

def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])


numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
dempy= {1:'w',-1:'s',10:'d',-10:'a'}
#dempy = {'w':1,'s':-1,'d':10,'a':-10}
answer = ''
#print(list(enumerate(numLog)))
#print(len(numLog))

for i, num in enumerate(numLog):
    #print('i=',i)
    if i < len(numLog)-1:
        value = numLog[i+1]-numLog[i]
        #print(value)
        answer +=dempy[value]

    #print(answer)

#print(range(1,len(numLog)))

#print(numLog[1:])
#print( list(enumerate(numLog[1:]) ) )

#수열과 구간 쿼리 3

arr = [0, 1, 2, 3, 4]	
queries = [[0, 3],[1, 2],[1, 4]]

#[3,1,2,0,4]
#[3,2,1,0,4]
#[3,4,1,0,2]

for i in queries:
    j= arr[i[0]]
    arr[i[0]]=arr[i[1]]
    arr[i[1]]=j

#print(arr)

# 수열과 구간 쿼리 2
    
arr = [0,1,2,4,3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

answer = []
for s,e,k in queries:
    answer.append( min( list( filter(lambda x : x > k , arr[s:e+1]) ), default=-1) )
    
##################
    
for s,e,k in queries:
    for i, j in enumerate(arr[s:e+1]):
        if i > k:
            print(i)