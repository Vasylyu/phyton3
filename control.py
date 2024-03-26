from datetime import datetime


def input_note(file_name):
    count = count_note(file_name)
    information = list()
    information.append(str(count))
    information.append(input('Введите заголовок заметки: '))
    information.append(input('Введите тело заметки: '))
    return information


def count_note(file_name):
    with open(file_name, 'r') as fp:
        return sum([1 for lst in fp])


def create_note(file_name):
    date = datetime.now()
    str_date = date.strftime("%c")
    note = input_note(file_name)
    with open(file_name, 'a') as file:
        file.write('; '.join(note) + '; ' + str_date + '\n')


def show_notes(file_name):
    with open(file_name, 'r') as file:
        for lst in file:
            print(lst, end="")


def change_note(file_name):
    date = datetime.now()
    str_date = date.strftime("%c")
    with open(file_name, 'r') as file:
        lst = file.readlines()
    for line in lst:
        print(line, end=" ")
    n = int(input('Введите идентификатор заметки: '))
    if 0 <= n <= len(lst):
        note = input_note(file_name)
        note[0] = str(n)
        note = '; '.join(note) + '; ' + str_date + '\n'
        lst[n] = note
    with open(file_name, 'w') as file:
        file.writelines(lst)


def find_note(file_name):
    name = input('Введите заголовок или дату создания заметки: ')
    with open(file_name, 'r') as file:
        lst = file.readlines()
    for item in lst:
        if name in item:
            print(item)
        elif name not in lst:
            print('Заметка не найдена')


def delete_note(file_name):
    with open(file_name, 'r') as file:
        lst = file.readlines()
    for item in lst:
        print(item)
    n = int(input('Введите идентификатор заметки для изменения: '))
    if 0 <= n <= len(lst):
        del lst[n]
    with open(file_name, 'w') as file:
        file.writelines(lst)
        print("Заметка успешна удалена")


