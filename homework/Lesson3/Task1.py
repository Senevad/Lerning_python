# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

N = int(input("Введите длинну списка:"))
list_N = []
for i in range(N):
    list.append(list_N, randint(0,10))
print ("Задан список:",list_N)

sum_list = 0 
for i in range(1,len(list_N),2):
    sum_list += list_N[i]
print ("Сумма равна:",sum_list)