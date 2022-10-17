from random import randint, random

# def Random_list (N,min,max):
#     list_N = []
#     for i in range(N):
#         list.append(list_N, randint(min,max))
#     print ("Задан список:",list_N)
#     return list_N

# def Random_list_float (N,min,max):
#     list_float = []
#     for i in range(N):
#         list.append(list_float, (randint(min,max) + round(random(),4)))
#     print ("Задан список:",list_float)
#     return list_float

# улучшение рандомного создания списков с помощью новых функций

def Random_list (N,min,max):
    list_N = [randint(min,max) for i in range(N)]
    print ("Задан список:",list_N)
    return list_N

def Random_list_float (N,min,max):
    list_float = [round(randint(min,max) + random(),4) for i in range(N)] 
    print ("Задан список:",list_float)
    return list_float