def xor_encrypt(text: str, key: str) -> str:
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    return encrypted


def xor_decrypt(encrypted_text: str, key: str) -> str:
    return xor_encrypt(encrypted_text, key)


def main():
    print("Добро пожаловать в программу шифрования!")
    while True:
        print("\nМеню:")
        print("1. Зашифровать строку")
        print("2. Расшифровать строку")
        print("q. Выйти")

        choice = input("Выберите действие (1/2/q): ").strip()

        if choice == "1":
            text = input("Введите строку для шифрования: ")
            if not text:
                print("Строка не может быть пустой!")
                continue
            key = input("Введите ключ шифрования: ")
            if not key:
                print("Ключ не может быть пустым!")
                continue
            encrypted_text = xor_encrypt(text, key)
            print(f"Зашифрованная строка: {encrypted_text}")
        elif choice == "2":
            encrypted_text = input("Введите зашифрованную строку: ")
            if not encrypted_text:
                print("Строка не может быть пустой!")
                continue
            key = input("Введите ключ шифрования: ")
            if not key:
                print("Ключ не может быть пустым!")
                continue
            decrypted_text = xor_decrypt(encrypted_text, key)
            print(f"Расшифрованная строка: {decrypted_text}")
        elif choice == "q":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
