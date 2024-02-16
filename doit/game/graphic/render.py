#from doit.game.sound.echo import echo_test
from ..sound.echo import echo_test

'''
접근자  설명
   ..   부모 디렉터리를 의미한다.
    .   현재디렉터리를 의미한다
'''

def render_test():
    print("render")
    echo_test()