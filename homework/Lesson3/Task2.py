# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from Random_list_module import Random_list

list_N = Random_list(5,0,10)

list_duo_mulp = []
for i in range(0,int((len(list_N)+1)/2)):
    list.append(list_duo_mulp,list_N[i]*(list_N[len(list_N)-i-1]))
print("Результат:", list_duo_mulp)