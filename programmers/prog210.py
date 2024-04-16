#점의 위치 구하기

dot = [-3,4]

def solution(dot):
    if dot[0]>0  and dot [1]>0:
        return 1
    elif dot[0]<0  and dot [1]>0:
        return 2
    elif dot[0]<0  and dot [1]<0:
        return 3
    else:
        return 4
    
#print(solution(dot))

#2차원으로 만들기
    
def solution(num_list, n):
    return [num_list[i:n+i] for i in range(0,len(num_list),n)]

# 공던지기
'''
numbers = 	[1, 2, 3, 4]
k = 2

def solution(numbers, k):
    print((k-1)*2 % len(numbers))
    return numbers[(k-1)*2 % len(numbers)]

#print(solution(numbers, k))
'''
# 배열회전시키기

numbers = [4, 455, 6, 4, -1, 45, 6]
direction = "left"

def solution(numbers, direction):
    answer=[]
    if direction == "right":
        answer.append(numbers[len(numbers)-1])
        for i in range(0,len(numbers)-1):
            answer.append(numbers[i])
    else:
        for i in range(1,len(numbers)):
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer

print(solution(numbers, direction))