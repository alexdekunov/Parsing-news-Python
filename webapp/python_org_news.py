from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)  # берём данные из url адреса
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_python_news():
    '''дерево которе преобразует Html в котором мы будем делать поиск'''
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        # нашли ul с классом list-recent-posts и в это нашил все с li
        result_news = []
        # пройдёмся по all_news и распечатаем
        for news in all_news:
            title = news.find('a').text  # заголовок
            #print(title)
            url = news.find('a')['href']
            #print(url)
            published = news.find('time').text  # дата публикации  в виде текста
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
    #         #print(published)
    #         # положим все данные в словарь
    #         result_news.append({
    #             "title": title,
    #             "url": url,
    #             "published": published,
    #         })
    #     return result_news
    # return False


def save_news(title, url, published):
    # создаём фильтр для проверки количества уникальный урл что бы они не повторялись
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        # создали объект класс news
        new_news = News(title=title, url=url, published=published)
        # и теперь надо положить его в базу данных
        db.session.add(new_news)
        db.session.commit()

