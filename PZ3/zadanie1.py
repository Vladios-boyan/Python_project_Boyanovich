#Условие: Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 0 или B < -2».
try:
    a = int(input("Введите число А: "))
    b = int(input("Введите число Б: "))
except ValueError:
    print("Вы ввели не число!")
while True:
    if (a > 0) or (b < -2):
        print("True")
    else:
        print("False")
    break
