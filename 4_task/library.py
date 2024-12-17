from typing import Dict, Union, List


class Page:
    def __init__(self, text: str, number: int):
        self.text = text
        self.number = number


class Book:
    __id = 1

    def __init__(self, name: str, author: str, pages: List[Page]):
        self.id = self.__get_current_id()
        self.name = name
        self.author = author
        self.pages = pages

    @classmethod
    def __get_current_id(cls):
        current_id = cls.__id
        cls.__id += 1
        return current_id


class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
    pass


class BookNotOpenError(LibraryError):
    pass


class BookCollection:
    def __init__(self):
        self.books: Dict[int, Book] = {}

    def add_books(self, *books: Book) -> None:
        for book in books:
            self.books[book.id] = book

    def remove_book(self, book_id: int) -> None:
        if book_id not in self.books:
            raise BookNotFoundError(f"Книга с id:{book_id} не найдена")
        del self.books[book_id]

    def get_book(self, book_id: int) -> Book:
        if book_id not in self.books:
            raise BookNotFoundError(f"Книга с id:{book_id} отсутствует в библиотеке")
        return self.books[book_id]


class BookReader:
    def __init__(self):
        self._current_book: Union[Book, None] = None
        self._book_positions: Dict[int, int] = {}

    def open_book(self, book: Book) -> None:
        self._current_book = book
        if book.id not in self._book_positions:
            self._book_positions[book.id] = 1

    def close_book(self) -> None:
        self._current_book = None

    def next_page(self) -> None:
        if not self._current_book:
            raise BookNotOpenError("Невозможно перелистнуть страницу у закрытой книги")

        current_page = self._book_positions[self._current_book.id]
        if current_page < len(self._current_book.pages):
            self._book_positions[self._current_book.id] = current_page + 1
        else:
            raise ValueError("Это последняя страница, дальше листать некуда")

    def previous_page(self) -> None:
        if not self._current_book:
            raise BookNotOpenError("Невозможно перелистнуть страницу у закрытой книги")

        current_page = self._book_positions[self._current_book.id]
        if current_page > 1:
            self._book_positions[self._current_book.id] = current_page - 1
        else:
            raise ValueError("Это первая страница, назад листать некуда")

    def go_to_page(self, page_number: int) -> None:
        if not self._current_book:
            raise BookNotOpenError("Невозможно перелистнуть страницу у закрытой книги")

        if page_number not in range(1, len(self._current_book.pages) + 1):
            raise ValueError(f"Страница {page_number} не существует")

        self._book_positions[self._current_book.id] = page_number

    @property
    def current_book(self) -> Union[Book, None]:
        return self._current_book

    @property
    def current_text(self) -> str:
        if not self._current_book:
            raise BookNotOpenError("Нет открытой книги")
        current_page = self._book_positions[self._current_book.id]
        return self._current_book.pages[current_page - 1].text


class Library:
    def __init__(self):
        self.collection = BookCollection()
        self.book_reader = BookReader()

    def add_books(self, *books: Book) -> None:
        self.collection.add_books(*books)

    def remove_book(self, book_id: int) -> None:
        if self.book_reader.current_book and self.book_reader.current_book.id == book_id:
            self.book_reader.close_book()
        self.collection.remove_book(book_id)

    def open_book(self, book_id: int) -> Book:
        book = self.collection.get_book(book_id)
        self.book_reader.open_book(book)
        return book


class User:
    def __init__(self, name: str):
        self.name = name
        self.library = Library()

    def add_books(self, *books: Book) -> None:
        self.library.add_books(*books)

    def remove_book(self, book_id: int) -> None:
        try:
            self.library.remove_book(book_id)
        except BookNotFoundError as e:
            print(e)

    def open_book(self, book_id: int) -> None:
        try:
            self.library.open_book(book_id)
        except BookNotFoundError as e:
            print(e)

    def close_current_book(self) -> None:
        self.library.book_reader.close_book()

    def next_page(self) -> None:
        try:
            self.library.book_reader.next_page()
        except (BookNotOpenError, ValueError) as e:
            print(e)

    def previous_page(self) -> None:
        try:
            self.library.book_reader.previous_page()
        except (BookNotOpenError, ValueError) as e:
            print(e)

    def go_to_page(self, page_number: int) -> None:
        try:
            self.library.book_reader.go_to_page(page_number)
        except (BookNotOpenError, ValueError) as e:
            print(e)

    @property
    def current_book(self) -> Union[Book, None]:
        return self.library.book_reader.current_book

    @property
    def current_text(self) -> str:
        try:
            return self.library.book_reader.current_text
        except BookNotOpenError:
            raise RuntimeError("Все книги закрыты. Откройте какую-нибудь")


def main():
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

    user = User("Читатель")
    user.add_books(*books)
    library = user.library

    print("-----------Все книги-------------")
    print(
        library.collection.books[1].name,
        library.collection.books[2].name,
        library.collection.books[3].name,
        library.collection.books[4].name,
        library.collection.books[5].name,
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
    print(user.current_book)
    # None

    print("-----------Открыли первую книгу-------------")
    user.open_book(1)
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    title=The Great Gatsby
    author=F. Scott Fitzgerald
    text=Text of page 1
    """

    print("-----------Посмотрели вторую книгу(закрытую)-------------")
    closed_book = user.library.collection.books[2]
    print(
        f"title={closed_book.name}",
        f"author={closed_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    title=1984
    author=George Orwell
    text=Text of page 1
    """

    print("-----------Перелистнуи на следующую страницу у открытой книги-------------")
    user.next_page()
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    title=The Great Gatsby
    author=F. Scott Fitzgerald
    text=Text of page 2
    """

    print("-----------Закрыли книгу-------------")
    user.close_current_book()
    print(f"current_book={user.current_book}")
    # current_book=None

    print("-----------Попытаться перелистнуть страницу у закрытой книги-------------")
    user.close_current_book()
    user.next_page()
    user.previous_page()
    # Невозможно перелистнуть страницу у закрытой книги
    # Невозможно перелистнуть страницу у закрытой книги

    print("-----------Попытаться открыть книгу по несуществующему id-------------")
    user.open_book(6)
    # Книга с id:6 отсутствует в библиотеке

    print("-----------Открыть другую книгу на 100 странице-------------")
    user.open_book(5)
    user.go_to_page(100)
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    title=Moby Dick
    author=Herman Melville
    text=Text of page 100
    """

    print("-----------Перелистнуть на несуществующую страницу-------------")
    user.go_to_page(586)
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    Страница 586 не существует
    title=Moby Dick
    author=Herman Melville
    text=Text of page 100
    """

    print("-----------Открыть еще не открытую книгу-------------")
    user.open_book(3)
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    title=To Kill a Mockingbird
    author=Harper Lee
    text=Text of page 1
    """

    print(
        "-----------Попытаться перелистнуть на предыдущую страницу, находясь на первой странице-------------"
    )
    user.open_book(4)
    user.previous_page()
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )
    """
    Это первая страница
    title=To Kill a Mockingbird
    author=Harper Lee
    text=Text of page 1
    """

    print("-----------Открыть предыдущую книгу(должна быть на 100 странице)-------------")
    user.open_book(5)
    print(
        f"title={user.current_book.name}",
        f"author={user.current_book.author}",
        f"text={user.current_text}",
        sep="\n",
    )

    print("-----------Удалить текущую книгу из библиотеки-------------")
    user.remove_book(5)
    print(f"current_book={user.current_book}")
    print(f"books_len={len(library.collection.books)}")


if __name__ == "__main__":
    main()
