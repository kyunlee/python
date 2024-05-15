# 1. 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

myString = "AAAAaaaa"
pat = "a"

def solution(myString, pat):    
    return myString[:myString.rindex(pat)+len(pat)]

#print( solution(myString,pat))

# 2. 문자열이 몇 번 등장하는지 세기
myString = "banana"
pat = "ana"

def solution(myString, pat):
    count = 0
    for x in range(0,len(myString)):
        if myString[x:x+len(pat)] == pat:
            count+=1
    return count

#print(solution(myString, pat))

#3. ad제거하기
strArr =['and', 'notad', 'abcd', 'ad1', 'ad2']
def solution(strArr):
    answer =[]
    for i in strArr:
        if "ad" not in i:
            answer.append(i)
    return answer

print(solution(strArr))

# 4. 공백으로 구분하기1
my_string4 = "i love you"

def solution(my_string):
    return my_string.split(" ")

#print(solution(my_string4))

# 5. 공백으로 구분하기2
my_string5= " i    love  you"

def solution(my_string):
    return ' '.join(my_string.split()).split(" ")

print(solution(my_string5))