'''
기초 day3-1
길이가 같은 두 문자열 str1과 str2가 주어집니다.
두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
'''
str1 = 'aaaaa'
str2 = 'bbbbb'

def solution(str1, str2):
    answer = ''    
    result = zip(str1,str2)
    for i  in list(result):
        answer = answer + ''.join(i) 
    return answer

print('answer_3-1=', solution(str1, str2) )

'''
기초 day3-2
문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.
'''
arr= ["a","b","c"]

def solution(arr):
    answer = ''.join(arr)
    return answer

print('answer_3-2=', solution(arr) )

'''
기초 day3-3
문자 리스트를 문자열로 변환하기
문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.
'''
my_string = "string"
k = 3

def solution(my_string, k):
    answer = my_string*k
    return answer

print('answer_3-3=',solution(my_string, k))

'''
기초 day3-4
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
'''
a = 2
b = 91


def solution(a, b):
    stra=str(a)
    strb=str(b)
    re1=int(stra+strb)
    re2=int(strb+stra)
    if re1 > re2 or re1 == re2:
        answer = re1
    else:
        answer = re2
    return answer

print('answer_3-4=',solution(a, b))

# 다른사람풀이
#   return int(max(f"{a}{b}", f"{b}{a}"))

'''
기초 day3-4
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.
'''

def solution(a, b):
    return max(int(f"{a}{b}"),a*b*2)

print('answer_3-5=',solution(a, b))