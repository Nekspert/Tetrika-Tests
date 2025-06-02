import requests
from bs4 import BeautifulSoup, Tag, ResultSet

base_url = 'https://ru.wikipedia.org/'


class Parser:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.first_url = base_url + ('wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:'
                                     '%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE'
                                     '_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83')
        self.pages: list[str] = []
        self.res: dict[str, int] = {}

    def parsing(self):
        soup = BeautifulSoup(requests.get(self.first_url).text, 'lxml')
        hrefs: set[str] = set()
        count = 0
        while ((href := soup.find_all('a', attrs={'title': 'Категория:Животные по алфавиту'})[-1].get('href'))
               not in hrefs):
            hrefs.add(href)
            soup = BeautifulSoup(requests.get(base_url + href).text, 'lxml')
            data: Tag = soup.find('div', attrs={'class': 'mw-category-columns'})
            letters_per_page: ResultSet[Tag] = data.find_all('div', attrs={'class': 'mw-category-group'})
            for letter_data in letters_per_page:
                letter = letter_data.find('h3').text
                for _ in letter_data.find('ul').find_all('li'):
                    count += 1
                if letter not in self.res:
                    self.res[letter] = count
                else:
                    self.res[letter] += count
                count = 0

        self.save_data()

    def save_data(self):
        with open('beasts.csv', 'w', encoding='utf-8', newline='\n') as file:
            for letter in self.res:
                file.write(letter + ',' + str(self.res[letter]) + '\n')




if __name__ == '__main__':
    p = Parser(base_url)
    p.parsing()
