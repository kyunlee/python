# 9-1 : 개미 군단 1

hp = 24
def solution(hp):
    return hp//5+(hp%5)//3+((hp%5)%3)//1

#print(solution(hp))


# 9-2 : 모스부호

letter = ".... . .-.. .-.. ---"

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    return  "".join([morse[i] for i in letter.split()])

#print(solution(letter))

# 9-3 : 가위 바위 보

rsp = "205"
def solution(rsp):
    answer = {'2':'0', '0':'5', '5':'2'}   
    return ''.join([answer[i] for i in rsp])

#print(solution(rsp))

#9-4 : 구슬을 나누는 경우의 수

balls = 30
share = 10

import math

def solution(balls, share):
    return math.comb(balls,share)

print(solution(balls, share))

#30045015