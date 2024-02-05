# While문

# while 문의 기분 구조
'''
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
'''
treeHit = 0 
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


# while문 만들기

prompt = """
   1. Add
   2. Del
   3. List
   4. Quit
Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while 문 강제로 빠져나가기

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#cofee.py

# while 문의 맨 처음으로 돌아가기
a = 0 
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)
