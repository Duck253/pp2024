from school import School

if __name__ == "__main__":
    school = School()
    school.add_student()
    school.add_course()
    while True:
        print("\nOptions:")
        print("1. List Courses")
        print("2. List Students")
        print("3. Input Marks for Student")
        print("4. Show Student Marks for Course")
        print("5. Exit")

        option = input("Choose an option: ")
        if option == "1":
            school.list_courses()
        elif option == "2":
            school.list_students()
        elif option == "3":
            school.input_marks()
        elif option == "4":
            school.show_student_marks_for_course()
        elif option == "5":
            break
        else:
            print("Invalid option. Please try again.")