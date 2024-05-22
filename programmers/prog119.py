# 세개의 구분자

myStr = "cabab"

def solution(myStr):
    import re
    return ["EMPTY"] if list(filter(None,re.split('[abc]',myStr))) == [] else list(filter(None,re.split('[abc]',myStr)))

#print(solution(myStr))

# 배열의 원소만큼 추가하기

arr= [5,1,4]

def solution(arr):
    answer = []
    for i in arr:
        answer += [i]*i
    return answer

print(solution(arr))

# 빈 배열에 추가, 삭제하기

arr = [3,2,4,1,3]
flag = [True, False, True, False, False]

def solution(arr, flag):
    answer = []
    for i,j in enumerate(arr):
        if flag[i]: 
            answer += [j]*(j*2)
        else:
            for j in range(0,j):
                answer.pop()
    return answer

#print(solution(arr,flag))

# 배열만들기 6

arr = [0, 1, 1, 1, 0]
def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if answer == []: 
            answer.append(arr[i]) 
            i+=1
        elif answer[len(answer)-1] == arr[i]:
            answer.pop()
            i+=1
        elif answer[len(answer)-1] != arr[i]:
            answer.append(arr[i]) 
            i+=1
    return answer or [-1]

#print(solution(arr))

#무작위로 K개의 수 뽑기

arr = [0, 1, 1]	
k = 4

def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
            print(answer)
        if len(answer) >= k : return answer

    for _ in range(len(answer),k):
        answer.append(-1)
    return answer

           
print(solution(arr, k))


