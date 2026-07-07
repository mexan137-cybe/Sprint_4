import pytest
from main import BooksCollector

@pytest.fixture
def books():
        return BooksCollector()

def test_add_new_book_valid_name_added(books):
        name = '1984'
        books.add_new_book(name)
        assert name in books.books_genre

@pytest.mark.parametrize('name', ['', 'qwertyuiopasdfghjklzxcvbnmqwertyuikjhgfdq'])
def test_add_new_book_invalid_name_not_added(books, name):
        books.add_new_book(name)
        assert name not in books.books_genre