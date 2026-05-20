import json
import os

FILE_NAME = "students.txt"

def read_students():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        content = file.read()

        if not content:
            return []

        return json.loads(content)

def write_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)