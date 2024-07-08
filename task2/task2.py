from pathlib import Path

"""
    Створює список словників з даними про котів.

    Параметри:
    path (Path): Об'єкт класу Path, що задає шлях до файлу.

    Повертає:
    list or None: Список зі словниками, які зберігають ідентифікатор, ім'я та вік кота.
                  Якщо файл не знайдено або знайдено ValueError, то повертаємо None.
    """


def get_cats_info(path: Path):
    result_list = []
    try:
        # Відкриття файлу для читання
        with open(path, 'r') as fh:
            line_list = [el.strip() for el in fh.readlines()]
            # Беремо інформацію про котів з кожного рядка та зберігаємо її у словник, додаючи до списку
            for line in line_list:
                cat_id, cat_name, cat_age = line.split(',')
                cat_dict = {'id': cat_id, 'name': cat_name, 'age': cat_age}
                result_list.append(cat_dict)
        return result_list

    except FileNotFoundError:
        print('File not found')
        return None

    except ValueError:
        print('Value error occurred')
        return None


print(get_cats_info(Path('task2.txt')))
