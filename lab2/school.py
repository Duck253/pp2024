from student import Student
from course import Course
class School:
    def __init__(self):
        self.students = []
        self.courses = []
    def add_student(self):
        num_students = int(input("Enter the number of students in the class"))
        for _ in range(num_students):
            student_id = input("enter the student ID:")
            name = input("enter the student name:")
            dob = input("enter the student dob:")
            self.students.append(Student(student_id,name,dob))
    def add_course(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id,name))
    def input_marks(self):
        student_id = int(input("Enter student ID: "))
        course_id = input("Enter course ID: ")
        marks = float(input("Enter mark for the student:"))

        for student in self.students:
            if student.id == student_id:
                student.add_marks(course_id,marks)
                return
            print("Student not found.")
    def list_courses(self):
        print("Courses available:")
        for course in self.courses:
            print(f"ID:{course.id}, Name:{course.name}")
    def list_students(self):
        print("Student exist")
        for student in self.students:
            print(f"ID:{student.id}, Name:{student.name}")
    def show_student_marks_for_course(self):
        student_id = input("Enter student ID:")
        course_id = input("Enter course ID:")

        for student in self.students:
            if student.id == student_id:
                marks = student.get_marks(course_id)
                print(f"Marks for {student.name} in course {course_id}: {marks}")
                return
        print("Student not found.")