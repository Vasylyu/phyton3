import control
import menu


def main():
    file_name = 'Note.csv'
    while True:
        menu.print_menu()

        input_number = str(input('Выберете раздел в меню: '))
        if input_number == '1':
            control.create_note(file_name)
        elif input_number == '2':
            control.show_notes(file_name)
        elif input_number == '3':
            control.change_note(file_name)
        elif input_number == '4':
            control.delete_note(file_name)
        elif input_number == '5':
            control.find_note(file_name)
        elif input_number == '6':
            print("good bay")
            break
        print("Записная книжка завершила работу")


