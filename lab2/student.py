class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
    def add_marks(self,course_id,marks):
        self.marks[course_id] = marks
        print(f"Marks added for {self.name} in course {course_id}")
    def get_marks(self,course_id):
        return self.marks.get(course_id,"No marks recorded.")
