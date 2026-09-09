screen_precision = 0
console_precision = 0
Foward = Event()
Left = Event()
Right = Event()
myVariable = 0
dice1 = 0
dice2 = 0
spaces_to_move = 0
current_space_number = 0

def roll_dice():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()

def move():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def play_game():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(5, MSEC)

def complete_task():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def Foward_callback_0():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def when_started1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    current_space_number = 1
    play_game()

def Left_callback_0():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def Right_callback_0():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def when_started2():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def Foward_callback_1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def Left_callback_1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def Right_callback_1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

# system event handlers
Foward(Foward_callback_0)
Foward(Foward_callback_1)
Left(Left_callback_0)
Left(Left_callback_1)
Right(Right_callback_0)
Right(Right_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
when_started1()
