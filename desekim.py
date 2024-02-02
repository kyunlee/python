#평균점수구하기
'''
국어 80
영어 75
수학 55
'''
print('길동이평균=',(80+75+55)/3)

#홀수,짝수 판별하기
#자연수 13이 홀수인지, 짝수인지 판별할수 있는 방법에 대해 말해보자

a = 13 % 2
if a == 0:
    print('짝수')
else:
    print('홀수')

#주민등록번호 나누기
pin = "881120-1068234"
yymmdd = pin[0:6]   
num = pin[7:15]
print('yymmdd=',yymmdd)
print('num=',num)

#주민등록번호 인덱싱
pin = "881120-1068234"
print(pin[7])

#문자열 바꾸기
a = "a:b:c:d"
# 'a#b#c#d
b = a[0]+'#'+a[2]+'#'+a[4]+'#'+a[6]
print(b)

#리스트 역순 정렬하기
#[1,3,5,4,2] 리스트를 [5,4,3,2,1]
a = [1,3,5,4,2] 
a.sort()
print('a=',a)
a.reverse()
print('a=',a)

#리스트를 문자열로 만들기
a = ['Life','is','too','short']
result = " ".join(a)
print(result)

#(1,2,3)튜플에 값 4를 추가하여 (1,2,3,4)를 만든 후 출력해보자

