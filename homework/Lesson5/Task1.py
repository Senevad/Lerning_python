# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string_input = "Мы любим животных и абвстараемся поддевабрживать тех из них, кому не абвпосчастливилось иметь ласабвковых хозяев и тёплый крвабов"

list_data = string_input.split()
inspect_data = lambda s, sample = "абв": sample in s
result_task = ""
for i in list_data:
    if inspect_data(i):
        list_data.remove(i)
for i in list_data:
    result_task += i + " "
print(result_task)