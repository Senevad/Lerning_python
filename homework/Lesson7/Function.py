def fun_1_write_all(data):
    print(*[x for x in data[0]])
    for i in range(len(data)):
        print("\n",*[data[i][x] for x in data[i]])

def fun_2_find_sec_name(data,sec_name):
    count = 0
    for i in range(len(data)):
        if data[i]["Фамилия"] == sec_name:
            print("\nМы нашли:",*[data[i][x] for x in data[i]])
            count += 1
    if count == 0:
        print("\nТакого нету")

def fun_3_find_phone(data,phone):
    count = 0
    for i in range(len(data)):
        if data[i]["Телефон"] == phone:
            print("\nМы нашли:",*[data[i][x] for x in data[i]])
            count += 1
    if count == 0:
        print("\nТакого нету")

def fun_4_add_data(filename,new_data):
   with open(filename, 'a', encoding='utf-8') as file:
    file.write("\n")
    file.write(new_data)

def fun_5_output(filename,data):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            list_data = " ".join([data[i][x] for x in data[i]])
            file.write(list_data)
            file.write("\n")
    
