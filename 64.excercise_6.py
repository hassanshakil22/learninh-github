class Library:
  def __init__(self   ):

    self.books= ["Eco","Sci","Lit","Gramm","Urdu"]
    self.no_of_books= len(self.books)
    print(f"the  books in library are {self.no_of_books} : ") 
    i = 1
    for book in self.books:
     print (f"{i} : {book}")   
     i = i + 1


  def add_book(self,bookname):
    self.books.append(bookname)
    i = 1
    for book in self.books:
     print (f"{i} : {book}")   
     i = i + 1 

      
a=Library()

addbook= input("do you want to add a book : Y/N ")
addbook=addbook.upper()
if addbook!= "Y":
  exit()
else:
    newbook=input("Enter the name of the book you want to add :")
    a.add_book(newbook)

# a.add_book("okay")
   
