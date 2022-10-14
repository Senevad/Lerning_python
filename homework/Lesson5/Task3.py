# Создайте программу для игры в ""Крестики-нолики"".

list_field = [i for i in range(1,10)]
def print_field():
    print(list_field[0],"|",list_field[1],"|",list_field[2])
    print("----------")
    print(list_field[3],"|",list_field[4],"|",list_field[5])
    print("----------")
    print(list_field[6],"|",list_field[7],"|",list_field[8])

def check_win(field):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_coord:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def take_input(player_sign):
    valid = False
    while not valid:
        player_answer = int(input(f"Куда поставим {player_sign}?:"))
        if player_answer >= 1 and player_answer <= 9:
            if (str(list_field[player_answer-1]) not in "XO"):
                list_field[player_answer-1] = player_sign
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")    

counter = 0
win = False
while not win:
    print_field()
    if counter % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    counter += 1
    if counter > 4:
        tmp = check_win(list_field)
        if tmp:
            print (tmp, "выиграл!")
            win = True
            break
    if counter == 9:
        print ("Ничья!")
        break
print_field()