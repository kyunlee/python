# 패키지
#파이썬에서 패키지(packages)란 관련 있는 모듈의 집합
'''
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
'''

# 패키지 안의 함수 실행하기
import doit.game.sound.echo

doit.game.sound.echo.echo_test()

from doit.game.sound import echo

echo.echo_test()

from doit.game.sound.echo import echo_test
echo_test()

# __init__.py의 용도
# 패키지 변수 및 함수 저의 
import doit.game
print(doit.game.VERSION)

doit.game.print_version_info()

# 패키지 내의 모듈을 미리 import 
import doit.game
doit.game.render_test()
 
# 패키지 초기화
import doit.game

from doit.game.graphic.render import render_test

#단 초기화 코드는 한번 실행된 후에는 다시 import를 수해하더라고 실행되지 않음
'''
Initializing game...
echo
echo
echo
3.5
The version of this fame is 3.5.
render
'''

# __all__
from doit.game.sound import *
echo.echo_test()

# relative 패키지
from doit.game.graphic.render import render
render_test()