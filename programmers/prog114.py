# 1. 홀수 vs 짝수

num_list = [4, 2, 6, 1, 7, 6]

def solution(num_list):
    짝 = 0
    홀 = 0
    for i,j in enumerate(num_list):
        if i % 2 == 0:
            짝 += j
        else:
            홀 += j

    return 짝 if 짝 > 홀 else 홀

#print(solution(num_list))

# 2. 5명씩

names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]

def solution(names):
    return names[::5]

#print(solution(names))

# 3. 할 일 목록

todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]

def solution(todo_list, finished):
    return [j for i,j in enumerate(todo_list) if finished[i]==False ]

#print(solution(todo_list, finished))

# 4. n보다 커질 때까지 더하기
numbers = [34, 5, 71, 29, 100, 34]
n = 123

def solution(numbers, n):
    sum = 0
    for i in numbers:
        sum += i
        if sum > n:
            return sum

#print(solution(numbers, n))

# 5. 수열과 구간 쿼리 1

arr = [0, 1, 2, 3, 4]
queries = [[0, 1],[1, 2],[2, 3]]

def solution(arr, queries):
    for i in queries:       
        for j in range(i[0],i[1]+1):
            if i[0] <= j <= i[1]: 
                arr[j] +=1
    return arr  
print(solution(arr, queries))