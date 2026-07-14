#more prectice on classes and OOP in general cause day 6 was kinda hard
#thats why ill do two projects now one to strenghten my OOP basics and one to learn new parts of OOP

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False
    
    def shorter_than(self, other_book):
        if self.pages < other_book.pages:
            return "This book is shorter than Harry Potter!"
        else:
            return "This book is longer or as long as Harry Potter!"
                    
        
book_1 = Book("Harry Potter", "J.K. Rowling", 320)
book_2 = Book("Bible", "Martin Luther", 2000)
book_3 = Book("Maths for dummies", "Mr. Quast", 267)

#print(book_1.is_long())
print(book_3.shorter_than(book_1))