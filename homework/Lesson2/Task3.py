# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from ipaddress import summarize_address_range


N = int(input("Введиите n:"))
list_N = []
for i in range(1,N + 1):
    list.append(list_N, (1+ (1/i)**i) )
print ("Список n чисел последовательности:",list_N)
sum_N = 0
for i in list_N:
    sum_N += i
print("Сумма последовательности чисел:",sum_N)