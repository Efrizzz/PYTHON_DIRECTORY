'''
Задача №49.
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

ДЗ: Дополнить справочник возможностью копирования данных из одного файла в другой.
'''
from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt 

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Не валидное имя')
            elif any(char.isdigit() for char in first_name):
                raise NameError('Имя не должно содержать цифры')
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err.txt)
            continue        

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input('Введите фамилию: ')
            if len(last_name) < 2:
                raise NameError('Не валидная фамилия')
            elif any(char.isdigit() for char in last_name):
                raise NameError('Фамилия не должна содержать цифры')
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err.txt)
            continue
    
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print('Не валидный номер!')
            continue
        except LenNumberError as err:
            print(err.txt)
            continue       

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        fieldnames = ['Имя', 'Фамилия', 'Телефон']
        writer = DictWriter(data, fieldnames=fieldnames)
        writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        reader = DictReader(data)
        return list(reader)
    
def write_file(file_name, lst):
    records = read_file(file_name)
    for record in records:
        if record['Телефон'] == str(lst[2]):
            print('Такой телефон уже существует')
            return
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    records.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        fieldnames = ['Имя', 'Фамилия', 'Телефон']
        writer = DictWriter(data, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def copy_data(input_file, output_file, name):
    with open(input_file, 'r', encoding='utf-8') as data:
        reader = DictReader(data)
        records = list(reader)

    with open(output_file, 'w', encoding='utf-8', newline='') as data:
        writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        writer.writeheader()

        for record in records:
            if record['Имя'] == name:
                writer.writerow(
                    {'Имя': record['Имя'], 'Фамилия': record['Фамилия'], 'Телефон': record['Телефон']})


def main():
    file_name = 'phone.csv'

    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует. Создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            input_file = input('Введите имя входного файла: ')
            output_file = input('Введите имя выходного файла: ')
            name = input('Введите имя для копирования: ')
            copy_data(input_file, output_file, name)

main()






        


    

