# course.py
class Book:
    def __init__(self, title, author, isbn):
        self.t = title  
        self.a = author  
        self.i = isbn  
        self.s = False  

    def __str__(self):
        if self.s == False:
            stat = "Available"
        else:
            stat = "Checked out"
        return f"{self.t} by {self.a} (ISBN: {self.i}) - {stat}"
