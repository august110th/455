class Student:
    names = []
    grades = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.gpa = 0
        Student.names.append(name)
        Student.grades.append(self.grades)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer
        ) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент")
        return self.gpa < other.gpa

    def __str__(self):
        print("print(some_student)")
        print(f"Имя: {self.name}")
        print(f"Фамилиия: {self.surname}")
        for key, value in self.grades.items():
            x = round(sum(value) / len(value), 1)
            self.gpa = x
        print(f"Средняя оценка за домашние задания: {x}")
        print(f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}")
        print(f"Завершенные курсы: {', '.join(self.finished_courses)}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    names = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        Reviewer.names.append(name)
    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print("print(some_reviewer)")
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")


class Lecturer(Mentor):
    names = []
    grades = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.gpa = 0
        Lecturer.names.append(name)
        Lecturer.grades.append(self.grades)

    def __str__(self):
        print("print(some_lecturer)")
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        for key, value in self.grades.items():
            y = round(sum(value) / len(value), 1)
            self.gpa = y
        print(f"Средняя оценка за лекции: {y}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не студент")
        return self.gpa < other.gpa

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

worst_student = Student("Petr", "Ivanov", "male")
worst_student.courses_in_progress += ["Git"]
worst_student.finished_courses += ['Введение в программирование']

middle_student = Student("Jack", "Daniels", "male")
middle_student.courses_in_progress += ["Python", "Git"]
middle_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

usual_reviewer = Reviewer("Phil", "Collins")
usual_reviewer.courses_attached += ["Git"]

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(middle_student, "Python", 8)
cool_reviewer.rate_hw(middle_student, "Python", 7)
cool_reviewer.rate_hw(middle_student, "Python", 9)
usual_reviewer.rate_hw(worst_student, "Git", 4)
usual_reviewer.rate_hw(worst_student, "Git", 5)
usual_reviewer.rate_hw(worst_student, "Git", 4)

cool_lecturer = Lecturer("Ivan", "Petrov")
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer("Mick", "Jagger")
bad_lecturer.courses_attached += ["Git"]

best_student.rate_lector(cool_lecturer, "Python", 10)
best_student.rate_lector(cool_lecturer, "Python", 9)
best_student.rate_lector(cool_lecturer, "Python", 10)
worst_student.rate_lector(bad_lecturer, "Git", 2)
worst_student.rate_lector(bad_lecturer, "Git", 5)
worst_student.rate_lector(bad_lecturer, "Git", 6)

cool_lecturer.__str__()
bad_lecturer.__str__()
best_student.__str__()
middle_student.__str__()
worst_student.__str__()

python_list_st = []
git_list_st = []
for dictionary in Student.grades:
    for key in dictionary:
        if 'Python' in dictionary:
            python_list_st += dictionary[key]
        else:
            git_list_st += dictionary[key]
python_gpa_st = round(sum(python_list_st)/ len(python_list_st), 1)
git_gpa_st = round(sum(git_list_st)/ len(git_list_st), 1)
print(python_gpa_st)
print(git_gpa_st)

python_list_lec = []
git_list_lec = []
for dictionary in Lecturer.grades:
    for key in dictionary:
        if 'Python' in dictionary:
            python_list_lec += dictionary[key]
        else:
            git_list_lec += dictionary[key]
python_gpa_lec = round(sum(python_list_lec)/ len(python_list_lec), 1)
git_gpa_lec = round(sum(git_list_lec)/ len(git_list_lec), 1)
print(python_gpa_lec)
print(git_gpa_lec)




