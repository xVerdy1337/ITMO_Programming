import requests
from bs4 import BeautifulSoup

def get_names(count: int, gender: int) -> list[str]:
    """
    Получает список имён

    Args:
        count: количество имён
        gender: пол (10 - все, 0 - мужские, 1 - женские)

    Returns:
        list[str]: список имён
    """

    if not gender in [10, 0, 1]:
        print('Допустимые аргументы gender: \n1 - мужской\n0 - женский\n10 - все')
        exit()

    url = f"https://randomus.ru/name?type=5&sex={gender}&count={count}"
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        names = soup.find('textarea', id='result_textarea')

        return names.text.split('\n')
    else:
        return []
