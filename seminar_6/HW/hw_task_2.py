# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

"""Функция заполнение массива длинною n"""
def filling_array(n):
    return [int(input(f"Введите {i + 1} значение : ")) for i in range(n)]

"""Запрос количества элементов в массиве и вызов функции для их заполнения"""
len_array = int(input("Введите количество элементов кустов: "))
array_data = filling_array(len_array)

"""Поиск нужных элементов"""
def find_element(array, left, right):
    global index_required_element
    for i in range(len(array)):
        if left <= array[i] <= right:
            index_required_element.append(i)

"""Получение границ диапозона запуск поиска"""
left_border = int(input("Введите левую границу диапозона поиска : "))
right_border = int(input("Введите правую границу диапозона поиска : "))
index_required_element = []
find_element(array_data, left_border, right_border)
print(f"Элементы лежащие в диапозоне [{left_border}; {right_border}] находятся под индексами {index_required_element}")