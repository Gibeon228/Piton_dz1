# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
print ("Введите номер четверти")
i = 1
number_quarter = int(input())
while (not (0 < number_quarter < 5)):
    print ("Попробуйте ещё раз")
    i+=1
    number_quarter = int(input())
else:
    if (i != 1):
        print (f"У вас получилось ввести номер четверти с",i , "раз")
if (number_quarter == 1):
    print ("В данной четверти координаты x > 0, y > 0")
elif (number_quarter == 2):
    print ("В данной четверти координаты x < 0, y > 0")
elif (number_quarter == 3):
    print ("В данной четверти координаты x < 0, y < 0")
else:
    print ("В данной четверти координаты x > 0, y < 0")
