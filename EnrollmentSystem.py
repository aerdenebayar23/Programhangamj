from student import Student
from course import Course

class EnrollmentSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            return f"Student {name} added."
        return "Student ID already exists."

    def add_course(self, course_code, title):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_code, title)
            return f"Course {title} added."
        return "Course already exists."

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll(course_code)
            course.add_student(student)
            return f"{student.name} enrolled in {course.title}"
        return "Invalid student ID or course code."

# Example Usage
enrollment_system = EnrollmentSystem()
enrollment_system.add_student(1, "Alice")
enrollment_system.add_course("CS101", "Intro to CS")
enrollment_system.enroll_student(1, "CS101")
