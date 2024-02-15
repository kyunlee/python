# 클래스

# calculator.py
result1 = 0
result2 = 0

def add1(num): # 계산기1
    global result1
    result1 += num # 결괏값(result)에 입력값(num) 더하기
    return result1  # 결괏값 리턴

def add2(num): # 계산기2
    global result2
    result2 += num
    return result2


print( add1(3) )
print( add1(4) )
print( add2(3) )
print( add2(7) )

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self,num):
        self.result -= num
        return self.result
    
# 클래스와 객체
# 과자틀 = 클래스
# 과자 틀로 찍어 낸 과자 = 객체    
    
class Fourcal:
#    pass
    def setdata(self, first, second): # 메서드의 매개변수
        self.first = first            # 메서드의 수행문
        self.second = second          # 메서드의 수행문
    def add(self):
        result = self.first + self.second
        return result
# 곱하기, 빼기, 나누기 기능 만들기
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = Fourcal()

'''
def 함수_이름(매개변수):
    수행할_문장
'''

a. setdata(4,2)              

#메서드를 호출하는 또 다른 방법
# ‘클래스명.메서드’ 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해야 한다
Fourcal.setdata(a, 4, 2)

# ‘객체.메서드’ 형태로 호출할 때는 self를 반드시 생략해서 호출
a.setdata(4, 2)

# 객체만의 변수를 ‘객체변수’ 또는 ‘속성’이
print(a.first)
print(a.second)

b = Fourcal()
b.setdata(3,7)
print(b.first)

print(a.add())
print(b.add())

print(a.mul())
print(a.sub())
print(a.div())
print(b.div)

# 생성자

a = Fourcal()
#a.add()
'''
Traceback (most recent call last):
  File "d:\python\python-1\20240215.py", line 45, in add
  File "d:\python\python-1\20240215.py", line 45, in add
    result = self.first + self.second
             ^^^^^^^^^^
AttributeError: 'Fourcal' object has no attribute 'first'
'''
# FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 먼저 수행하면 ‘AttributeError: 'FourCal' object has no attribute 'first'’오류가 발생
# 객체에 first, second와 같은 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다 생성자를 구현하는 것이 안전한 방법

print(type(a)) # <class '__main__.Four

# 생성자(constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미
# 파이썬 메서드명으로 __init__를 사용하면 이 메서드는 생성자가 됨

class Fourcal2:
#    pass
    def __init__(self, first, second):
        self.first = first
        self.second = second    
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# __init__로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이
#a = Fourcal2()
'''
TypeError: Fourcal2.__init__() missing 2 required positional arguments: 'first' and 'second'
'''

a = Fourcal2(4,2)
print(a.first)
print(a.add())
print(a.div())

# 클래스의 상속
# 상속(Inheritance)이란 ‘물려받다’라는 뜻으로, ‘재산을 상속받다’라고 할 때의 상속과 같은 의미
# class 클래스_이름(상속할_클래스_이름)

class MoreFourCal(Fourcal2):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(6,7)
print(a.add())
print(a.pow())

# 메서드 오버라이딩 : 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
class SafeFourCal(Fourcal2):
    def div(self):
        if self.second == 0 : # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "김" # Family 클래스에 선언한 lastname이 바로 클래스변수

#  클래스_이름.클래스변수로 사용
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

a.lastname = "최"

print(a.lastname)  # a.lastname 객체변수 최
print(b.lastname)      # 박
print(Family.lastname) # 박


