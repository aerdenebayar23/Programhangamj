# course.py
class Course:
    def __init__(self, course_code, title):
        self.course_code = course_code
        self.title = title
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            return f"{student.name} added to {self.title}"
        return f"{student.name} is already in {self.title}"

    def get_students(self):
        return [s.name for s in self.students]