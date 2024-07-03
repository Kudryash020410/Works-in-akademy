my_field = ["*","*","*","*","*","*","*","*","*"]

global step_value 
step_value = 1

first_player = "x"
second_player = "o"

def end_game(my_field):
    if(my_field[0] == first_player and my_field[4] == first_player and my_field[8] == first_player):
        return 1
    elif(my_field[0] == first_player and my_field[1] == first_player and my_field[2] == first_player):
        return 1
    elif(my_field[3] == first_player and my_field[4] == first_player and my_field[5] == first_player):
        return 1
    elif(my_field[6] == first_player and my_field[7] == first_player and my_field[8] == first_player):
        return 1
    elif(my_field[0] == first_player and my_field[3] == first_player and my_field[6] == first_player):
        return 1
    elif(my_field[1] == first_player and my_field[4] == first_player and my_field[7] == first_player):
        return 1
    elif(my_field[2] == first_player and my_field[5] == first_player and my_field[8] == first_player):
        return 1
    elif(my_field[2] == first_player and my_field[4] == first_player and my_field[6] == first_player):
        return 1
    elif(my_field[0] == second_player and my_field[4] == second_player and my_field[8] == second_player):
        return 2
    elif(my_field[0] == second_player and my_field[1] == second_player and my_field[2] == second_player):
        return 2
    elif(my_field[3] == second_player and my_field[4] == second_player and my_field[5] == second_player):
        return 2
    elif(my_field[6] == second_player and my_field[7] == second_player and my_field[8] == second_player):
        return 2
    elif(my_field[0] == second_player and my_field[3] == second_player and my_field[6] == second_player):
        return 2
    elif(my_field[1] == second_player and my_field[4] == second_player and my_field[7] == second_player):
        return 2
    elif(my_field[2] == second_player and my_field[5] == second_player and my_field[8] == second_player):
        return 2
    elif(my_field[2] == second_player and my_field[4] == second_player and my_field[6] == second_player):
        return 2
    else:
        return 0
def show_field(mass):
    for i in range(9):
        if ((i == 3) or (i == 6)):
            print("\n")
        print(my_field[i], end="")
    print("\n")    
 
def step(value):
    global step_value
    if(value % 2 != 0):
        x = int(input("Ход крестика: \n"))
        step_value = step_value + 1
        return x
    else:
        y = int(input("Ход нолика: \n"))
        step_value = step_value + 1
        return y
    
def step_check(field, user_step):
    global step_value
    if (field[user_step - 1] != "*"):
        print("Место занято!\n")
        step_value = step_value - 1
        step(step_value)
    else:    
        if(step_value %2 == 0):
            field[user_step - 1] = first_player
        else:
                field[user_step - 1] = second_player
 
print("Здравствуй,это игра крестики-нолики:)")
print("Тут мы ходим по очереди")
print("Первый ход делает крестик")
print("Выбирай свободное место от 1 до 9")
show_field(my_field)

while True:
    if(step_value <= 5):
        move = step(step_value)
        step_check(my_field, move)
        show_field(my_field)
    elif((step_value >= 5) and (step_value <= 9)):
        end = end_game(my_field)
        if(end == 1):
            print("Победили крестики!")
            break
        elif(end == 2):
            print("Победили нолики!")
            break
        move = step(step_value)
        step_check(my_field, move)
        show_field(my_field)
    else:
        print("Ничья!")
        break
