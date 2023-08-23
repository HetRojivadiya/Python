class Student:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.books = []
        
    @property
    def het(self):
        return self.name, self.id , self.books
    
    @het.setter
    def het(self,list):
        self.name = list[0]
        self.id = list[1]
        self.books = list[2]
        
    def show(self):
        print(f"Student Name : {self.name}\nStudent ID : {self.id}")
        if len(self.books) != 0:
            print("Issues Books by student : ")
            for book in self.books:
                print("\t\t\t",book)  
        else:
            print("No Book Issues by the student") 
            
class Library(Student):
    AvailableBooks = ["abc","def","ghi","jkl","mno"]
    Booksissues = ["xyz"]
    
    def getBooks(self):
        print("AvailableBooks : ")
        for book in self.AvailableBooks:
            print("\t\t",book)
            
    def getIssue(self):
        print("AvailableBooks : ")
        for book in self.Booksissues:
            print("\t\t",book)
            
    def issueBook(self, bookName):
        self.Booksissues.append(bookName)
        self.books.append(bookName)
        self.AvailableBooks.remove(bookName)
                     
a = Library()
a.het = ["het",3223,["xyz"]]
b = Library()
b.het = ["ansh",3224,["pqr"]]
c = Library()
c.het = ["kalapi",3223,["stu"]]


while True:
    print("1. Show Students")
    print("2. Show Available Books")
    print("3. Issue a Book")
    print("4. Check Issues Book")
    print("5. exit")

    x=int(input())

    match x:
        case 1:
            a.show()
            b.show()
            c.show()
        case 2:
            a.getBooks()
        case 3:
            book = input("Enter Book name : ")
            a.issueBook(book)
        case 4:
            
            a.getIssue()
        case 5:
            break
    
    if x== 5:
        break      
            


