# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            result_task = not(X or Y or Z) == (not X and not Y and not Z) 
            print(f"для X = {X}, Y = {Y}, Z = {Z} результат:",result_task)