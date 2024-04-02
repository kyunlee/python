# 옷가게할인받기

price = 580000
def solution(price):
    answer = 0
    if price >= 100000 and price < 300000:
        answer = price*0.95
    elif price >= 300000 and price < 500000:
        answer = price*0.90
    else:
        answer = price*0.80
    return int(answer)

#print( solution(price) )


discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#print(discount_rates.items())

'''
for discount_price, discount_rate in discount_rates.items():
    if price >= discount_price:
         print(int(price * discount_rate))
'''

money = 15000
def solution(money): 
    return [ int(money//5500), money%5500]
#print(solution(money))

age= 23

#print(2022-(age-1))

num_list = [1, 2, 3, 4, 5]

def solution(num_list):
    answer = []
    for i in range(len(num_list)):
       answer.append(num_list[len(num_list)-1-i])
    return answer

#print(solution(num_list))


print(num_list[::-1])