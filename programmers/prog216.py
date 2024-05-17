# 가장 큰 수 찾기

array = [1,8,3]

def solution(array):    
    return [max(array),array.index(max(array))]

print(solution(array))

# 문자열 계산기
my_string = "3+4"
def solution(my_string):
    return eval(my_string)

print(solution(my_string))

# 배열의유사도
s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]

def solution(s1, s2):
    s1= set(s1)
    s2= set(s2)
    return len(s1.intersection(s2))

print(solution(s1,s2))