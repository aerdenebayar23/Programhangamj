from Book import book
from Member import member
class Library:
    def __init__(self):
        self.bks = []  
        self.mbs = []  

    def add_book(self, book):
        for b in self.bks:  
            if b.i == book.i:  
                print("Duplicate book!")  
                return  
        self.bks.append(book)  
        print("Added book: " + book.t)  

    def register_member(self, member):
        for m in self.mbs:  
            if m.mid == member.mid:  
                print("Duplicate member!")  
                return  
        self.mbs.append(member)  
        print("Registered member: " + member.nm)  

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

        if found_book.s == True:
            print("Already borrowed")  
            return  

        found_member.borrow_book(found_book)  

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


if __name__ == "__main__":
    lib = Library()

    b1 = Book("Book1", "Author1", "111")
    b2 = Book("Book2", "Author2", "222")
    lib.add_book(b1)
    lib.add_book(b2)

    m1 = Member(1, "John")
    m2 = Member(2, "Alice")
    lib.register_member(m1)
    lib.register_member(m2)

    lib.lend_book("111", 1)  
    lib.lend_book("222", 2)  

    lib.return_book("111", 1)  
