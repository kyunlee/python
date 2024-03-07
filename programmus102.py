#문자열 겹쳐쓰기

my_string = "Program29b8UYP"
overwrite_string = "merS123"
s = 7
'''
my_string = "He11oWor1d"
overwrite_string = "lloWorl"
s = 2

print(my_string[:s])
print(len(my_string))
print(len(overwrite_string))
print(s+len(overwrite_string))
print(len(my_string)-(s+len(overwrite_string)))

print(my_string[s+len(overwrite_string):])

'''
def solution(my_string, overwrite_string, s):
    answer = my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
    return answer

result = solution(my_string,overwrite_string,s)

print(result)

# 숫자비교하기
num1 = 2
num2 = 3
def solution(num1, num2):
    if int(num1)==int(num2):
        answer = 1
    else:
        answer = -1
    return answer

print(solution(num1, num2))