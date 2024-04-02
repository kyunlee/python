# 9-2 배열 만들기 5
intStrs = ["0123456789","9876543210","9999999999999"]
k = 50000
s = 5
l = 5

def solution(intStrs, k, s, l):
    return [int(i[s:s+l]) for i in intStrs if k < int(i[s:s+l])]

#print(solution(intStrs, k, s, l))

# 9-2부분 문자열 이어 붙여 문자열 만들기

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]

def solution(my_strings, parts):
    [j[parts[i][0]:parts[i][1]+1]  for i,j in enumerate(my_strings)]
    return ''.join([ j[parts[i][0]:parts[i][1]+1] for i,j in enumerate(my_strings)])

#print(solution(my_strings, parts))

# 9-3 문자열의 뒤의 n글자
my_string = "ProgrammerS123"
n = 11

def solution(my_string, n):    
    return my_string[len(my_string)-n:]

print(solution(my_string, n))