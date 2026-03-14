from exceptions import BookAlreadyBorrowedError, BookAlreadyReturnedError
from utils import log_action





class Item:
    def __init__(self,id,title):
        self.id=id
        self.title=title
        
    


class Book(Item):
    def __init__(self,id,title,author,is_borrowed=False):
        self.author=author
        self.is_borrowed=False
        super().__init__(id,title)
    

    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "author": self.author,
        "is_borrowed": self.is_borrowed
    }

    @log_action
    def borrow(self):
        if self.is_borrowed:
            raise BookAlreadyBorrowedError(f"\n{self.id} id'li {self.title} başlıklı kitap zaten ödünç alınmış.")
        else:
            self.is_borrowed=True
            return f"{self.id} id'li {self.title} başlıklı kitap ödünç alındı"
        
    @log_action
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            return f"{self.id} id'li {self.title} başlıklı kitap iade edildi."
        else:
            raise BookAlreadyReturnedError(f"{self.id} id'li {self.title} başlıklı kitap ödünç alınmadığı için iade edilemez.")
    
    
    def __str__(self):
        if self.is_borrowed:
            situation="Ödünç Alındı"
        else:
            situation="Rafta"
        return f"{self.id}-{self.title}-{self.author}-{situation}"


    def __repr__(self):
        return f"Book(id='{self.id}', title='{self.title}', author='{self.author}')"