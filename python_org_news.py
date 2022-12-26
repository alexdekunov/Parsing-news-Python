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


def get_python_news(html):
    '''дерево которе преобразует Html в котором мы будем делать поиск'''
    soup = BeautifulSoup(html, 'html.parser')
    all_news = soup.find('ul')
    print(all_news)

if __name__ == "__main__":
    html = get_html("https://www.python.org/blogs/")
    if html:
        with open("python.org.html", "w", encoding="utf8") as f:
            f.write(html)
