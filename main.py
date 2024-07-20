from library import Library

def add_book(library: Library) -> None:
    """
    Добавляет книгу в библиотеку.

    library: Объект библиотеки.
    """
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания книги: "))
    library.add_book(title, author, year)

def remove_book(library: Library) -> None:
    """
    Удаляет книгу из библиотеки по ID.

    library: Объект библиотеки.
    """
    book_id = int(input("Введите id книги, которую хотите удалить: "))
    library.remove_book(book_id)

def search_books(library: Library) -> None:
    """
    Ищет книги в библиотеке по заданному критерию.

    library: Объект библиотеки.
    """
    search_by = input("Искать по title, author или year? ").lower()
    if search_by == "title":
        title = input("Введите название книги: ")
        books = library.search_books(title=title)
    elif search_by == "author":
        author = input("Введите автора книги: ")
        books = library.search_books(author=author)
    elif search_by == "year":
        year = int(input("Введите год издания книги: "))
        books = library.search_books(year=year)
    else:
        print("Некорректный критерий поиска")
        return

    for book in books:
        print(f"id: {book.id}, title: {book.title}, author: {book.author}, year: {book.year}, status: {book.status}")

def display_books(library: Library) -> None:
    """
    Отображает все книги в библиотеке.

    library: Объект библиотеки.
    """
    library.display_books()

def change_status(library: Library) -> None:
    """
    Изменяет статус книги в библиотеке.

    library: Объект библиотеки.
    """
    book_id = int(input("Введите id книги: "))
    status = input("Введите новый статус книги (в наличии/выдана): ")
    library.change_status(book_id, status)

def exit_program(library: Library) -> None:
    """
    Завершает выполнение программы.

    library: Объект библиотеки.
    """
    print("Выход из программы.")
    exit()

def main() -> None:
    """
    Основная функция программы, которая предоставляет пользователю меню для взаимодействия с библиотекой.
    """
    library = Library()
    actions = {
        "1": add_book,
        "2": remove_book,
        "3": search_books,
        "4": display_books,
        "5": change_status,
        "6": exit_program
    }

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("Выберите опцию: ")

        action = actions.get(choice)
        if action:
            action(library)
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
