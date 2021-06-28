import requests
from bs4 import BeautifulSoup


r = requests.get('https://tw.stock.yahoo.com/q/q?s=2330')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    # table = soup.find_all('table', attrs={'border': '2'})
    table = soup.find_all('table')[2]
    # print(table)
    th = table.find_all('th')[2]

    price = table.find_all('td')[2]
    buy_price = price.find_next('td')
    sell_price = buy_price.find_next('td')
    # print(price)
    print(sell_price.text)