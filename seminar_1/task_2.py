# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.

class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

print(-(-class_1 // 2 + -class_2 // 2 + -class_3 // 2))
