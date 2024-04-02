'''
입문 3-1
정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
'''
num1 = 10
num2 = 5

def solution(num1, num2):
    answer = num1 % num2
    return answer

print('answer3-1=',solution(num1, num2) )

'''
입문3-1
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
'''
array = [2,2,10,11,7]
#array = [9,-1,0]

def solution(array):
    array.sort()
    return  array[len(array) // 2]

print('answer3-2=',solution(array) )

'''
입문3-1
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
'''
array = [1,  3, 3, 5,5,5, 4, 4] # 5
#array = [1, 1, 2, 2] #-1	
#array = [1]	# 1

'''
def solution2(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
            print("■■■■■■■■■■")
            print(f"i : {i}")
            print(f"a : {a}")
            print("■■■■■■■■■■")
        print(f"result : +{array}")
        print(f"i : {i}")       
        if i == 0: return a 
    return -1


print('answer3-이야=',solution2(array))
'''
from collections import Counter

def solution(array):
    counter = Counter(array)
    print(counter)
    # Counter({3: 3, 4: 2, 1: 1, 2: 1})
    
    print('len(counter.keys())=',len(counter.keys()))
    if len(counter.keys()) > 1:
        if counter.most_common()[0][1] ==  counter.most_common()[1][1]:
            answer = -1
        else:
            answer = counter.most_common(1)[0][0]
        
    else:
        answer = array[0]
    return answer


print('answer3-3=',solution(array))

'''
입문 3-4
짝수는 싫어요
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

'''

n= 15

def solution(n):
    answer=[]
    for i in range(1,n+1):
        if((i) % 2 != 0):
            answer += (i,)
    return answer

print('answer3-4=',solution(n))

###

anwer123 = [i for i in range(1, n+1, 2)]
print('anwer123=',anwer123)