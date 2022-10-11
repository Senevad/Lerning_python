# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from Random_list_module import Random_list

k = int(input("Введите k:"))
list_rand_data = Random_list(k + 1,0,5)

def mulp_in_string(list_data):
    list_result = []
    result_task = ""
    for i in range(len(list_data)):
        if list_data[i] != 0:
            if i == 0:
                list_result.insert(0,f"{list_data[i]}")
            elif i == 1:
                list_result.insert(0,f"{list_data[i]}X")
            else:
                list_result.insert(0,f"{list_data[i]}X^{i}")
    for i in range(len(list_result)-1):
        result_task += list_result[i] + " + "
    result_task += list_result[-1] + " = 0"
    return result_task

with open("homework/Lesson4/Task4/Task4_file.txt", "w") as data:
    data.write(mulp_in_string(list_rand_data))