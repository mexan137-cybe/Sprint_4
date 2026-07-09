import pytest
from main import BooksCollector

@pytest.fixture
def books():
    return BooksCollector()

@pytest.fixture
def books_collection():
    collection = BooksCollector()
    name_books = ['Звездные войны', 'Оно', 'Агата Кристи', 'Колобок', 'Золотой телёнок']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(len(name_books)):
        collection.add_new_book(name_books[i])
        collection.set_book_genre(name_books[i], genre[i])
    return collection

@pytest.mark.parametrize('name', ['1', 'qwertyuiopasdfghjklzxcvbnmqwertyuikjhgfd'])
def test_add_new_book_valid_name_added(books,name):
    books.add_new_book(name)
    assert name in books.books_genre

@pytest.mark.parametrize('name', ['', 'qwertyuiopasdfghjklzxcvbnmqwertyuikjhgfdq'])
def test_add_new_book_invalid_name_not_added(books, name):
    books.add_new_book(name)
    assert name not in books.books_genre

def test_add_new_book_repeat_add_book_not_added(books):
    name = 'Русалочка'
    for _ in range(2):
        books.add_new_book(name)
    assert len(books.books_genre) == 1

@pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
def test_set_book_genre_valid_genre_assigned(books, genre):
    name = 'Джо'
    books.add_new_book(name)
    books.set_book_genre(name, genre)
    assert books.books_genre[name] == genre

def test_set_book_genre_invalid_genre_empty(books):
    name = 'Джо'
    books.add_new_book(name)
    books.set_book_genre(name, 'Триллер')
    assert books.books_genre[name] == ''

def test_set_book_genre_invalid_book_name_empty(books):
    books.set_book_genre('Мастер и Маргарита', 'Ужасы')
    assert 'Мастер и Маргарита' not in books.books_genre

def test_get_book_genre_valid_book_return_genre(books):
    name = 'Джо'
    books.add_new_book(name)
    books.set_book_genre(name, 'Ужасы')
    print(books.get_book_genre(name))
    assert books.get_book_genre(name) == 'Ужасы'

def test_get_books_with_specific_genre_valid_genre_return_book(books_collection):
    name = 'Омен'
    books_collection.add_new_book(name)
    books_collection.set_book_genre(name, 'Ужасы')
    x = books_collection.get_books_with_specific_genre('Ужасы')
    assert name in x and len(x) == 2

def test_get_books_genre_return_books_genre(books_collection):
    assert len(books_collection.get_books_genre()) == 5

def test_get_books_for_children_return_books_for_children(books_collection):
    assert 'Оно' not in books_collection.get_books_for_children() and 'Агата Кристи' not in books_collection.get_books_for_children()

def test_get_books_for_children_return_count_books_for_children(books_collection):
    assert len(books_collection.get_books_for_children()) == 3

def test_add_book_in_favorites_add_book_added(books_collection):
    horror = books_collection.get_books_with_specific_genre('Ужасы')
    books_collection.add_book_in_favorites(horror[0])
    assert books_collection.favorites == ['Оно']

def test_add_book_in_favorites_repeat_add_book_not_added(books_collection):
    horror = books_collection.get_books_with_specific_genre('Ужасы')
    for _ in range(2):
        books_collection.add_book_in_favorites(horror[0])
    assert books_collection.favorites == ['Оно']

def test_add_book_in_favorites_non_existent_book_not_added(books_collection):
    books_collection.add_book_in_favorites('Омен')
    assert len(books_collection.favorites) == 0

def test_delete_book_from_favorites_deleted_book(books_collection):
    name = 'Агата Кристи'
    books_collection.add_book_in_favorites(name)
    books_collection.delete_book_from_favorites(name)
    assert len(books_collection.favorites) == 0

def test_delete_book_from_favorites_non_existent_book_skip(books_collection):
    books_collection.add_book_in_favorites('Агата Кристи')
    books_collection.delete_book_from_favorites('Оно')
    assert books_collection.favorites == ['Агата Кристи']

def test_get_list_of_favorites_books_return_favorites(books_collection):
    books_collection.add_book_in_favorites('Агата Кристи')
    books_collection.add_book_in_favorites('Оно')
    assert books_collection.get_list_of_favorites_books() == ['Агата Кристи', 'Оно']
    