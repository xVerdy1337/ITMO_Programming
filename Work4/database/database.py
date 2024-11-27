import os
import json

def load_data(file_path: str) -> list:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                print(f'Загружены следующие данные: {data}')
                return data
            except json.JSONDecodeError:
                print('Ошибка при загрузке данных! Данные не были загружены!')
                return []

    else:
        print('Сохранёных данных не найдено!')
        return []

def save_data(file_path: str, data) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)