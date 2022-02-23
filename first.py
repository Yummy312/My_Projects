# Светофор
red = 'красный'
yellow = 'желтый'
green = 'зеленый'
signal = input('Введите цвет')
if signal == red:
    print('Стой')
elif signal == yellow:
    print('Ожидай')
elif signal == green:
    print('Поехали')
else:
    print('Смотрим по ситуации')
