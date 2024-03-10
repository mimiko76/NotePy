import json
import uuid
from datetime import datetime
import random

import Work_with_file


def generate_id():
    random_num = random.randint(1, 100)
    return random_num


def add_note():
    notes = Work_with_file.load_notes()

    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note_id = generate_id()

    new_note = {
        'id': note_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }

    notes.append(new_note)
    Work_with_file.save_notes(notes)
    print("Заметка добавлена успешно.")


def delete_note():
    display_notes()
    note_id = int(input("Введите ID заметки для удаления: "))

    notes = Work_with_file.load_notes()
    notes = [note for note in notes if note['id'] != note_id]

    Work_with_file.save_notes(notes)
    print("Заметка удалена успешно.")


def date_search():
    try:
        note_date = datetime.strptime(input("Введите дату (в формате ГГГГ-ММ-ДД): "), "%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")
        return

    notes = Work_with_file.load_notes()

    search_date = note_date.date()

    found = False
    for note in notes:
        note_timestamp = datetime.fromisoformat(note.get("timestamp")).date()
        if note_timestamp == search_date:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print()
            found = True

    if not found:
        print("Запись с указанной датой не найдена.")


def display_notes():
    notes = Work_with_file.load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")
        print()
