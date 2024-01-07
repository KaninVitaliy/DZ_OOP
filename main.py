class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        #Cредняя оценка за домашние задания
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached and course in lector.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def sum_grades(self):
        self.grades_sum = []
        for key, value in self.grades.items():
            self.grades_sum.append(value[0])
        return (sum(self.grades_sum) / len(self.grades_sum))

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.sum_grades()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

    def __lt__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self < sum_grades_other:
            return True
        else:
            return False

    def __ne__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self != sum_grades_other:
            return True
        else:
            return False

    def __eq__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self == sum_grades_other:
            return True
        else:
            return False

    def __le__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self <= sum_grades_other:
            return True
        else:
            return False

    def __ge__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self >= sum_grades_other:
            return True
        else:
            return False

    def __gt__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self > sum_grades_other:
            return True
        else:
            return False

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
'''
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []
        self.courses_attached = []

    def sum_grades(self):
        self.grades_sum = []
        for key, value in self.grades.items():
            self.grades_sum.append(value[0])
        return (sum(self.grades_sum) / len(self.grades_sum))

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.sum_grades()}'''

    def __lt__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self < sum_grades_other:
            return True
        else:
            return False

    def __ne__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self != sum_grades_other:
            return True
        else:
            return False
    def __eq__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self == sum_grades_other:
            return True
        else:
            return False

    def __le__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self <= sum_grades_other:
            return True
        else:
            return False

    def __gt__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self > sum_grades_other:
            return True
        else:
            return False

    def __ge__(self, other):
        sum_grades_self = self.sum_grades()
        sum_grades_other = other.sum_grades()
        if sum_grades_self >= sum_grades_other:
            return True
        else:
            return False
def student_grades(spisok, course): # Функция для подсчетов оценок для всех Студентов
    sum_student_grades = []
    for i in spisok:
        if i.grades.get(course):
            for j in i.grades[course]:
                sum_student_grades.append(j)
    return sum(sum_student_grades) / len(sum_student_grades)

def lector_grades(spisok, course):
    sum_lector_grades = []
    for i in spisok:
        if i.grades.get(course):
            for j in i.grades[course]:
                sum_lector_grades.append(j)
    return sum(sum_lector_grades) / len(sum_lector_grades)





student_1 = Student("Vasiliy", "Petrov", "Мужчина")
student_1.finished_courses += ["Введение в программирование"]
student_1.courses_in_progress += ["Python"]
student_1.courses_attached += ["Python"]
student_1.courses_in_progress += ["Git"]
student_1.courses_attached += ["Git"]

student_2 = Student("Daria", "Ivanova", "Женщина")
student_2.finished_courses += ["Введение в программирование"]
student_2.courses_in_progress += ["Python"]
student_2.courses_attached += ["Python"]
student_2.courses_in_progress += ["Git"]
student_2.courses_attached += ["Git"]

lector_1 = Lecturer("Viktor", "Petrovich")
lector_1.courses_in_progress += ["Python"]
lector_1.courses_attached += ["Python"]

lector_2 = Lecturer("Vladimir", "Sergeevich")
lector_2.courses_in_progress += ["Git"]
lector_2.courses_attached += ["Git"]

reviewer_1 = Reviewer("Michail", "Nikolaevich")
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["Git"]

reviewer_2 = Reviewer("Alexandr", "Evgenevich")
reviewer_2.courses_attached += ["Python"]
reviewer_2.courses_attached += ["Git"]

student_1.rate_hw(lector_1, "Python", 10) # Cтудент 1 ставит оценку лектору №1
student_1.rate_hw(lector_2, "Git", 9) # Cтудент 1 ставит оценку лектору №2

student_2.rate_hw(lector_1, "Python", 9) # Cтудент 2 ставит оценку лектору №1
student_2.rate_hw(lector_2, "Git", 6) # Cтудент 2 ставит оценку лектору №2

reviewer_1.rate_hw(student_1, "Python", 9) # Ревьювер 1 ставит оценку студенту №1 За Питон
reviewer_2.rate_hw(student_1, "Python", 10) # Ревьювер 2 ставит оценку студенту №1 За Питон
reviewer_1.rate_hw(student_1, "Git", 7) # Ревьювер 1 ставит оценку студенту №1 За Гит
reviewer_2.rate_hw(student_1, "Git", 9) # Ревьювер 2 ставит оценку студенту №1 За Гит

reviewer_1.rate_hw(student_2, "Python", 8) # Ревьювер 1 ставит оценку студенту №2 За Питон
reviewer_2.rate_hw(student_2, "Python", 5) # Ревьювер 2 ставит оценку студенту №2 За Питон
reviewer_1.rate_hw(student_2, "Git", 8) # Ревьювер 1 ставит оценку студенту №2 За Гит
reviewer_2.rate_hw(student_2, "Git", 5) # Ревьювер 2 ставит оценку студенту №2 За Гит


print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lector_1)
print(lector_2)

print(student_1 == student_2)
print(student_1 < student_2)
print(student_1 > student_2)
print(student_1 != student_2)

print(lector_1 == lector_2)
print(lector_1 < lector_2)
print(lector_1 > lector_2)
print(lector_1 != lector_2)

# Задание №4

spisok_students = [student_1, student_2]
print(student_grades(spisok_students, "Python"))


spisok_lectors = [lector_1, lector_2]
print(lector_grades(spisok_lectors, "Python"))








