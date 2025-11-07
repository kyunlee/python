
answer = ''
input_string = "edeaaabbccd" #"de"

#for i in range(len(input_string)-1):
#    if input_string[i] == input_string[i+1]:
'''
lonely = []
n = len(input_string)
print("n=",n)

for i, ch in enumerate(input_string):
    print(i, ch)
    if (i == 0 or input_string[i-1] != ch) and (i == n-1 or input_string[i+1] != ch):
        lonely.append(ch)
    
    print(dict.fromkeys(lonely))

apcon = set()
lonely = set()
pre = ''

for ch in input_string:
    if ch not in pre:
        pre = ch
    
    if ch in apcon:
        lonely.add(ch)
        apcon.add(ch)

print(''.join(sorted(lonely)) )
'''
#if not in lonely:
#    print("N")
#else:



seen = set()          # 이미 지나간 문자
lonely = set()        # 외톨이로 판정된 문자

prev = ''
for ch in input_string:
    if ch != prev:           # 새 덩어리 시작
        if ch in seen:       # 이전에 등장했는데, 새로운 덩어리면 외톨이
            lonely.add(ch)
        seen.add(ch)
        prev = ch

print(''.join(sorted(lonely)) )