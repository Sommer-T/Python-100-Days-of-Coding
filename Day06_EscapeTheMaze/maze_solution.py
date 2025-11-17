# NOTE:
# These functions are normally provided by Reeborg's World in the browser.
# Here they are just placeholders so this file is valid Python and PyCharm
# doesn't complain about undefined names.

def move():
    pass

def turn_left():
    pass

def right_is_clear():
    return False

def front_is_clear():
    return False

def at_goal():
    return False

def turn_right():
    # usage only in Reeborg
    # 3 left turns = right turn
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()