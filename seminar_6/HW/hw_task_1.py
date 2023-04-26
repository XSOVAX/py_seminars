# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

"""Функция возвращающая массив заполненый элементами арифметической прогрессии"""
def arithmetic_progression(a1, d, n):
    global data_arithmetic_progression
    data_arithmetic_progression.append(a1)
    if n - 1: arithmetic_progression(a1 + d, d, n - 1)


"""Получение значений и вывод результата"""
a1 = int(input('Введите значение первого элемента прогрессии : '))
d = int(input('Введите значение разности прогрессии : '))
n = int(input('Введите количество элементов прогрессии : '))
data_arithmetic_progression = []
arithmetic_progression(a1, d, n)
print(f'Прогрессия с указанными значениями -> {data_arithmetic_progression}')