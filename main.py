import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')


    catalog = soup.find('div', class_='list-view')
    phones = catalog.find_all('div', class_='item product_listbox oh')

    for i in phones:
        try:
            title = i.find('div', class_='listbox_title oh').text.strip()
        except:
            title = ''
        try:
            img = 'https://www.kivano.kg/mobilnye-telefony' + i.find('img').get('src')
            
        except:
            img = ''
        try: 
            price = i.find('div', class_ = 'listbox_price text-center').find('strong').text
        except:
            price = ''

        with open('phones.csv', 'a') as file:
            fields = ['title', 'price','image']
            writer = csv.DictWriter(file, delimiter=',', fieldnames=fields)
            writer.writerow({'title': title,'price':price, 'image': img})

def main():
    for i in range(1,16):
    
        URL = 'https://www.kivano.kg/mobilnye-telefony'
        url = URL + f'page-{i}/'
        html = get_html(URL)
        get_data(html)



main()