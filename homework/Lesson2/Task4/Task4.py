# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

N = int(input("Введите N:"))
list_N = []
for i in range(N):
    list.append(list_N, randint(-N,N))
print ("Задан список:",list_N)
file_N = open("homework/Lesson2/Task4/file.txt","r")
mulp_N = 1
for i in file_N:
    if int(i) >= len(list_N):
        print(f"позиции {int(i)} нет, она не будет учитываться.")
    else:
        mulp_N *= list_N[int(i)]
print("Произведение заданых элементов равно:",mulp_N)
file_N.close()