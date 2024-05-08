# 1.조건에 맞게 수열 변환하기 1

arr1 = [1, 2, 3, 100, 99, 98]

def solution(arr):
    answer = []
    for i in arr:
        if i%2 == 0 and i >= 50:
            answer.append(i//2)
        elif i%2 != 0 and i < 50:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer

#print(solution(arr1))

# 2.조건에 맞게 수열 변환하기 2

arr2 = [1, 2, 3, 100, 99, 98]

def solution(arr):
    answer1 = arr
    answer2 = []
    answer = 0
    
    while True:                                          
        for i in answer1:            
            if i%2 == 0 and i >= 50:
                answer2.append(i//2)
            elif i%2 != 0 and i < 50:
                answer2.append(i*2+1)
            else: 
                answer2.append(i)   

        if answer1==answer2: break  
        else:  
            answer +=1  
            answer1 = answer2   
            answer2 = []  
    return answer

print(solution(arr2))


# 3.1로 만들기
num_list3 = [12, 4, 15, 1, 14]

def solution(num_list):
    answer = 0
    for i in num_list:
        while i > 1:
            if i//2 == 1:
                answer +=1
                break
            elif i%2 == 0:
                i = i//2
                answer +=1
            else: 
                i = (i-1)//2
                answer +=1
    return answer

#print(solution(num_list3))


# 4.길이에 따른 연산 
num_list = [2,3,4,5]	

def solution(num_list):
    from functools import reduce
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return reduce(lambda x, y: x*y, num_list)
    
# print(solution(num_list))

# 5. 원하는 문자열 찾기

myString = "aaAA"
pat = "aaaaa"
def solution(myString, pat):
    return 1 if pat.upper() in myString.upper() else 0

#print(solution(myString, pat))