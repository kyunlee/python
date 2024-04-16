# 문자 개수 세기

my_string = "Programmers"

alphabet = [0]*52
print(alphabet)
#0 - 65
#27 = 97 - 70

def solution(my_string):
    alphabet = [0]*52
    for char in my_string:
        if(char.isupper()):
            alphabet[(ord(char)-65)] = alphabet[(ord(char)-65)] +1
        else:
            alphabet[(ord(char)-71)] = alphabet[(ord(char)-71)] +1

    return alphabet

print(solution(my_string))

# 배열 만들기 1
n = 10
k = 3

def solution(n, k):
    return [i for i in range(1,n+1) if i%k == 0]

#print(solution(n,k))

# 글자 지우기
my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]

def solution(my_string, indices):
    listms=list(my_string)
    indices.sort()
    for i in sorted(indices,reverse=True):
        del listms[i]
    return ''.join(listms)

#print(solution(my_string, indices))

# 카운트다운
start_num = 10
end_num = 3

def solution(start_num, end_num):
    return [i for i in range(start_num, end_num-1,-1)]
#print(solution(start_num, end_num))

# 가까운 1찾기 
arr = [1, 1, 1, 1, 0]
idx = 3

def solution(arr, idx):
    for i,j in enumerate(arr):
        if j==1 and i >= idx:
            return i
    return -1

#print(solution(arr,idx))
