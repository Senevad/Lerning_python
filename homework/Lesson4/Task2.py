# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

N = int(input("Введите N:"))
list_N = []
while N % 2 == 0:
    list.append(list_N,2)
    N /= 2
for i in range(3,int(math.sqrt(N))+1,2):
    while N % i== 0:
        list.append(list_N,i)
        N /= i
if N > 2:
    list.append(list_N,int(N))
print("Результат:",list_N)