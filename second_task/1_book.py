class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price


book = Book(title="Новая книга", author="Новый автор", price=2.45)
print(book.title, book.author, book.price, sep=" | ")

book.author = "Измененный новый автор"
book.price = 2
print(book.title, book.author, book.price, sep=" | ")