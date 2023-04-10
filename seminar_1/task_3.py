# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
# это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

i = int(input("I got into the train car under the number: "))
j = int(input("this is the train car numbered: "))

if i == j:
    answer = "I don't know"
else:
    answer = i + j - 1

print(answer)