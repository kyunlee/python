'''
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 
다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.
'''
x1 = True
x2 = False
x3 = False
x4 = False

def solution(x1, x2, x3, x4):
    return all([any([x1,x2]),any([x3,x4])]) 

#print(solution(x1, x2, x3, x4))

#print(all([True,True]),any([True,True]))
#print(all([True,False]),any([True,False]))
#print(all([False,True]),any([False,True]))
#print(all([False,False]),any([False,False]))

'''
글자 이어 붙여 문자열 만들기
'''
my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]

answer=[]
for i in index_list:
    answer.append(my_string[i])

#print("".join(answer))

#print("".join([my_string[i] for i in index_list]))
#print("".join(list(map(lambda a :my_string[a], index_list))))

'''
9로 나눈 나머지
'''
number = "123"

def solution(number):
    answer = 0
    return answer

#print(sum(int(i) for i in number)%9)

'''
문자열 여러 번 뒤집기 
'''

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

#print(my_string[2:4][::])
#print(my_string[2:3+1][::-1])

def solution(my_string, queries):
    for i in queries:
        first = my_string[:i[0]]    

        if i[0] !=0:
            center = my_string[i[1]:i[0]-1:-1]         
        else:
            center = my_string[i[1]::-1]      
        end = my_string[i[1]+1:]

        my_string = first + center + end
    return my_string
    print('my_string=',my_string)

'''
def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)
[출처] #6. Python 기초 트레이닝(+근황?현황?)|작성자 meee
'''
'''
주사위게임3
'''
a = 2
b = 5
c = 2
d = 6

def solution(a, b, c, d):
    nums = [a,b,c,d]
    counts = [nums.count(i) for i in nums]  
    answer = 0
    print( counts )
    if max(counts) == 4:
        answer = 1111*a
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        answer = (10*p+q)**2
    elif max(counts) == 2:
        if min(counts) == 2: 
            if a == b:
                answer = (a+c)*abs(a-c) 
            else: answer = (a+b)*abs(a-b)
        else:
            p = nums[counts.index(2)]
            answer = (a*b*c*d)/p**2
    else:
        answer = min(nums)
    return answer

print(solution(a, b, c, d))

