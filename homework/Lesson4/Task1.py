# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = input("введите точность d:")
number_task = 3.1415926535
count = 0
while float(d) / 1 < 1:
    d = float(d) * 10
    count += 1
print("число равно:",round(number_task,count))
