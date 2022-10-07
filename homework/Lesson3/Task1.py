# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from Random_list_module import Random_list

list_N = Random_list(5,0,10)

sum_list = 0 
for i in range(1,len(list_N),2):
    sum_list += list_N[i]
print ("Сумма равна:",sum_list)