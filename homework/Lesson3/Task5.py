# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input("введите число:"))

def fibb(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibb(n-1) + fibb(n-2)

def neg_fibb(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
   
    return neg_fibb(n+2) - neg_fibb(n+1)

list_fibb = []
for i in range(-N,0):
    list.append(list_fibb, neg_fibb(i))
for i in range(N+1):
    list.append(list_fibb, fibb(i))
print("",list_fibb)
