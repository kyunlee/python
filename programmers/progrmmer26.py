#문자열 뒤집기
my_string = "jaron"
#print( my_string[::-1] )

#지각삼각형 출력하기

n= 3
for i in range(1,n+1):
    print('*'*(i))
#print('\n'.join('*' * (i + 1) for i in range(int(input()))))

#짝수 홀수 개수
    
num_list = [1,2,3,4,5]

answer = [len( [ num for num in num_list if num %2 == 0] ),len( [ num for num in num_list if num %2 != 0] )]
#print(answer)

#문자 반복 출력하기
my_string = "hello"
n = 3

answer = ''
for i in my_string:
    answer += i*n

#print(answer )
    

