
n=3
def solution(n):
    answer = []
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j]=1
            else:
                answer[i][j]=0
    return answer

print(solution(n))

'''
arr= [[5, 192, 33], [192, 72, 95], [33, 95, 999]]
def solution(arr):
    for i in arr:
        for j in arr:
            if arr[i][j] == arr[j][i]:
                answer = 1
            else:
                answer = 0
    
    return answer

date1 =[2022, 1, 1]
date2 = [2021,12,31]
def solution(date1, date2):
    answer = 0
    if date1[0] > date2[0]:
        return  0
    else:
        if date1[1] < date2[1]:
            answer= 1
        else:
            answer= 0
        if date1[2] < date2[2]:
            answer= 1
        else:
            answer= 0
    return answer
#print(solution(date1, date2))


'''



