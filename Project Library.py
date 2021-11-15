# project  library

class library:
    def __init__(self,book_list,library_name):
        self.book_list=book_list
        self.library_name=library_name
        self.lendict={}

    def display(self):
        print(f"we have following books in library {self.library_name}")
        for book in self.book_list:
            print(book)

    def lendbook(self,bookname,user):
        if bookname not in self.lendict.keys():
            self.lendict.update({bookname:user})
            self.book_list.remove(bookname)
            print("book library has been updated ,u can take your book")
        else:
            print(f"book has bee alreasy taken by {self.lendict[bookname]}")
    def addbook(self,bookname):
        self.book_list.append(bookname)
        print("book has been added")

    def returnbook(self,bookname):
        self.lendict.pop(bookname)
        self.book_list.append(bookname)
mainlab=library(["rich dad","poor dad","data science"],"metlab")
if __name__ == '__main__':
    while(True):
        print(f"welcome to the {mainlab.library_name}\n press 1 to display,2 for lend the book , 3 for add book ,4 for return the book")
        a=(input())
        if a not in ["1","2","3","4"]:
            print('ENTER BETWEEN 1 TO 4')
            continue
        else :
            a=int(a)
        if a==1:
            mainlab.display()
        elif a==2:
            user = input("enter your name please")
            bookname = input("enter book name")
            mainlab.lendbook(bookname,user)
        elif a==3:
            bookname = input("enter book name")
            mainlab.addbook(bookname)
        elif a==4:
            bookname=input("enter name of book")
            mainlab.returnbook(bookname)
        else :
            print("not a valid option")
        print("press Q to quit and C to continue")
        b=""
        while(b!= "q" and b!="C"):
            b=input()
            if b=="c":
                continue
            elif b=="Q":
                exit()

