a=2
b=6
c=1
temp =[]
temp.append(a)
temp.append(b)
temp.append(c)
print(temp)

setnum = set(temp)
answer = 1
#print("setnum",setnum)
print(len(setnum))

for i in range(1,5-len(setnum)) :
   print('i=',i)
   answer *= (a ** i) + (b ** i) + (c ** i)

print(answer)
