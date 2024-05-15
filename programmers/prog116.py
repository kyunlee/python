# 1,2 대문자 소문자
myString = "aBcDeFg"
#print(myString.upper())
#print(myString.lower())

#2. 대문자 소문자 번갈아 바꾸기
strArr=["AAA","BBB","CCC","DDD"]

def solution(strArr):  
    return [j.lower() if i % 2 == 0 else j.upper()  for i,j in enumerate(strArr) ]
#print(solution(strArr))

#3. A강조하기

myString3 = "abstract algebra"

def solution(myString):
    answer =''
    for i in myString:
        if i == 'a':
            answer += i.upper()
        elif i == 'A':
            answer += i
        else:
            answer += i.lower()
    return answer

# 4.특정한 문자를 대문자로 바꾸기

my_string4 = "programmers"
alp = "p"

def solution(my_string, alp):
  return my_string.replace(alp,alp.upper())

print(solution(my_string4,alp))