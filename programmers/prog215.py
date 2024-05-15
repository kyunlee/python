# 1.영어가 싫어요
#"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
#{"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,"zero":0 }

numbers = "onefourzerosixseven"

def solution(numbers):
    numalp = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9","zero":"0" }

    for key, value in numalp.items():
        numbers= numbers.replace(key,value)
    return int(numbers)    

#print(solution(numbers))

#2.인덱스 바꾸기

my_string = "hello"
num1 = 1
num2 = 2

def solution(my_string, num1, num2):
    return my_string[:num1]+my_string[num2]+my_string[num1+1:num2]+my_string[num1]+my_string[num2+1:]

#print(solution(my_string, num1, num2))

#3.한번만등장한 문자

s = "abdc"
def solution(s):
    s=sorted(s)
    answer =''
    for i in s:
        if 1 == s.count(i):
            answer += i
    return answer
print(solution(s))

#4. 약수구하기
n = 24

# result = [1, 2, 3, 4, 6, 8, 12, 24]

def solution(n):
    answer =[]
    i = 0
    while i < n:
        i+=1
        if n%i == 0: 
            answer.append(i)

    return answer

#print(solution(n))