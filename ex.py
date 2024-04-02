'''
age = 40
print(2022-int(age))
print((2022-(age-1)))
'''

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]


def solution(my_string, queries):
    answer=list(my_string)
    print(answer)
    for s,e in queries:
        print(s,e)
        print(answer[s:e+1])
        print(answer[s:e+1][::-1])
        answer[s:e+1]=answer[s:e+1][::-1]
        print(answer[s:e+1])
    return ''.join(answer)

print(solution(my_string, queries))