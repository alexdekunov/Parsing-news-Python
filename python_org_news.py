import requests
from bs4 import BeautifulSoup

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
            published = news.find('time').text  # дата публикации
            #print(published)
            # положим все данные в словарь
            result_news.append({
                "title": title,
                "url": url,
                "published": published,
            })
        return result_news
    return False

