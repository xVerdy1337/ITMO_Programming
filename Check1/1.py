name = ''

while True:
    word = input("Введите слово или словосочетание: ")

    if word == '':
        break

    for i in reversed(word):
        if i.isalpha():
            name += i
            break

print(name)
