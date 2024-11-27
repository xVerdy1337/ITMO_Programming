def change_reg(text: str) -> str:
    res = ''

    for i in text:
        res += i.lower() if i.isupper() else i.upper()

    return res

data = input('Введите какой-нибудь текст: ')

print(change_reg(data), len(data))
