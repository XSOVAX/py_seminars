# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

a = int(input('Enter a number to check: '))

fib_1 = 0
fib_2 = 1
answer = -1
n = 2
if a == fib_1:
    answer = 1
elif a == fib_2:
    answer = 2
else:
    while a > fib_2:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        n += 1
        if a == fib_2:
            answer = n

print(answer)

