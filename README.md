# Effective_Mobile_test_task

**create venv:**
python3 -m venv .venv

**run venv:**
. .venv/bin/activate

**run project:**
python main.py

**Main menu description**\
Commands:\
1 or Display all books - Отображение всех книг\
2 or Book search - Поиск книги\
3 or Adding a book - Добавление книги\
4 or Deleting a book - Удаление книги\
5 or Changing status - Изменение статуса книги\
6 or Exit - Выход из приложения

**Display all books description**\
Отображаются все книги\
id: уникальный идентификатор, генерируется автоматически\
title: название книги\
author: название книги\
year: год издания\
status: статус книги - “в наличии”, “выдана”

**Book searchain menu description**\
Search commands:\
1 or Search by title - поиск по названию книги\
2 or Search by author - поиск по автору книги\
3 or Search by year - поиск по году издания\
4 or Exit - выход из меню поиска

**Adding a book description**\
Enter book title: добавить название книги\
Enter book author: добавить автора книги\
Enter book year: добавить год издания книги

**Deleting a book description**\
Enter book ID: ввести ID книги для удаления

**Changing status description**\
Enter book ID: ввести ID книги для изменения статуса книги (“в наличии” или “выдана”)

\
Все данные хранятся в db.json файле в директории json

