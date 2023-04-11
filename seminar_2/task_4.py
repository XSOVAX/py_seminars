# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза

n = int(input())
mather_watermelon = 10*10
myself_watermelon = 0

for i in range(n):
    watermelon_weight = int(input())
    mather_watermelon = min(mather_watermelon, watermelon_weight)
    myself_watermelon = max(myself_watermelon, watermelon_weight)

print(mather_watermelon, myself_watermelon)