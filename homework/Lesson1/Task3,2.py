# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Coord_A = list(map(int, input("введите координаты первой точки через пробел: ").split()))
Coord_B = list(map(int, input("введите координаты второй точки через пробел: ").split()))
Coord_result = round(((Coord_B[0] - Coord_A[0])**2 + (Coord_B[1] - Coord_A[1])**2) ** 0.5, 2)
print("растояние между точками = ",Coord_result)