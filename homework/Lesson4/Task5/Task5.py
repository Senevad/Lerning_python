# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def find_mulp(inp):
    mulp_inp = []
    for i in range(10):
        mulp_inp.append(inp[inp.find(f"X^{i}") - 1])
    mulp_inp[1] = inp[inp.find("X ") - 1]
    for i in inp:
        if i.isdigit() and i != "0":
            mulp_inp[0] = i
    for i in range(len(mulp_inp)):
        if mulp_inp[i] == " ":
            mulp_inp[i] = 0
    return mulp_inp

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

input_1 = open("homework/Lesson4/Task5/Task5_file_input1.txt","r")
input_2 = open("homework/Lesson4/Task5/Task5_file_input2.txt","r")

for line in input_1:
    mulp_input_1 = find_mulp(line)
for line in input_2:
    mulp_input_2 = find_mulp(line)

mulp_result = []
for i in range(len(mulp_input_1)):
    mulp_result.append(int(mulp_input_1[i]) + int(mulp_input_2[i]))

with open("homework/Lesson4/Task5/Task5_file_result.txt","w") as result_output:
    result_output.write(mulp_in_string(mulp_result))
    
input_1.close
input_2.close