import csv
import pickle as pc
import datetime


class Student:
    def __init__(self, name, second_name, birthdate):
        self.name = name
        self.second_name = second_name
        self.birthdate = birthdate


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def students_by_month(self, birthdate):
        answer = [student for student in self.students if student.birthdate == birthdate]
        return answer

    def sort_students(self):
        self.students = sorted(self.students, key=lambda student: student.name)

    def save_to_csv(self, filename):
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Name', 'Surname', 'Birthdate'])
            for student in self.students:
                writer.writerow([student.name, student.second_name, student.birthdate])

    @staticmethod
    def load_from_csv(filename):
        school_class = SchoolClass()
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                name, second_name, birthdate = row
                student = Student(name, second_name, birthdate)
                school_class.add_student(student)
        return school_class

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as pickle_file:
            pc.dump(self.students, pickle_file)

    @staticmethod
    def load_from_pickle(filename):
        school_class = SchoolClass()
        with open(filename, 'rb') as pickle_file:
            school_class.students = pc.load(pickle_file)
        return school_class


def run_task():
    school_class = SchoolClass()
    while True:
        choice_inp = int(input('Choose an action:\n'
                               '1. Add a student\n'
                               '2. Sort students\n'
                               '3. Sort students by birthdate\n'
                               '4. Save to csv\n'
                               '5. Load from csv\n'
                               '6. Save to pickle\n'
                               '7. Load from pickle\n'
                               '8. Exit\n'))
        match choice_inp:
            case 1:
                name = input('Enter name: ')
                surname = input('Enter a surname: ')
                date_str = input('Enter a birthdate in a format YYYY-MM-DD: ')
                try:
                    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    school_class.add_student(Student(name, surname, date))
                except ValueError:
                    print('Wrong date format')
            case 2:
                school_class.sort_students()
            case 3:
                inp_date = input('Enter a date in a format YYYY-MM-DD: ')
                date = datetime.datetime.strptime(inp_date, '%Y-%m-%d').date()
                for student in school_class.students:
                    if student.birthdate == date:
                        print(student.name, student.second_name, student.birthdate)
            case 4:
                school_class.save_to_csv('task1/school-class.txt')
            case 5:
                school_class = SchoolClass.load_from_csv('task1/school-class.txt')
                for student in school_class.students:
                    print(student.name, student.second_name, student.birthdate)
            case 6:
                school_class.save_to_pickle('task1/school-class.pkl')
            case 7:
                school_class = SchoolClass.load_from_pickle('task1/school-class.pkl')
                for student in school_class.students:
                    print(student.name, student.second_name, student.birthdate)
            case 8:
                break
