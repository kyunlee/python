# 1. 컨트롤 제트
s = "10 Z 20 Z 1"

def solution(s):
    sum = 0
    str = s.split()
    for i,j in enumerate(str):
        if 'Z' == j:
            sum -= int(str[i-1])
        else:
            sum += int(j)
    return sum

print(solution(s))


# 2.배열 원소의 길이

strlist = ["We", "are", "the", "world!"]

def solution(strlist):
    return [ len(i) for i in strlist]

#print(solution(strlist))

# 3. 중복된 문자 제거 

my_string = "We are the world"

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

#print(solution(my_string))


# 4. 삼각형의 완성조건 (1)

sides = [3, 6, 2]
def solution(sides):
    sides.sort() 
    return 1 if sides[0]+sides[1] > sides[2] else 2

#print(solution(sides))