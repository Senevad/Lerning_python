# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from Random_list_module import Random_list

list_data = Random_list(5,0,5)

list_result = []
for i in list_data:
    count = 0
    for j in list_data:
        if i == j:
            count += 1
    if count == 1:
        list_result.append(i)
print("результат:",list_result)