# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num_data = int(input("введите число:"))

list_num = []
while num_data != 0:
    list_num.insert(0, num_data % 2)
    num_data = int(num_data/2)
result_num = 0
for i in list_num:
  result_num = result_num * 10 + i
print("Результат:",result_num)