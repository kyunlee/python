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

print(my_string[2:4][::])
print(my_string[2:3+1][::-1])

def solution(my_string, queries):
    answer = ''
    return answer

for i in queries:
    first = my_string[:i[0]]    

    if i[0] !=0:
        center = my_string[i[1]:i[0]-1:-1]         
    else:
        center = my_string[i[1]::-1]      
    end = my_string[i[1]+1:]

    my_string = first + center + end

    print('my_string=',my_string)
