from database import load_data, save_data

logins = load_data('database/logins.json')

user_input = input('Введите ваш логин: ')

if user_input in logins:
    print('Доступ разрешён!')
else:
    print('Доступ запрещён! Необходимо зарегистрироваться. Для регистрации введите r: ')

    if input() != 'r':
        exit()

    user_input = input('Придумайте логин: ')

    logins += [user_input.strip()]
    save_data('database/logins.json', logins)

    print('Логин сохранён!')

