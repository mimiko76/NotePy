import Work_with_note


def main():
    while True:
        print("\nМеню:")
        print("1. Просмотреть все заметки")
        print("2. Добавить новую заметку")
        print("3. Удалить заметку")
        print("4. Найти заметку по дате")
        print("5. Выйти")

        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            Work_with_note.display_notes()
        elif choice == '2':
            Work_with_note.add_note()
        elif choice == '3':
            Work_with_note.delete_note()
        elif choice == '4':
            Work_with_note.date_search()
        elif choice == '5':
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()