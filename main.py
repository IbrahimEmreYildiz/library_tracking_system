from storage import load_books, save_books
from models import Book, Item
from utils import make_title_filter, filter_books, log_action
from exceptions import BookNotFoundError, BookAlreadyBorrowedError, BookAlreadyReturnedError



books=load_books()


@log_action
def kitap_ekle():
    title=input("Kitap Adı: ")
    author=input("Kitap Yazarı: ")
    id=len(books)+1
    kitap1=Book(id=id, title=title, author=author)
    books.append(kitap1)
    save_books(books)



@log_action
def kitapları_listele():

    print("*********************KAYITLI KİTAPLAR*************************")
    for book in books:
        print(book)



@log_action
def kitap_ara():
    filtre=make_title_filter(input("Lütfen aramak istediğiniz kelimeyi giriniz: "))
    kitap_listesi= filter_books(books,filtre)
    print("**************LİSTEDEKİ KİTAPLAR***************")
    for book in kitap_listesi:
        print(book)



@log_action
def kitap_odunc_al():
    kontrol=int(input("Lütfen ödünç almak istediğiniz kitabın id'sini giriniz: "))
    bulunan_kitap=None
    for book in books:
        if book.id==kontrol:
            print("Seçtiğiniz kitap elimizde bulunmakta ödünç alabilirsiniz.")
            bulunan_kitap=book
            break
                
    if bulunan_kitap==None:
        raise BookNotFoundError(f"Aradığınız kitap ({bulunan_kitap}) mevcut değil.")
                    
                    
    try:
        bulunan_kitap.borrow()
        save_books(books)
    except BookAlreadyBorrowedError:
        print(f"Aradığınız kitap ({bulunan_kitap}) zaten ödünç alınmış.")





@log_action
def kitap_iade_et():
    iade=int(input("Lütfen iade etmek istediğiniz kitabın id'sini giriniz: "))
    iade_kitap=None
    for book in books:
        if book.id==iade:
            print(f"{book.id} id'li kitabı iade edebilirsiniz.")
            iade_kitap=book
            break
    if iade_kitap==None:
        raise BookNotFoundError(f"{iade} id'li kitap bize ait değil.")
            
    try:
        iade_kitap.return_book()
        save_books(books)
    except BookAlreadyReturnedError:
        print(f"Önce ödünç almanız lazım.")





while True:
    try:
        secim=int(input("\n\n1-Kitap ekle\n2-Kitapları Listele\n3-Kitap Ara\n4-Kitapları Ödünç al\n5-Kitap İade Et\n6-Çıkış\nLütfen bir seçim yapınız(1-6):"))

        if secim==6:
            break
        elif secim==1:
            kitap_ekle()

        elif secim==2:
           kitapları_listele()
 
        elif secim==3:
            kitap_ara()

        elif secim==4:
            kitap_odunc_al()
            
        elif secim==5:
            kitap_iade_et()
       
        else:
              print("Lütfen sadece belirtilen aralıkta bir rakam giriniz(1-6).")  
    except ValueError:
        print("Lütfen sadece belirtilen aralıkta bir rakam giriniz(1-6).")
    
        