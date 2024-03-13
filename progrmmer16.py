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
print(list(enumerate(numLog)))
print(len(numLog))

for i, num in enumerate(numLog):
    print('i=',i)
    if i < len(numLog)-1:
        value = numLog[i+1]-numLog[i]
        #print(value)
        answer +=dempy[value]

    #print(answer)

print(range(1,len(numLog)))

print(numLog[1:])
print( list(enumerate(numLog[1:]) ) )

[(0, 1), (1, 0), (2, 10), (3, 0), (4, 1), (5, 0), (6, 10), (7, 0), (8, -1), (9, -2), (10, -1)]
[(1, 1), (2, 0), (3, 10), (4, 0), (5, 1), (6, 0), (7, 10), (8, 0), (9, -1), (10, -2), (11, -1)]