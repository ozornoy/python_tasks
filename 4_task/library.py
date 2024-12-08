from typing import Dict, Union, List


class Page:
    def __init__(self, text, number):
        self.text = text
        self.number = number


class Book:
    __id = 1

    def __init__(
        self,
        name: str,
        author: str,
        pages: List[Page],
        current_page: int = 1,
        active_status: bool = False,
    ):
        self.id = self.__get_current_id()
        self.name = name
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.active_status = active_status

    @classmethod
    def __get_current_id(cls):
        current_id = cls.__id
        cls.__id += 1
        return current_id

    def go_to_the_next_page(self):
        if not self.active_status:
            print("Невозмоно перелестнуть страницу у закрытой книги:-(")
            return
        if self.current_page < len(self.pages):
            self.current_page += 1
            return self.current_text
        else:
            print("К сожалению это последняя страница:-(")

    def go_to_the_previous_page(self):
        if not self.active_status:
            print("Невозмоно перелестнуть страницу у закрытой книги:-(")
            return
        if self.current_page < 1:
            self.current_page -= 1
            return self.current_text
        else:
            print("Это первая страница, листай вперед:-)")

    def go_to_page(self, page_number: int):
        if not self.active_status:
            print("Невозмоно перелестнуть страницу у закрытой книги:-(")
            return
        if page_number in range(1, len(self.pages) + 1):
            self.current_page = page_number
            return self.current_text
        else:
            print(f"К сожалению страницы под номером {page_number} не существует:-(")

    @property
    def current_text(self):
        return self.pages[self.current_page - 1].text


class Library:
    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.current_book: Union[Book, None] = None

    def add_books(self, *books: Book):
        for book in books:
            self.books[book.id] = book

    def remove_book(self, book_id: int):
        del self.books[book_id]
        if self.current_book.id == book_id:
            self.current_book = None

    def open_book(self, book_id: int):
        if book_id not in self.books:
            print(f"Книга с id:{book_id} отсутсвует в библиотеке. Добавь:-)")
            return
        opened_book = self.books[book_id]
        if self.current_book is None or self.current_book.id != book_id:
            if self.current_book is not None:
                self.current_book.active_status = False
            self.current_book = opened_book
            opened_book.active_status = True
        return opened_book

    def close_book(self):
        self.current_book.active_status = False
        self.current_book = None


class Reader:
    def __init__(self, name):
        self.name = name
        self.library = Library()

    def add_books(self, *books):
        self.library.add_books(*books)

    def remove_book(self, book_id: int):
        self.library.remove_book(book_id)

    def open_book(self, book_id: int):
        return self.library.open_book(book_id)

    def close_book(self):
        self.library.close_book()


books = [
    Book(
        name="The Great Gatsby",
        author="F. Scott Fitzgerald",
        pages=[Page(f"Text of page {i}", i) for i in range(1, 101)],
    ),
    Book(
        name="1984",
        author="George Orwell",
        pages=[Page(f"Text of page {i}", i) for i in range(1, 200)],
    ),
    Book(
        name="To Kill a Mockingbird",
        author="Harper Lee",
        pages=[Page(f"Text of page {i}", i) for i in range(1, 281)],
    ),
    Book(
        name="Pride and Prejudice",
        author="Jane Austen",
        pages=[Page(f"Text of page {i}", i) for i in range(1, 432)],
    ),
    Book(
        name="Moby Dick",
        author="Herman Melville",
        pages=[Page(f"Text of page {i}", i) for i in range(1, 585)],
    ),
]

reader = Reader("Читатель")
reader.add_books(books[0], books[1], books[2], books[3], books[4])
library = reader.library
print("-----------Все книги-------------")
print(
    library.books[1].name,
    library.books[2].name,
    library.books[3].name,
    library.books[4].name,
    library.books[5].name,
    sep="\n",
)
"""
The Great Gatsby
1984
To Kill a Mockingbird
Pride and Prejudice
Moby Dick
"""

print("-----------Текущая книга-------------")
print(library.current_book)
# None

print("-----------Открыли первую книгу-------------")
reader.open_book(1)
current_book = reader.library.current_book
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)
"""
title=The Great Gatsby
author=F. Scott Fitzgerald
text_of_current_page=Text of page 1
"""


print("-----------Посмотрели вторую книгу(закрытую)-------------")
closed_book = reader.library.books[2]
print(
    f"title={closed_book.name}",
    f"author={closed_book.author}",
    f"text_of_current_page={closed_book.current_text}",
    f"active_status={closed_book.active_status}",
    sep="\n",
)

print("-----------Перелестнули на следующую страницу у открытой книги-------------")
current_book.go_to_the_next_page()
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)


print("-----------Закрыли книгу-------------")
reader.close_book()
print(
    f"current_book={library.current_book}",
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)

print("-----------Попытаться перелестнуть страницу у закрытой книги-------------")
library.books[1].go_to_the_next_page()
library.books[1].go_to_the_previous_page()
# Невозмоно перелестнуть страницу у закрытой книги:-(
# Невозмоно перелестнуть страницу у закрытой книги:-(

print("-----------Попытаться открыть книгу по несуществующему id-------------")
reader.open_book(6)
# Книга с id:6 отсутсвует в библиотеке. Добавь:-)

print("-----------Открыть другую книгу на 100 странице-------------")
current_book = reader.open_book(5)
current_book.go_to_page(100)
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)
"""
title=Moby Dick
author=Herman Melville
text_of_current_page=Text of page 100
active_status=True
"""

print("-----------Перелестнуть на несуществующую страницу-------------")
current_book.go_to_page(586)
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)
"""
К сожалению страницы под номером 586 не существует:-(
title=Moby Dick
author=Herman Melville
text_of_current_page=Text of page 100
active_status=True
"""

print("-----------Открыть на еще не открытую книгу-------------")
current_book = reader.open_book(3)
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)
"""
title=To Kill a Mockingbird
author=Harper Lee
text_of_current_page=Text of page 1
active_status=True
"""

print("-----------Попытаться перелестнуть на предыдущую страницу-------------")
current_book.go_to_the_previous_page()
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)
"""
Это первая страница, листай вперед:-)
title=To Kill a Mockingbird
author=Harper Lee
text_of_current_page=Text of page 1
active_status=True
"""

print("-----------Открыть предыдущую книгу(должна быть на 100 странице)-------------")
current_book = reader.open_book(5)
print(
    f"title={current_book.name}",
    f"author={current_book.author}",
    f"text_of_current_page={current_book.current_text}",
    f"active_status={current_book.active_status}",
    sep="\n",
)

print("-----------Удалить текущую книгу из библиотеки-------------")
reader.remove_book(5)
print(f"current_book={library.current_book}")
print(f"books_len={len(library.books)}")
