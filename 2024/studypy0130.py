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

