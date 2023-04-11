# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input())
power = 0

power_of_two = []
while 2 ** power <= n:
    power_of_two.append(2 ** power)
    power += 1

for number in power_of_two:
    print(number, end=' ')
print()