from collections import defaultdict

import requests
from bs4 import BeautifulSoup
import csv


def get_category_links(url: str) -> list[str]:
    """Функция для получения списка ссылок на подкатегории"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    soup.find('div', attrs={'class': 'category-links'})
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'):
            links.append(href)
    return links


def count_animals_per_letter(category_url):
    """Функция для подсчета количества элементов в каждой подкатегории"""
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mw_pages_div = soup.find('div', id='mw-pages')
    if mw_pages_div is not None:
        divs = mw_pages_div.find_all('div', class_='mw-category-group')
        counts = {}
        for div in divs:
            letter = div.h3.text.strip().upper()
            animals = div.find_all('li')
            counts[letter] = len(animals)
        return counts
    else:
        return {}


def main():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    category_links = get_category_links(url)
    results = defaultdict(int)
    for link in category_links:
        counts = count_animals_per_letter(link)
        for k, v in counts.items():
            results[k] += v

    with open('beasts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for key, value in sorted(results.items()):
            writer.writerow([key, value])


if __name__ == "__main__":
    main()
