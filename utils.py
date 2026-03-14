#decorator

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} işlemi yapıldı")
        return func(*args, **kwargs)
    return wrapper



def make_title_filter(keyword):
    def filtering(book):
        
        if keyword in book.title:
            return f"{book.title}"
        else:
            return None
    return filtering

def filter_books(books, condition_func):
    results=[]
    for book in books:
        if condition_func(book):
            results.append(book)
            
    return results


def create_formatter(format_type):
        
    def formatting(book):
        if format_type=="kısa":
           return f"{book.title}-{book.author}"
        elif format_type=="uzun":
            return f"{book.title}-{book.author}-{book.is_borrowed}"
    
    return formatting