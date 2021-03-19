from bs4 import BeautifulSoup
import requests as req
import time


# Построение матрицы из списка животных.
def matrix_transformation(list_of_animals, alphabet):
    tmp_list = []
    matrix = []
    i = 0
    for item in list_of_animals:
        if not item[0] == ' ':
            if item[0] == alphabet[i]:
                tmp_list.append(item)
            else:
                matrix.append(tmp_list)
                tmp_list = list()
                tmp_list.append(item)
                i += 1
    matrix.append(tmp_list)
    return matrix


# Конструктор списка букв русского алфавита.
def alpha_builder():
    alphabet_in_deci = [code for code in range(ord('А'), (ord('а')))]
    # alphabet_in_deci.insert((alphabet_in_deci.index(ord('Ж'))), (ord('Ё')))
    # Удаление из списка неиспользуемых символов.
    black_list = [ord('Ъ'), ord('Ы'), ord('Ь')]
    alphabet_in_deci = [
        item for item in alphabet_in_deci if item not in black_list
    ]
    alphabet_list = list()
    for code in alphabet_in_deci:
        alphabet_list.append(chr(code))
    # Возвращение списка необходимых символов.
    return alphabet_list


# Стартовый URL и GET запрос.
base_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
page = req.get(base_url).text


# Цикл прокрутки страниц вики и создание общего списка животных.
animal_list = list()
# Флаг сигнализирующий о начале списка животных на латыни
# и прерывание цикла.
latin_starts = False
while not latin_starts:
    soup = BeautifulSoup(page, 'lxml')
    animals_list_page = soup.find_all('div', class_='mw-category-group')
    white_list = alpha_builder()
    for animal_page in animals_list_page:
        animals = animal_page.find_all('a')
        for animal in animals:
            """
            Решение semi-костыль, потому что сталкивался с латиницей внутри 
            кириллического списка, но к лучшей реализации пока не пришел
            """
            if animal.text[0] == 'A':
                latin_starts = True
                break
            # Замена Ё на Е.
            """
            Сортировка по кириллическому алфавиту начинается с "Ё".
            Для упрощения алгоритма и скорости его работы принял решение
            все "Ё"-значимые объекты переводить в "Е".
            """
            if animal.text[0] == 'Ё':
                animal_list.append(
                    animal.text.replace(animal.text[0], 'Е')
                )
            if animal.text[0] in white_list:
                animal_list.append(animal.text)
        if latin_starts:
            break
    links = soup.find('div', id='mw-pages').find_all('a')
    for link in links:
        try:
            if link.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + link.get('href')
                page = req.get(url).text
        except:
            time.sleep(3)
            continue


# alphabet = alpha_builder()
matrix = matrix_transformation(sorted(animal_list), alpha_builder())

i = 0
for el in alpha_builder():
    print(f'{el}: {len(matrix[i])}')
    i += 1
