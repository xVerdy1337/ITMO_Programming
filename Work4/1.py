fullname = input("Введите ваше ФИО (полностью): ")
fullname = fullname.split()
print(f'{fullname[0]} {fullname[1][0]}. {fullname[2][0]}.')
