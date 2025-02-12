class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"{self.name} enrolled in {course}"
        return f"{self.name} is already enrolled in {course}"

    def get_courses(self):
        return self.courses