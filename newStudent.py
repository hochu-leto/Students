import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('ошибка. Разные классы')
            return
        return self.average_grades() < other.average_grades()

    def average_grades(self):
        sum_grades = []
        for courses in (self.finished_courses + self.courses_in_progress):
            if courses in self.grades:
                sum_grades += self.grades[courses]

        average = sum(sum_grades) / len(sum_grades)
        return round(average, 2)

    def rate_lecture(self, lecturer, course, grade):
        if grade not in range(0, 11):
            print(f'Оценка может лектору быть от 0 до 10. Вы поставили {grade}')
            return
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
            return f'Новая оценка для {lecturer.name}'
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_grades()}'

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('ошибка. Разные классы')
            return
        return self.average_grades() < other.average_grades()

    def average_grades(self):
        sum_grades = []
        for courses in self.courses_attached:
            if courses in self.lecture_grades:
                sum_grades += self.lecture_grades[courses]
        average = sum(sum_grades) / len(sum_grades)
        return round(average, 2)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if grade not in range(0, 11):
            print(f'Оценка за ДЗ может быть от 0 до 10. Вы поставили {grade}')
            return
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return f'Новая оценка для {student.name}'
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Java']

worse_student = Student('Bob', 'Man', 'your_gender')
worse_student.courses_in_progress += ['Python']
worse_student.courses_in_progress += ['Java']
worse_student.finished_courses += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

good_mentor = Reviewer('Katie', 'Perry')
good_mentor.courses_attached += ['Python']
good_mentor.courses_attached += ['Git']

bad_mentor = Lecturer('Jonh', 'Smith')
bad_mentor.courses_attached += ['Git']
bad_mentor.courses_attached += ['Java']

no_bad_mentor = Lecturer('Sarah', 'Conor')
no_bad_mentor.courses_attached += ['Git']
no_bad_mentor.courses_attached += ['Python']

for i in range(random.randint(7, 15)):
    cool_mentor.rate_hw(best_student, 'Python', random.randint(2, 10))
    cool_mentor.rate_hw(worse_student, 'Python', random.randint(2, 8))
    cool_mentor.rate_hw(worse_student, 'Java', random.randint(6, 10))

    best_student.rate_lecture(bad_mentor, 'Git', random.randint(1, 7))
    best_student.rate_lecture(no_bad_mentor, 'Python', random.randint(3, 10))
    best_student.rate_lecture(no_bad_mentor, 'Git', random.randint(2, 9))

for i in range(random.randint(4, 20)):
    good_mentor.rate_hw(worse_student, 'Python', random.randint(2, 7))
    good_mentor.rate_hw(best_student, 'Python', random.randint(2, 7))
    good_mentor.rate_hw(best_student, 'Git', random.randint(5, 8))

    worse_student.rate_lecture(no_bad_mentor, 'Python', random.randint(1, 10))
    worse_student.rate_lecture(bad_mentor, 'Java', random.randint(1, 10))

print("Проверяющие:")
print(cool_mentor)
print(good_mentor)
print("\nЛекторы:")
print(bad_mentor)
print(no_bad_mentor)
print(f"{bad_mentor.name} круче {no_bad_mentor.name}?")
print(no_bad_mentor < bad_mentor)
print("\nСтуденты:")
print(worse_student)
print(best_student)
print(f"{worse_student.name} круче {best_student.name}?")
print(worse_student > best_student)


def course_average_hw_grades(students_list, course):
    sum_grades = []
    for student in students_list:
        if not isinstance(student, Student):
            print('ошибка. Разные классы')
            return
        if course in student.grades:
            sum_grades += student.grades[course]
    # print(sum_grades)
    return round(sum(sum_grades) / len(sum_grades), 2)


def course_average_lecturer_grades(lectures_list, course):
    sum_grades = []
    for lecturer in lectures_list:
        if not isinstance(lecturer, Lecturer):
            print('ошибка. Разные классы')
            return
        if course in lecturer.lecture_grades:
            sum_grades += lecturer.lecture_grades[course]
    # print(sum_grades)
    return round(sum(sum_grades) / len(sum_grades), 2)


course = "Python"
print(f"Средняя оценка за ДЗ по {course}:", course_average_hw_grades({worse_student, best_student}, course))
print(f"Средняя оценка лекций по {course}:", course_average_lecturer_grades({no_bad_mentor, bad_mentor}, course))
