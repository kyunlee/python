#딕셔너리 자료형
# 연관배열(asscociative array) 또는 '해시(hash) 라고 함.

# 딕셔너리와 리스트나 튜플의 차이?
# 순차적으로(sequential)해당 요솟값을 구하는지 않고 Key를 통해 Value를 얻음.
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}

dic = {'name':'pey', 'phone': '010-9999-1234', 'birth':'1118'}
print(dic)
print( dic['name'])
print(dic['phone'])
print(dic['birth'])

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
print(a)

a['name']='pey'
print(a)
a[3] = [1,2,3]
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# 딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey':10, 'julliest':99}
print(grade['pey'])

# 딕셔너리에서 Key는 고유한 값! 중복으로 존재할 수 없음.

# 딕셔너리 관련 함수
# Key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys()) 

for k in a.keys():
    print(k)

# dict_keys 객체를 리스트로 변환
print( list(a.keys()) ) # ['name', 'phone', 'birth']

# Value 리스트 만들기 - values
print( a.values() )

# Key, Value 쌍 얻기 - items
print( a.items() ) # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# Key:Value 쌍 모두 지우기 - clear
print( a.clear() )

# Key로 Value 얻기 -get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('nokey')) # None
#print(a['nokey'])      # KeyError: 'nokey'
print(a.get('nokey', 'foo'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
print( 'name' in a )
print( 'email' in a )