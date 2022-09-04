# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
flag = True
for i in False, True:
    for j in False, True:
        for k in False, True:
            x = i
            y = j
            z = k
            if (not (x or y or z)) == ( not x and not y and not z):
                print(f"x = ", {x}, "y = ", {y}, "z = ", {z}, " = True")
            else:
                print ("Выражение тождественно истинным не является")
                flag = False
if (flag):
    print ("Выражение является тождественно истинным")