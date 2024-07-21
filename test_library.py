import pytest
import os
import json
from library import Library, Book


@pytest.fixture
def library(tmpdir):
    """
    Фикстура для создания экземпляра библиотеки с временным файлом данных.
    """
    data_file = tmpdir.join("data.json")
    return Library(str(data_file))


def test_add_book(library):
    """
    Тест добавления книги в библиотеку.
    """
    library.add_book("Test Title", "Test Author", 2022)
    assert len(library.books) == 1
    assert library.books[0].title == "Test Title"
    assert library.books[0].author == "Test Author"
    assert library.books[0].year == 2022


def test_remove_book(library):
    """
    Тест удаления книги из библиотеки.
    """
    library.add_book("Test Title", "Test Author", 2022)
    book_id = library.books[0].id
    library.remove_book(book_id)
    assert len(library.books) == 0


def test_change_status(library):
    """
    Тест изменения статуса книги в библиотеке.
    """
    library.add_book("Test Title", "Test Author", 2022)
    book_id = library.books[0].id
    print(f"До изменения: {library.books[0].status}")
    library.change_status(book_id, "выдана")
    print(f"После изменения: {library.books[0].status}")
    assert library.books[0].status == "выдана"


def test_search_books(library):
    """
    Тест поиска книги в библиотеке.
    """
    library.add_book("Test Title", "Test Author", 2022)
    results = library.search_books(title="Test Title")
    assert len(results) == 1
    assert results[0].title == "Test Title"


def test_save_and_load_books(library):
    """
    Тест сохранения и загрузки книг в библиотеке.
    """
    library.add_book("Test Title", "Test Author", 2022)
    library.save_books()
    
    new_library = Library(library.data_file)
    assert len(new_library.books) == 1
    assert new_library.books[0].title == "Test Title"
    assert new_library.books[0].author == "Test Author"
    assert new_library.books[0].year == 2022


def test_find_book_by_id(library):
    """
    Тест поиска книги по идентификатору.
    """
    library.add_book("Test Title", "Test Author", 2022)
    book_id = library.books[0].id
    found_book = library.find_book_by_id(book_id)
    assert found_book is not None
    assert found_book.title == "Test Title"


def test_display_books(capsys, library):
    """
    Тест отображения всех книг в библиотеке.
    """
    library.add_book("Test Title", "Test Author", 2022)
    library.display_books()
    captured = capsys.readouterr()
    assert "Test Title" in captured.out


def test_empty_library_display_books(capsys, library):
    """
    Тест отображения книг в пустой библиотеке.
    """
    library.display_books()
    captured = capsys.readouterr()
    assert "В библиотеке нет книг." in captured.out
