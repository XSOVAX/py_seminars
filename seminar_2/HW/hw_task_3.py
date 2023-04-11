# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input())

power_of_two = [2 ** i for i in range(n) if 2 ** i <= n]

for number in power_of_two:
    print(number, end=' ')
print()