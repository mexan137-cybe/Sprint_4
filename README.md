# ## Тестирование

Для проверки работы класса `BooksCollector` написаны автотесты на фреймворке **pytest**. Тестами покрыта вся ключевая бизнес-логика: добавление книг, валидация полей, управление жанрами и работа со списками избранного.

### Архитектура тестов
* **Фикстуры (Fixtures):**
  * `books` — создает чистый экземпляр класса для изоляции тестов.
  * `books_collection` — создает предзаполненный объект с 5 книгами разных жанров для интеграционных проверок.

### Что именно проверяется (Тест-кейсы)
1. **Метод`add_new_book`:**
   * "test_add_new_book_valid_name_added" – проверяет добавление книги с валидным названием (длина от 1 до 40 символов).
   * "test_add_new_book_invalid_name_not_added" – проверяет, что книга не добавляется при невалидном названии (пустая строка или длина > 40 символов).
   * "test_add_new_book_repeat_add_book_not_added" – проверяет, что повторное добавление уже существующей книги не создаёт дубликат.
2. **Метод `set_book_genre`:**
   * "test_set_book_genre_valid_genre_assigned" – проверяет успешное присвоение жанра книге (жанр из допустимого списка).
   * "test_set_book_genre_invalid_genre_empty" – проверяет, что при указании недопустимого жанра у книги не устанавливается жанр.
   * "test_set_book_genre_invalid_book_name_empty" – проверяет, что при попытке установить жанр для несуществующей книги жанр не присваивается.
3. **Метод `get_book_genre`:**
    * "test_get_book_genre_valid_book_return_genre" – проверяет корректное получение жанра существующей книги.
4. **Метод `get_books_with_specific_genre`:**
   * "test_get_books_with_specific_genre_valid_genre_return_book" – проверяет получение списка книг по указанному жанру.
5. **Метод `get_books_genre`:**
   * "test_get_books_genre_return_books_genre" – проверяет получение словаря со всеми книгами и их жанрами (коллекция содержит 5 книг).
6. **Метод `get_books_for_children`:**
   * "test_get_books_for_children_return_books_for_children" – проверяет, что в списке для детей отсутствуют книги жанров "Ужасы" и "Детективы".
   * "test_get_books_for_children_return_count_books_for_children" – проверяет количество книг, подходящих для детей (из 5 книг только 3 имеют допустимые жанры).
7. **Метод `add_book_in_favorites` :**
    * "test_add_book_in_favorites_add_book_added" – проверяет успешное добавление книги в избранное.
    * "test_add_book_in_favorites_repeat_add_book_not_added" – проверяет, что повторное добавление книги в избранное не создаёт дубликат.
    * "test_add_book_in_favorites_non_existent_book_not_added" – проверяет, что несуществующая книга не добавляется в избранное.
8. **Метод `delete_book_from_favorites` :**
    * "test_delete_book_from_favorites_deleted_book" – проверяет успешное удаление книги из избранного.
    * "test_delete_book_from_favorites_non_existent_book_skip" – проверяет, что при попытке удалить несуществующую книгу из избранного другие книги не удаляются.
9. **Метод `get_list_of_favorites_books` :**
    * "test_get_list_of_favorites_books_return_favorites" – проверяет получение списка всех книг, добавленных в избранное.
