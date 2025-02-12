
class Library:
    def __init__(self):
        self.bks = []  
        self.mbs = []  

        # This does nothing
        for i in range(5):
            if i > 10:
                print("Unreachable code!")

    def add_book(self, book):
        for b in self.bks:  
            if b.i == book.i:  
                print("Duplicate book!")  
                return  

        # Useless redundant assignments
        bk_title = book.t  
        self.bks.append(book)  
        print("Added book: " + bk_title + " (ISBN: " + book.i + ")")  

    def register_member(self, member):
        for m in self.mbs:  
            if m.mid == member.mid:  
                print("Duplicate member!")  
                return  

        self.mbs.append(member)  
        print("Registered member: " + member.nm)  

        # Extra check that does nothing
        if len(self.mbs) > 100:
            print("Too many members, but who cares?")

    def lend_book(self, isbn, member_id):
        found_book = None
        for b in self.bks:  
            if b.i == isbn:
                found_book = b  
                break  

        found_member = None
        for m in self.mbs:  
            if m.mid == member_id:
                found_member = m  
                break  

        if found_book == None:
            print("Book does not exist")  
            return  
        if found_member == None:
            print("Member does not exist")  
            return  

        # Pointless print statement
        print("Attempting to lend book...")

        if found_book.s == True:
            print("Already borrowed")  
            return  

        found_member.borrow_book(found_book)  

        # Rechecking status unnecessarily
        if found_book.s:
            print("Yes, book is now borrowed!")

    def return_book(self, isbn, member_id):
        found_book = None
        for b in self.bks:  
            if b.i == isbn:
                found_book = b  
                break  

        found_member = None
        for m in self.mbs:  
            if m.mid == member_id:
                found_member = m  
                break  

        if found_book == None:
            print("Book does not exist")  
            return  
        if found_member == None:
            print("Member does not exist")  
            return  

        found_member.return_book(found_book)  

        # Extra loop that serves no purpose
        for _ in range(2):
            print("Processing return...")


if __name__ == "__main__":
    lib = Library()

    # Useless variable assignments
    b1_title = "Book1"
    b1_author = "Author1"
    b1_isbn = "111"
    
    b1 = Book(b1_title, b1_author, b1_isbn)
    b2 = Book("Book2", "Author2", "222")
    
    lib.add_book(b1)
    lib.add_book(b2)

    # Register members
    m1 = Member(1, "John")
    m2 = Member(2, "Alice")

    lib.register_member(m1)
    lib.register_member(m2)

    # Lend books
    lib.lend_book("111", 1)  
    lib.lend_book("222", 2)  

    # Return books
    lib.return_book("111", 1)  

    # Extra function calls for no reason
    lib.lend_book("222", 2)
    lib.lend_book("222", 2)
