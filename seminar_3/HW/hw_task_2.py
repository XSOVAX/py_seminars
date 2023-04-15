# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

""" Количество элементов в массиве"""
n = int(input('Введите количество элементов -> '))

""" Создание массива для ввода данных"""
array_data = []

""" Получение элементов массива"""
for i in range(n):
    array_data.append(int(input(f"Введите {i + 1} число из {n} чисел: ")))

"""Получение искомого элемента"""
x = int(input("Введите число для поиска: "))

"""Поиск ближайщего элемента"""
suitable_element = array_data[0]
if x in array_data:
    suitable_element = x
else:
    delta = abs(array_data[0] - x)
    suitable_element = array_data[0]
    for i in range(1, n):
        new_delta = abs(array_data[i] - x)
        if new_delta < delta:
            delta = new_delta
            suitable_element = array_data[i]
print(f"Наиболее близкий по значению к {x} элемент -> {suitable_element}")