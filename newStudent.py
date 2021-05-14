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
        courses = ''
        for course in self.courses_in_progress:
            courses += ', ' + course
            return f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
                   f'Курсы в процессе изучения: {courses}\n' \
                   f'Завершенные курсы: {self.finished_courses}'

    def average_grades(self):
        count = 0
        sum_grades = 0
        for courses in self.finished_courses:
            if courses in self.grades and len(self.grades[courses]) > 0:
                for grades in self.grades[courses]:
                    sum_grades += grades
                    count += 1
            else:
                count = 1
        return sum_grades / count

    def rate_lecture(self, lecturer, course, grade):
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
    @property
    def average_grades(self):
        count = 0
        sum_grades = 0
        for courses in self.courses_attached:
            if courses in self.lecture_grades:
                for grades in self.lecture_grades[courses]:
                    sum_grades += grades
                    count += 1
        return sum_grades / count

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades}'

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
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

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor)

bad_mentor = Lecturer('Jonh', 'Smith')
bad_mentor.courses_attached += ['Git']

for i in range(15):
    cool_mentor.rate_hw(best_student, 'Python', random.randint(5, 10))

for i in range(10):
    best_student.rate_lecture(bad_mentor, 'Git', random.randint(1, 10))

print(bad_mentor.lecture_grades)
print(bad_mentor)

print(best_student.grades)
print(best_student)