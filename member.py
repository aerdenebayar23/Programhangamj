import pickle
from typing import List, Optional

class User:
    def __init__(self):
        self.user_details = {"username": "", "password": "", "access_level": 0}
        self.permissions = []
        self.is_active = False
        self.failed_login_attempts = 0

    def login(self, username: str, password: str):
        if username == self.user_details["username"] and password == self.user_details["password"]:
            self.is_active = True
            print("Login successful!")
        else:
            self.failed_login_attempts += 1
            print("Login failed. Attempts:", self.failed_login_attempts)

    def logout(self):

        self.user_details["username"] = username
        self.user_details["password"] = password
        self.user_details["access_level"] = access_level
        print("User details updated.")

class Student:
    def __init__(self, first_name: str, last_name: str):

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_id_number(self):
        return self.id_number

class Course:
    

    def print_course(self):

    def update_course_detail(self, key, value):
        if key in self.course_details:
            self.course_details[key] = value

    def get_detail(self, key):
        return self.course_details.get(key, None)

    def add_student(self, student):
        if self.course_details["current_students"] < self.course_details["max_students"]:
            self.student_list.append(student)
            self.course_details["current_students"] += 1
        else:
            print("Course is full.")

    def get_students(self):
        return self.student_list

class Admin(User):
    def __init__(self):
        super().__init__()
        self.set_user_details("admin", "admin001", 10)
        self.master_registry = []
        self.course_list = []

    def create_course(self):
        details = {}
        for key in ["name", "id", "max_students", "current_students", "instructor", "section", "location"]:
            details[key] = input(f"Enter course {key}: ")
            if key in ["max_students", "current_students"]:
                details[key] = int(details[key])
        
        new_course = Course(
            details["name"], details["id"], details["max_students"], details["current_students"],
            details["instructor"], details["section"], details["location"]
        )
        self.course_list.append(new_course)
        print(f"Added course: {details['name']}")

    def delete_course(self):
        name_to_delete = input("Enter course name to delete: ")
        index_to_delete = None
        for idx, course in enumerate(self.course_list):
            if course.get_detail("name") == name_to_delete:
                index_to_delete = idx
                break

        if index_to_delete is not None:
            del self.course_list[index_to_delete]
            print(f"Deleted course: {name_to_delete}")
        else:
            print("Course not found.")

    def edit_course(self):
        name = input("Enter course name to edit: ")
        for course in self.course_list:
            if course.get_detail("name") == name:
                key = input("Enter detail to update (e.g., instructor, location): ")
                value = input(f"Enter new value for {key}: ")
                course.update_course_detail(key, value)
                print("Course updated.")
                return
        print("Course not found.")

    def display_all_courses(self):
        if not self.course_list:
            print("No courses available.")
        for course in self.course_list:
            course.print_course()

        new_student = Student(first_name, last_name)
        self.master_registry.append(new_student)

        course_name = input("Enter course name to register student: ")
        for course in self.course_list:
            if course.get_detail("name") == course_name:
                course.add_student(new_student)
                print(f"Registered {first_name} {last_name} to {course_name}.")
                return

        print("Course not found, student not registered.")

    def view_full_courses(self):
        full_courses = [c for c in self.course_list if c.get_detail("current_students") == c.get_detail("max_students")]
        if not full_courses:
            print("No full courses.")
        for course in full_courses:
            course.print_course()

    def write_to_file_full_courses(self):
        with open("full_courses_dump.txt", "w") as file:
            for course in self.course_list:
                if course.get_detail("current_students") == course.get_detail("max_students"):
                    file.write(course.get_detail("name") + "\n")
        print("Full courses written to file.")
