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

def complete_task():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    brain.screen.print(str("LandedSpace") + str(current_space_number))
    brain.screen.next_row()
    wait(1, SECONDS)
    if current_space_number == 1:
        # Space = GO
        for repeat_count in range(4):
            Left.broadcast_and_wait()
            wait(5, MSEC)
    elif current_space_number == 4:
        # Space = Jail
        wait(3, SECONDS)
    elif current_space_number == 7:
        # Space = Free parking
        wait(5, SECONDS)
    elif current_space_number == 10:
        # Space = Go to Jail
        Right.broadcast_and_wait()
        for repeat_count2 in range(3):
            Foward.broadcast_and_wait()
            wait(5, MSEC)
        Left.broadcast_and_wait()
        for repeat_count3 in range(3):
            Foward.broadcast_and_wait()
            wait(5, MSEC)
        for repeat_count4 in range(2):
            Right.broadcast_and_wait()
            wait(5, MSEC)
        current_space_number = 4
        wait(1, SECONDS)
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        Right.broadcast_and_wait()
        Foward.broadcast_and_wait()
        for repeat_count5 in range(2):
            Left.broadcast_and_wait()
            wait(5, MSEC)
        Foward.broadcast_and_wait()
        Right.broadcast_and_wait()

def move():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    brain.screen.print(str("moving") + str(str(spaces_to_move) + str("spaces")))
    brain.screen.next_row()
    for repeat_count6 in range(int(spaces_to_move)):
        Foward.broadcast_and_wait()
        current_space_number = current_space_number + 1
        if current_space_number > 12:
            current_space_number = 1
        if current_space_number == 1:
            Right.broadcast_and_wait()
        if current_space_number == 4:
            Right.broadcast_and_wait()
        if current_space_number == 7:
            Right.broadcast_and_wait()
        if current_space_number == 10:
            Right.broadcast_and_wait()
        wait(5, MSEC)

def roll_dice():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 5), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    spaces_to_move = dice1 + dice2

def play_game():
    global FWD, LT, RT, my_event, Foward, Left, Right, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(3, SECONDS)
        brain.screen.set_cursor(1, 1)
        brain.screen.clear_row(4)
        brain.screen.set_cursor(brain.screen.row(), 1)
        wait(5, MSEC)