import pytest
from main import BooksCollector

@pytest.fixture
def books():
    return BooksCollector()

@pytest.fixture
def books_collection(books):
    name_books = ['Звездные войны', 'Оно', 'Агата Кристи', 'Колобок', 'Золотой телёнок']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(len(name_books)):
        books.add_new_book(name_books[i])
        books.set_book_genre(name_books[i], genre[i])
    return books