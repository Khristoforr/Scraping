KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get('https://habr.com/ru/all/')
    if not response.ok:
        raise Exception('Error')
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    return make_a_soup(soup)

def make_a_soup(soup):
    descriptions = soup.find_all('article')
    for description in descriptions:
       # приходится создать 2 версии описания, т.к. структура сайта имеет два класса для описания статьи
       body_version_1 = description.find_all(class_ = 'article-formatted-body article-formatted-body_version-1')
       body_version_2 = description.find_all(class_ = 'article-formatted-body article-formatted-body_version-2')
       for i in body_version_1:
           word = i.text.strip().lower()
           if set(word.split()) & KEYWORDS:
               print(f"Дата публикации: {description.find('time').attrs.get('datetime')[:10]},"
                     f" название: {description.find('h2').find('a').find('span').text.strip()},"
                     f" ссылка: {description.find('h2').find('a').attrs.get('href')}")
       for i in body_version_2:
           word = i.text.strip().lower()
           if set(word.split()) & KEYWORDS:
               print(f"Дата публикации: {description.find('time').attrs.get('datetime')[:10]},"
                     f" название: {description.find('h2').find('a').find('span').text.strip()},"
                     f" ссылка: {description.find('h2').find('a').attrs.get('href')}")

if __name__ == '__main__':
    main()