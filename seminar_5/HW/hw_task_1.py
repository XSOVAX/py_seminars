# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

"""Функция возведения в степень"""
def power(a, b):
    if b == 0: return 1
    return a * power(a, b - 1)

"""Получение значений и вывод результата"""
number = input('Введите значение A = ')
degree = input('Введите значение B = ')
print(power(number, degree))