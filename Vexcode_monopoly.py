 def Left_callback_0():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    motor_1.spin_for(REVERSE, 450, DEGREES)

def Foward_callback_0():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 400, DEGREES)

def Left_callback_1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 250, DEGREES)

def Foward_callback_1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 400, DEGREES)

def Right_callback_0():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 250, DEGREES)

def Right_callback_1():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    motor_5.spin_for(REVERSE, 450, DEGREES)

# system event handlers
Left(Left_callback_0)
Left(Left_callback_1)
Foward(Foward_callback_0)
Foward(Foward_callback_1)
Right(Right_callback_0)
Right(Right_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()