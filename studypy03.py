#리스트
a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1, 2, 3]
a.index(3)
print(a)

a = [1, 2, 3]
a.insert(0,4)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)   #값으로 삭제 
print('remove',a)

a = [1, 2, 3]
a.pop()  #pop index로 삭제 값
print('pop',a)

a = [1, 2, 3, 1]
a.count(1)
print(a)

a = [1, 2, 3]
a.extend([4, 5])
print(a)