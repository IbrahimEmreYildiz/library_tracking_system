import json
from models import Book

def save_books(books):
    with open('books.json', mode='w', encoding='utf-8') as file:
        json.dump([book.to_dict() for book in books], file, indent=4)
    



def load_books():
    try:
        with open('books.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)
            books = []
            for item in data:
                book = Book(item['id'], item['title'], item['author'], item['is_borrowed'])
                books.append(book)
            return books
    except FileNotFoundError:
        return []


