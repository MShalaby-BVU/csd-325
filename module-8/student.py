import json

# Loads the JSON file
with open('student.json' , 'r') as students:
    students = json.load(students)


# Prints current students
def student_directory(directory):
    for student in directory:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")


def main():
    print(">> Original Student List: ")
    student_directory(students)

    new_student = {
        "F_Name": "Mike",
        "L_Name": "Shalaby",
        "Student_ID": 12345,
        "Email": "mshalaby@my365.bellevue.edu"
    }

    students.append(new_student)

    print("\n>> Updated Student List: ")
    student_directory(students)

    with open('student.json', 'w') as file:
        json.dump(students, file)

    print('>> The student.json master file has been updated')


if __name__ == '__main__':
    main()
