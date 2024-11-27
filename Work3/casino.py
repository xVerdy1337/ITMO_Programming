from random import randint


def get_user_input():
    while True:
        user_input = input('Введите число от 1 до 100 (или "q" для выхода): ').lower()
        if user_input == 'q':
            return 'q'
        try:
            user_num = int(user_input)
            if 1 <= user_num <= 100:
                return user_num
            else:
                print('Число должно быть в диапазоне от 1 до 100.')
        except ValueError:
            print('Введите корректное число!')


def play_game():
    max_attempts = 10
    ask_num = randint(1, 100)
    attempts = 0

    print('Загадано число от 1 до 100 (включительно). Ваша задача — угадать его!')

    while attempts < max_attempts:
        print(f'Попытка {attempts + 1} из {max_attempts}')

        user_input = get_user_input()

        if user_input == 'q':
            print('Вы завершили игру. Спасибо за игру!')
            return False

        user_num = user_input

        if user_num == ask_num:
            print(f'Поздравляем! Вы угадали число {ask_num} за {attempts + 1} попыток.')
            break
        else:
            print('Неверно! ', end='')
            if user_num > ask_num:
                print('Загаданное число меньше.')
            else:
                print('Загаданное число больше.')
            attempts += 1

        if attempts == max_attempts:
            print(f'Вы исчерпали все попытки! Загаданное число было {ask_num}.')

    if input('Хотите сыграть ещё раз? (y/n): ').lower() != 'y':
        print('Игра завершена.')
        return False
    else:
        play_game()

play_game()
