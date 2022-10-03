# Реализуйте алгоритм перемешивания списка.

from random import randint, shuffle


N = int(input("Введите длинну списка:"))
list_N = []
for i in range(N):
    list.append(list_N, randint(-N,N))
print ("Задан список:",list_N)
shuffle(list_N)
print ("Результат:",list_N)

# Если посложнее то

# N = int(input("Введите длинну списка:"))
# round_iter = int(input("Введите кол-во итераций перемешивания:"))
# list_N = []
# for i in range(N):
#     list.append(list_N, randint(-N,N))
# print ("Задан список:",list_N)
# for i in range(round_iter):
#     X = randint(0,N - 1)
#     Y = randint(0,N - 1)
#     list_N[X],list_N[Y] = list_N[Y],list_N[X]
# print ("Результат:",list_N)