import os
import time
from pprint import pprint

# Формируем словарь
'''
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''


def cook_book():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book_dict = {}
    # with open(file_path, 'r', encoding='utf-8') as f:
    with open(file_path, 'r', encoding='cp1251') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book_dict[dish_name] = ing_list
    return cook_book_dict



#  функцию, которая на вход принимает список блюд из
#  cook_book и количество персон для кого мы будем готовить

def list_dishes(dishes, person_count):
    ingr_dict = dict()

    for dish in dishes:  # перебор блюд
        if dish in result:
            for ings in result[dish]:  # перебор ингридиентов
                dish_list = dict()
                if ings['ingredient_name'] not in ingr_dict:
                    dish_list['measure'] = ings['measure']
                    dish_list['quantity'] = ings['quantity'] * person_count
                    ingr_dict[ings['ingredient_name']] = dish_list
                else:
                    ingr_dict[ings['ingredient_name']]['quantity'] = ingr_dict[ings['ingredient_name']]['quantity'] + ings['quantity'] * person_count

        else:
            print(f'\n"Блюдо отсутсвует в списке."\n')
    return ingr_dict




# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них 
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Пример Даны файлы: 1.txt
# 
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt
# 
# Строка номер 1 файла номер 2
# Итоговый файл:
# 
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1



def summary_file():
    directory = 'sorted'
    out_file = "rewrite_file.txt"

    # перебор файлов в каталоге
    list_file = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            with open(f, 'r', encoding='cp1251') as f1:
                file1 = f1.readlines()
            list_file[f] = len(file1)

    #  сортируем кортеж
    sorted_list_file = sorted(list_file.items(), key=lambda x: x[1])
    # записываем все в файл
    with open(out_file, 'w', encoding='cp1251') as f_total:
        idx = 1
        for name_file, len_file in dict(sorted_list_file).items():
            if idx <= len(list_file):
                with open(name_file, 'r', encoding='cp1251') as f1:
                    read_file = f1.readlines()
                    f_total.write(name_file + '\n')
                    f_total.write(str(len_file) + '\n')
                    f_total.writelines(read_file)
                    f_total.write('\n')
                    idx += 1
    return out_file

if __name__ == '__main__':
    filename = "recipes.txt"
    result = cook_book()
    print('Task 1')
    print('****************************************************')

    print(result)
    print('Task 2')
    print('****************************************************')
    pprint(list_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=3))


    print('Task 3')
    print('****************************************************')
    print('Создан файл: ',summary_file())