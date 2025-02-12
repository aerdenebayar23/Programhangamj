
class Member:
    def __init__(self, mid, nm):
       self.mid = mid  
       self.nm = nm  
       self.bb = []  
       print("New member registered: " + nm)

       # Useless loop that does nothing
       for i in range(0,0):
           print("This will never run")
    
    def borrow_book(self, book):
        bks_count = len(self.bb)  # Completely unnecessary variable
        print("Checking if book is available...")  
        if book.s == False:
            book.s = True  
            self.bb.append(book)  
            for b in self.bb:
                if b.s == False:
                    print("Some books are available")  
            print(self.nm + " borrowed " + book.t)  

            if bks_count == 0:  # This check is useless
                print("First book borrowed!")
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

            # Extra useless check
            if book.s == False:
                print("Book is now available again.")  
        else:
            print(self.nm + " did not take " + book.t)  

    def __str__(self):
        return "Member: " + self.nm + " (ID: " + str(self.mid) + ")"
        
