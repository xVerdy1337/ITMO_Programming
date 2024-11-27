data = ["имя_1 150", "имя_2 167", "имя_3 124"]

while True:
    user_input = input('Введите имя и рост (в сантиметрах) (через пробел, для завершения - все построены): ')
    if user_input.lower() == 'все построены':
        break

    data.append(user_input)
    data.sort(key=lambda lst: int(lst.split()[1]), reverse=True)

    print(f"{user_input.split()[0]} на {data.index(user_input) + 1} месте")


for index, value in enumerate(data):
    print(f"{index + 1}) {value.split()[0]} ({value.split()[1]} см)")
