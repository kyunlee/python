# 1리스트 자르기

n = 4
slicer = [1,5,2]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solution(n, slicer, num_list):    
    if n == 1:
        return num_list[0:slicer[1]+1]
    elif n == 2:
        return num_list[slicer[0]:]
    elif n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    else:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]
    
#print(solution(n, slicer, num_list))

#2첫 번째로 나오는 음수

num_list=[12, 4, 15, 46, 38, -2, 15]

def solution(num_list):
    for i,j in enumerate(num_list):
        if j < 0:
            return i
    return -1

#print(solution(num_list))

# 3배열만들기 3
'''
arr = [1,2,3,4,5]
intervals = [[1, 3], [0, 4]]

def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1]+arr[intervals[1][0]:intervals[1][1]+1]
'''
#print(solution(arr, intervals))

#4.2의 영역

aarr = [1, 2, 1, 2, 1, 10, 2, 1]

def solution(arr):    
    idx = []
    for i,j in enumerate(arr):
        if j == 2:
            idx.append(i)

    if len(idx) >= 2:
        return arr[idx[0]:idx[len(idx)-1]+1]
    elif len(idx) == 1:
        return [arr[idx[0]]]
    else:
        return [-1]

#print(solution(aarr))

# 5.배열 조각하기
arr5 = [0, 1, 2, 3, 4, 5]
query = [4,1,2]

def solution(arr, query):
    for i,j in enumerate(query):
        if i % 2 == 0:
            arr = arr[:j+1]
        else:
            arr = arr[j:]
    return arr

print(solution(arr5, query))