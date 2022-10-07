# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from Random_list_module import Random_list_float

list_data = Random_list_float(5,0,10)

min_float = 1
max_float = 0
for i in range(len(list_data)):
    list_data_float = list_data[i] % 1
    if list_data_float < min_float:
        min_float = list_data_float
    if list_data_float > max_float:
        max_float = list_data_float
print("результат:",round(max_float - min_float,4))