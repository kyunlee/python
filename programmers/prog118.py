# x 사이의 개수

myString = "oxooxoxxox"

def solution(myString):        
    return  [len(i) for i in myString.split("x")]

print(solution(myString))

# 문자열 잘라서 정렬하기

myString2 = "dxccxbbbxaaaa"

def solution(myString):
    return  sorted([i for i in myString.split("x") if ''!= i])

print(solution(myString2))

# 문자열 바꿔서 찾기

myString3 = "AAABBAAA"
pat = "BBB"

def solution(myString, pat):
    answer = ""
    for i in myString:
        if i == "A":
            answer += "B"
        elif i == "B":
            answer += "A"

    if answer.count(pat) >= 1:
        return 1
    else:
        return 0
    
print(solution(myString3,pat))

# rny_string

rny_string = "masterpiece"

def solution(rny_string):    
    return rny_string.replace("m","rn")

print(solution(rny_string))