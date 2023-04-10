# Найдите сумму цифр трехзначного числа.

number = input('Enter the number: ')
print(sum(int(digit) for digit in number))