# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Введите координаты точки Х:")
x = int(input())
print("Введите координаты точки Y:")
y = int(input())
if (x > 0 and y > 0):
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится в 1 четверти")
elif (x < 0 and y > 0):
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится во 2 четверти")
elif (x < 0 and y < 0):
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится в 3 четверти")
elif (x > 0 and y < 0):
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится в 4 четверти")
elif (x == 0 and y == 0):
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится на пересечении осей OX и OY ")
elif (x == 0):
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится на оси OY")
else:
    print(f"Точка с введёнными координатами X = ", x, "Y = ", y, "находится на оси OX")
