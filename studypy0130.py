#문자열 자료형
print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

print("Python's favorite food is perl")
say1 = '"Python is very easy." he says.'
print('say1 = ',say1)

food =  'Python\'s favorite food is perl'
say2 = "\"Python is very easy.\" he says."
print('food = ',food)
print('say2 = ',say2)

multiline = "Life is too short\nYou need python"
print('multiline = ',multiline)

#문자열 더하기 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

#문자열 곱하기
a = "python"
print(a*2)

#문자열 길이 구하기
a = "Life is too short"
print(len(a))

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
#파이썬은 0부터 숫자를 센다.

print([a[0]])
print(a[12])
print(a[-1])
print(a[-2])
print(a[-5])

a = "Life is too short, You nedd Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[19:])
print(a[:])
print(a[19:-7])

#Pithon 문자열을 Python으로 바꾸려면?
a = "Pithon"
print(a[1])
#a[1] = 'y' --오류

print(a[:1])
print(a[2:])
print( a[:1]+ 'y' + a[2:] )

#문자열 포매팅
#숫자대입
print("I eat %d apples." % 3)
#문자열대입
print("I eat %s apples." % "five")
#숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." %number)
#2개 이상의 값 넣기
number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days." % (number,day))

#포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
print("Error is %d%%." % 98)

#정렬과 공백
print("%10s" % "hi")      #         hi
print("%-10sjane." %'hi') #hi        jane.
#hi를 왼쪽으로 정렬하고 나머지는 공백으로 채웠다는 것을 알 수 있다.

#소수점 표현하기
print("%0.4f" % 3.42134234)  #3.4213
print("%10.4f" % 3.42134234) #    3.4213

#format 함수를 사용한 포매팅
print("I eat {0} apples." .format(3))
print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples" .format(number))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))

print("I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days." .format(10,day=3))

#왼쪽정렬
print("{0:<10}" .format("hi"))
#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞춤
#오른쪽정렬
print("{0:>10}".format("hi"))
#오른쪽 정렬은 :< 대신 :>을 사용하면 됨.
#가운데 정렬
print("{0:^10}".format("hi"))
#출력결과
'''
hi
        hi
    hi
'''