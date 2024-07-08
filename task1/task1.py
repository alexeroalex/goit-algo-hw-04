from pathlib import Path

"""
    Розраховує загальну та середню суму заробітної плати всіх розробників за даними у заданому файлі

    Параметри:
    path (Path): Об'єкт класу Path, що задає шлях до файлу.

    Повертає:
    tuple or None: Кортеж з двома значеннями: загальна та середня сума заробітної плати.
                   Якщо файл не знайдено або знайдено ValueError, то повертаємо None.
    """


def total_salary(path: Path):
    try:
        # Відкриття файлу для читання
        with open(path, 'r') as fh:
            # Зберігаємо всі рядки з файлу в список
            line_list = [el.strip() for el in fh.readlines()]

            tot_salary = 0
            # Беремо тільки заробітні плати робітників з кожного рядка
            for line in line_list:
                _, employee_salary = line.split(',')
                tot_salary += int(employee_salary)

            avg_salary = tot_salary/len(line_list)
            if int(avg_salary) == avg_salary:
                avg_salary = int(avg_salary)

            return tot_salary, avg_salary

    except FileNotFoundError:
        print(f'File not found at {path}!')
        return None

    except ValueError:
        print('Value error occurred')
        return None


print(total_salary(Path('task1.txt')))
