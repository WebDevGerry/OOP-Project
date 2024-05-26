from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @abstractmethod
    def object_data(self):
        pass


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.__student_id = student_id
        self.__courses = []

    @property
    def student_id(self):
        return self.__student_id

    @property
    def courses(self):
        return self.__courses

    def object_data(self):
        pass

    def enroll_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            print(f"{self.name} enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")


class Course:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.__students = []

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def students(self):
        return self.__students

    def object_data(self):
        pass

    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
            print(f"{student.name} added to {self.name}.")
        else:
            print(f"{student.name} is already in {self.name}.")



courses = [
    Course("Mathematics", "MATH101"),
    Course("English Literature", "ENG201"),
    Course("Science", "SCI301"),
    Course("History", "HIST401")
]

while True:
    
    print("\nAvailable Courses:")
    for index, course in enumerate(courses):
        print(f"{index + 1}. {course.name} ({course.code})")

    
    selected_course_index = int(input("Enter the index of the course to enroll in: ")) - 1
    selected_course = courses[selected_course_index]

    
    num_students = int(input("Enter the number of students to create: "))

    
    students = []

    for i in range(num_students):
        student_name = input(f"Enter the name of student {i+1}: ")
        student_age = int(input(f"Enter the age of student {i+1}: "))
        student_gender = input(f"Enter the gender of student {i+1}: ")
        student_id = input(f"Enter the student ID of student {i+1}: ")

        
        student = Student(student_name, student_age, student_gender, student_id)
        students.append(student)

    
    for student in students:
        selected_course.add_student(student)

    
    print(f"\nStudents in {selected_course.name}:")
    for student in selected_course.students:
        print(f"- {student.name}")

    
    another_course = input("Do you want to enroll in another course? (yes/no): ")
    if another_course.lower() != 'yes':
        break


print("\nAll Students Enrolled in Different Courses:")
for course in courses:
    print(f"\nStudents in {course.name}:")
    for student in course.students:
        print(f"- {student.name}")

