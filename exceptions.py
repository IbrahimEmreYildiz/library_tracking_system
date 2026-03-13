class LibError(Exception):
    pass



class BookNotFoundError(LibError):
    pass


class BookAlreadyReturnedError(LibError):
    pass


class BookAlreadyBorrowedError(LibError):
    pass
