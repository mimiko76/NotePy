import json
import os.path


def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r+') as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)
