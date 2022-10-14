# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_string(string_data):
    string_data += " "
    coded_string = ""
    count = 1
    char = string_data[0]
    for i in range(1, len(string_data)):
        if string_data[i] == char:
            count += 1
        else:
            if count > 2:
                coded_string += str(count) + char
            else:
                coded_string += char * count
            char = string_data[i]
            count = 1
    return coded_string


def decode_string (coded_string):
    input_string = ""
    char_amount = ""
    for i in range(len(coded_string)):
        if coded_string[i].isdigit():
            char_amount = coded_string[i]
            input_string += coded_string[i+1] * (int(char_amount) - 1)
        else:
            input_string += coded_string[i]
        char_amount = ""
    return input_string

with open("homework/Lesson5/file_input.txt", "r") as file:
    input_string = file.read()

with open("homework/Lesson5/file_output.txt", "w") as file:
    file.write(encode_string(input_string))

print("Строка в файле:", input_string)
print("Кодированая строка:", encode_string(input_string))
print("Декодированая строка:",decode_string(encode_string(input_string)))