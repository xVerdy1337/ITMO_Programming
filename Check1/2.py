from modules import save_data, load_data

data = load_data('databases/products.json')

while True:
    product = input('Введите продукт (нажмите Enter для выхода): ').strip()
    if not product:
        if data:
            print(f'Сохранены следующие данные: {data}')

        print('Программа завершена!')
        break

    try:
        cost = round(float(input(f'Введите стоимость для "{product}" (целое число или с плавающей точкой): ').strip()), 2)

        if cost <= 0:
            print('Стоимость не может быть 0 или меньше нуля!')
            continue

    except ValueError:
        print('Вы ввели неверный тип данных! (необходимо ввести число)')
        continue

    price = round(cost + cost * 0.15, 2)

    product = [product]
    cost = [cost]
    price = [price]
    new_data = list(zip(product, price, cost))

    data.append(new_data)
    save_data('databases/products.json', data)
