import csv

def get_age(age):
    """ Возвращает строку возраста в числовой формат. """
    return int(age) if age.isdigit() else float(age)

def replace_years(age):
    """ Заменяет число лет в текстовый формат с правильным склонением. """
    suffix_map = {1: 'год', 2: 'года', 3: 'года', 4: 'года'}
    suffix = suffix_map.get(age % 10, 'лет') if not 11 <= age % 100 <= 14 else 'лет'
    return f"{age} {suffix}"

def get_device(device_type):
    """ Получает устройства с англ. на рус. """
    return {
        'mobile': 'мобильного',
        'tablet': 'планшетного',
        'laptop': 'переносного компьютера',
        'desktop': 'стационарного компьютера'
    }.get(device_type, "пользовательского устройства")

def set_desc(row):
    """ Устанавливает описание клиента на основе его данных. """
    gender_map = {'female': 'женского', 'male': 'мужского'}
    return f"Пользователь {row['name']} {gender_map.get(row['sex'], 'неопределенного')} пола, " \
           f"{replace_years(row['age'])} совершил(а) покупку на {row['bill']} у.е. с " \
           f"{get_device(row['device_type'])} браузера {row['browser']}. " \
           f"Регион, из которого совершалась покупка: {row['region']}."

def main(input_file, output_file):
    """ Точка входа в программу """
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        descriptions = [set_desc({**row, 'age': get_age(row['age'])}) for row in reader]

    with open(output_file, mode='w', encoding='utf-8') as file:
        file.writelines(f"{desc}\n\n" for desc in descriptions)

# Иницилизация
main("./source.csv", "load.txt")