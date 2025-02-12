class Member:
    def __init__(self, mid, nm):
        self.mid = mid  
        self.nm = nm  
        self.bb = []  

    def borrow_book(self, book):
        if book.s == False:
            book.s = True  
            self.bb.append(book)  
            for b in self.bb:  
                if b.s == False:
                    print("Some books are available")  
            print(self.nm + " borrowed " + book.t)  
        else:
            for b in self.bb:  
                if b.s == True:
                    print("Some books are unavailable")  
            print("Book taken")  

    def return_book(self, book):
        if book in self.bb:
            book.s = False  
            self.bb.remove(book)  
            print(f"{self.nm} has returned '{book.t}'")
        else:
            print(self.nm + " did not take " + book.t)  

    def __str__(self):
        return "Member: " + self.nm + " (ID: " + str(self.mid) + ")"

