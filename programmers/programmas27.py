my_string = "BCBdbe"
letter ="B"

def solution(my_string, letter):        
    return my_string.replace(letter,'')

#print(solution(my_string,letter))

angle = 180
answer = 0

'''
if angle == 180:
    answer = 4
elif angle < 180:
    answer = 3
elif angle == 90:
    answer = 2
elif angle < 90:
    answer =1
'''
#print( [[1, 2], [3, 4]][angle > 90][angle % 90 == 0])


#n이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 

n=10

print( sum (i for i in range(0,n+1,2)) )

