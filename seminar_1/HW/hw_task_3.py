# Вы пользуетесь общественным транспортом? 
# Вероятно, вырасплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета

number = input('Enter ticket number: ')

sum_number_1 = sum(int(number[i]) for i in range(3))
sum_number_2 = sum(int(number[i]) for i in range(3, 6))

if sum_number_1 == sum_number_2:
    answer = 'Your ticket is lucky'
else:
    answer = 'Your ticket is not lucky'

print(answer)