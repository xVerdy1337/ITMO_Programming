class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = self.check_age(age)
        self.pronoun = self.set_pronoun(gender)

    def check_age(self, age: int):
        if 0 <= age:
            return age
        else:
            raise ValueError("Возраст должен быть больше нуля")

    def set_pronoun(self, gender: str):
        gender = gender.strip().lower()
        if gender == 'м':
            return ['Его', 'Ему']
        elif gender == 'ж':
            return ['Её', 'Ей']
        else:
            raise ValueError("Неправильное значение пола. Введите 'м' или 'ж'.")

    def decline_year(self):
        if self.age % 10 == 1 and self.age % 100 != 11:
            return 'год'
        elif 2 <= self.age % 10 <= 4:
            return 'года'
        else:
            return 'лет'

    def show_info(self):
        year_word = self.decline_year()
        print(f'{self.pronoun[0]} зовут {self.name}. {self.pronoun[1]} {self.age} {year_word}.')


def get_input(prompt, expected_type=str):
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(f"Ошибка: ожидался ввод типа {expected_type.__name__}.")


name = get_input('Введите имя\n')
age = get_input('Введите возраст\n', int)
gender = get_input('Введите пол (м или ж)\n')


user_person = Person(name, age, gender)
user_person.show_info()