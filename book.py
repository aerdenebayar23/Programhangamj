class Book:
    def __init__(self, title, author, isbn):
     self.t = title  # Title of the book
     self.a = author  # Author of the book
     self.i = isbn  # ISBN of the book
     self.s = False  # Status: True if checked out

     # Print the book info every time an object is created
     print("Created book: " + title + " by " + author + " (ISBN: " + isbn + ")")
    
    def __str__(self):
        if self.s == False:
            stat = "Available"
        else:
            stat = "Checked out"
        return f"{self.t} by {self.a} (ISBN: {self.i}) - {stat}"
        d