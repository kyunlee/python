#
# 배열비교하기
arr1 = [49,13]
arr2 =[70,11,2]

def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif  len(arr1) > len(arr2):
        return 1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
#1

# 문자열 묶기
