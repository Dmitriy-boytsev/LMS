import json
import os
from typing import List, Optional


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Инициализирует объект книги.

        id: Идентификатор книги.
        title: Название книги.
        author: Автор книги.
        year: Год издания книги.
        status: Статус книги.
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def to_dict(self) -> dict:
        """
        Преобразует объект книги в словарь.

        return: Словарь с данными книги.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """
        Создает объект книги из словаря.

        data: Словарь с данными книги.
        :return: Объект книги.
        """
        return cls(data["id"], data["title"], data["author"], data["year"], data["status"])


class Library:
    def __init__(self, data_file: str = 'data.json'):
        """
        Инициализирует объект библиотеки.

        data_file: Файл для хранения данных о книгах.
        """
        self.data_file = data_file
        self.books: List[Book] = []
        self.load_books()


    def load_books(self) -> None:
        """
        Загружает книги из файла данных.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    books_data = json.load(f)
                    self.books = [Book.from_dict(book) for book in books_data]
            except json.JSONDecodeError:
                self.books = []
        else:
            self.books = []


    def save_books(self) -> None:
        """
        Сохраняет книги в файл данных.
        """
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)


    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет книгу в библиотеку.

        title: Название книги.
        author: Автор книги.
        year: Год издания книги.
        """
        new_id = self.generate_id()
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с id {new_id}")


    def generate_id(self) -> int:
        """
        Генерирует новый уникальный идентификатор для книги.

        Новый идентификатор книги.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1


    def remove_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по ID.

        book_id: Идентификатор книги для удаления.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с id {book_id} удалена")
        else:
            print(f"Книга с id {book_id} не найдена")


    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        """
        Находит книгу по ее идентификатору.

        book_id: Идентификатор книги.
        :return: Объект книги, если найден, иначе None.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None


    def search_books(self, title: str = "", author: str = "", year: int = None) -> List[Book]:
        """
        Ищет книги по заданным критериям.

        title: Название книги.
        author: Автор книги.
        year: Год издания книги.
        :return: Список найденных книг.
        """
        results = []
        for book in self.books:
            if title.lower() in book.title.lower() or author.lower() in book.author.lower() or (year and book.year == year):
                results.append(book)
        return results


    def display_books(self) -> None:
        """
        Отображает все книги в библиотеке.
        """
        if not self.books:
            print("В библиотеке нет книг.")
        for book in self.books:
            print(f"id: {book.id}, title: {book.title}, author: {book.author}, year: {book.year}, status: {book.status}")


    def change_status(self, book_id: int, status: str):
        """
        Изменяет статус книги по ее id.
    
        :param book_id: идентификатор книги
        :param status: новый статус книги
        """
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            print(f"Статус книги с id {book_id} изменен на '{status}'")
        else:
            print(f"Книга с id {book_id} не найдена")
