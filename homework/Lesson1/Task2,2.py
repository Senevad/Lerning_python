# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

num_X =int(input("X = "))
num_Y =int(input("Y = "))
if num_X > 0 and num_Y > 0:
    print("точка в 1 четверти")
elif num_X < 0 and num_Y > 0:
    print("точка в 2 четверти")
elif num_X < 0 and num_Y < 0:
    print("точка в 3 четверти")
elif num_X > 0 and num_Y < 0:
    print("точка в 4 четверти")