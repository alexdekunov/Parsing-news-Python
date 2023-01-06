# Парсер погоды и новостей

Проект на flask который отображает текущую погоду в Москве и собирает новости с сайта.

1. Ставим flask `pip install flask`
2. Ставим requests `pip install requests`

## Сбор и отображение погоды на сайте
1. Регистриуемся на сайте 
2. Получаем ключ
3. Создаём файл setting.py
4. Добавляем переменную KEY, которая содержит ключ
    ```
    KEY = "ключ"
    URLS = "адрес сайта"
    ```
5. Делаем импорт из файла setting.py `from setting import KEY, URLS`


# Парсинг новостей
1. Для парсинга новостей устанавливаем библиотеку `pip install beautifulsoup4`
2. Добавляем в файл `from bs4 import BeautifulSoup`

# База данных
Для хранения информации создадим базу данных. Будем использовать пакет Flask-SQLAlchemy.
Установим библиотеку.
```
pip install flask-sqlalchemy
```
### Конфигурация
Задаём путь к нашей sqlite-базе.
Flask-SQLAlchemy ожидает найти этот параметр в конфигурации по ключу SQLALCHEMY_DATABASE_URI.

Помимо этого задаём путь к файлу не прописывая его "вручную".
Для этого импортируем в файл `config.py` библиотеку os `import os` и в переменной пишем путь
```commandline
SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(basedir, '..', 'webapp.db')
```
Для визуализации ставим DB Browser for SQLite, который дает удобный графический интерфейс.

### Опишем наши модели. 
создадим файл model.py 
```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()```

