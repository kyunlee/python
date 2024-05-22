# 7개의 개수

array = [7,77,17]

def solution(array):
    return str(array).count(str('7'))
        

#print(solution(array))

# 잘라서 뱅열로 저장하기

my_str = "abc1Addfggg4556b"
n = 6

def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]

#print(solution(my_str, n))

# 중복된 숫자 개수

array = [0, 10]
n = 0

ct = 0
for i in array:
    if i == n: ct +=1

#print (ct)

# 머쓱이보다 키 큰 사람
array = [149, 180, 192, 170]
height = 167

def solution(array, height):
    answer = 0
    array.sort()
    for i,j in enumerate(array):
        if j > height: return len(array)- i
    return answer

print(solution(array, height))