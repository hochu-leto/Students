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
                    
        average = sum(sum_grades)/len(sum_grades)
        return round(average, 2)

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
        sum_grades = []
        for courses in self.courses_attached:
            if courses in self.lecture_grades:
                sum_grades += self.lecture_grades[courses]     
        average = sum(sum_grades)/len(sum_grades)
        return round(average, 2)

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

worse_student = Student('Bob', 'Man', 'your_gender')
worse_student.courses_in_progress += ['Python']
worse_student.courses_in_progress += ['Java']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']
print(cool_mentor)

bad_mentor = Lecturer('Jonh', 'Smith')
bad_mentor.courses_attached += ['Git']

for i in range(15):
    cool_mentor.rate_hw(best_student, 'Python', random.randint(5, 10))

for i in range(15):
    cool_mentor.rate_hw(worse_student, 'Java', random.randint(2, 7))

for i in range(10):
    best_student.rate_lecture(bad_mentor, 'Git', random.randint(1, 10))

print(bad_mentor.lecture_grades)
print(bad_mentor)

print(best_student.grades)
print(best_student)

print(worse_student.grades)
print(worse_student)

print(worse_student < best_student)
