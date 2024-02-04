#1.평균점수구하기
'''
국어 80
영어 75
수학 55
'''
a = 80
b = 75
c = 55
print('길동이평균=',(a+b+c)/3)

#2.홀수,짝수 판별하기
#자연수 13이 홀수인지, 짝수인지 판별할수 있는 방법에 대해 말해보자

a = 13 % 2
if a == 0:
    print('짝수')
else:
    print('홀수')

#3.주민등록번호 나누기
pin = "881120-1068234"
yymmdd = pin[0:6] #pin[:6]  
num = pin[7:15] #pin[7:]
print('yymmdd=',yymmdd)
print('num=',num)

#4.주민등록번호 인덱싱
pin = "881120-1068234"
print(pin[7])

#5.문자열 바꾸기
a = "a:b:c:d"
# 'a#b#c#d
#b = a[0]+'#'+a[2]+'#'+a[4]+'#'+a[6]
b= a.replace(":","#")
print(b)

#6.리스트 역순 정렬하기
#[1,3,5,4,2] 리스트를 [5,4,3,2,1]
a = [1,3,5,4,2] 
a.sort()
print('a=',a)
a.reverse()
print('a=',a)

#7.리스트를 문자열로 만들기
a = ['Life','is','too','short']
result = " ".join(a)
print(result)

#8.(1,2,3)튜플에 값 4를 추가하여 (1,2,3,4)를 만든 후 출력해보자
t1 = (1,2,3)
print(id(t1)) #a의 고유 주소 값 출력
t1 = t1+(4,)
print(t1)
print(id(t1)) #(4,)값이 더해진 후 a의 고유 주소 값 출력


#9.딕셔너리의 키
a =  dict()
print(a) # {}

a['name'] = 'python' #{'name': 'python'}
a[('a',)] = 'python' # {('a',): 'python'}
#a[[1]] = 'python'
'''
    a[[1]] = 'python'
    ~^^^^^
TypeError: unhashable type: 'list'
'''
a[250] = 'python'  #{250: 'python'}

#10.딕셔너리 값 추출하기
#딕셔너리 a에서 'B'에 해당하는 값을 추출해 보자.

a = {'A':90, 'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

#11.리스트에서 중복제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(aSet)
print(b)

#12.파이썬 변수
# 다음과 같이 a,b 변수를 선언한 수 a의 두번째 요솟값을 변경하면 b 값은 어떻게 될까?
# 그리고 이런 결과가 나타나는 이유를 설명해 보자.
a = b = [1, 2, 3]
a[1] = 4
print(b)