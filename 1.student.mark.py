students = []
courses = []
def student_in_class():
    num_students = int(input("Enter the number students in the class:"))
    for stu in range(num_students):
        id = (input("Enter the student ID: "))
        name = (input("Enter the student name: "))
        DoB = (input("Enter the student DoB:"))
        students.append({'ID':id, 'Name':name,'DoB':DoB,'marks':{}})

def number_of_courses():
    num_courses = int(input("Enter the number of course"))
    for cou in range(num_courses):
        courses_id = input('Enter course ID:')
        name = input('Enter course name:')
        courses.append({'id':courses_id,'name':name})

def marks_of_students():
    student_id = input("Enter student ID:")
    course_id = input("Enter course ID:")
    marks = float(input("Enter marks for the student:"))

    for student in students:
        if student['ID'] == student_id:
            student['marks'][course_id] = marks
            print(f"Marks was added for {student['name']} in course {course_id}")
            return
        print("Student not found")
def list_course():
    print("Course available:")
    for course in courses:
        print(f"ID:{course['id']}, Name:{['name']}")
def show_student_marks_for_course():
    student_id = input("Enter student ID:")
    course_id = input("Enter course ID:")

    for student in students:
        if student['id'] == student_id:
            marks = student['marks'].get(course_id,"No marks recorded.")
            print(f"Marks for {student['name']} in course {course_id}:{marks}")
            return
    print("Student not found.")
student_in_class()
number_of_courses()
print(students)
while True:
    print("\nOptions:")
    print("1. List Courses")
    print("2. List Students")
    print("3. Input Marks for Student")
    print("4. Show Student Marks for Course")
    print("5. Exit")

    option = input("Choose an option: ")
    if option == "1":
        list_courses()
    elif option == "2":
        list_students()
    elif option == "3":
        marks_of_students()
    elif option == "4":
        show_student_marks_for_course()
    elif option == "5":
        break
    else:
        print("Invalid option. Please try again.")