numbers=[1, 2, -3, 4, -5]

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(abs(i))    
    answer = sorted(answer, reverse=True)
    return answer[0]*answer[1]

#print(solution(numbers))


i = 1
j = 13
k = 1
def solution(i, j, k):
    return sum(str(num).count(str(k))for num in range(i,j+1))

#print(solution(i, j, k))

my_string = "aAb1B2cC34oOp"

def solution(my_string):
    s =''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(char) for char in s.split())

#print(solution(my_string))

spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]

def solution(spell, dic):
    spell= set(spell)
    for i in dic:
        if spell & set(i):
            answer =1
        else:
            answer =2
    return answer

#print(solution(spell, dic))

chicken =1081

def solution(chicken):    
    return chicken // 10

#print(solution(chicken))


babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]


def solution(babbling):
    joka = ["aya", "ye", "woo", "ma" ]
    count = 0
    for i in babbling:       
        for j in joka:
            i=i.replace(j," ")
        if i.strip()=="":
            count +=1
    return count

print(solution(babbling))