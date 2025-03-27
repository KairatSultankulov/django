import requests
from bs4 import BeautifulSoup

URL = "https://mybook.ru/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

#1 создание запроса
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2 Получение данных через html (Консоль разработчика)
def get_data(html):
    bs = BeautifulSoup(html, features="html.parser")
    items = bs.find_all("div", class_="e4xwgl-0 iJwsmp")
    mybook_list = []
    for item in items:
        title = item.find("div", class_='e4xwgl-1 gEQwGK').get_text(strip=True)
        mybook_list.append({
            "title": title,

        })
    return mybook_list

#3 Функционал парсинга и объединение 2х функций в 1
def parsing_mybook():
    response = get_html(URL)
    if response.status_code == 200:
        mybook_list2 = []
        for page in range(1,2):
            response = get_html("https://mybook.ru/catalog/books/", params={'page': page})
            mybook_list2.extend(get_data(response.text))
        return  mybook_list2
    else:
        raise Exception("error in parsing")

#print(parsing_mybook())