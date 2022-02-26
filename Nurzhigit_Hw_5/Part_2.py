from random import randint
cash = 1000
r = randint(1, 2)

answer = input('нажмите любую клавишу')

while answer != 'нет':
    с = 0
    с += 1
    bet = int(input(f'Введите ставку:(Доступно:{cash})'))
    slot = int(input('Выберите слот от 1го до 30ти'))
    if bet > cash:
        print(f'У тебя не хватает денег{cash}')
        continue
    elif slot == r:
        cash += bet*2
        print(f'У тебя денег:({cash})')
        answer = input('Вы хотите продолжить?')
        if answer == 'нет':
            print(f'У тебя:{cash}')
            break
    elif slot != r:
        cash -= bet
        print(f'У тебя денег:({cash})')
        answer = input('Вы хотите продолжить?')
        if answer == 'нет':
            print(f'У тебя{cash}')
            break
    else:
        print('Ты выиграл')

