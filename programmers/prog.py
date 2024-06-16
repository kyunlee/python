num_list = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]

def solution(num_list):
    num_list.sort()
    return num_list[6:]

num_str = "123456789"
def solution(num_str):
    return sum([int(i)for i in num_str])

#print( solution(num_str) )

strArr = ["a","bc","d","efg","hi"]

def solution(strArr):
    from collections import Counter
    length_counter = Counter([len(i) for i in strArr])
    return length_counter.most_common(1)[0][1]

#print(solution(strArr))

arr = [444, 555, 666, 777]
n =100
def solution(arr, n):    
    for i,j in enumerate(arr):
        if i%2 == 0 and len(arr)%2 == 1:
            arr[i]= j+n
        elif i%2 == 1 and len(arr)%2 == 0:
            arr[i]= j+n
    return arr
#print(solution(arr, n))

arr = [58, 172, 746, 89]

def solution(arr):   
    cpyarr = arr

    while len(cpyarr) & len(cpyarr)-1 != 0:
        cpyarr.append(0)

    return cpyarr
    
#print(solution(arr))

rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]

def solution(rank, attendance):
    answer = []
    for i,j in enumerate(rank):
        if attendance[i]:
            answer.append(j)
        else:
            answer.append(0)
    return answer

print(solution(rank, attendance))