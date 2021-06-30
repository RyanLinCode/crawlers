from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

import pandas as pd

def crawl(date):
    r = requests.get('https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={}%2F{}%2F{}'.format(date.year, date.month, date.day))
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        print('sucessfully got data from', date)
    else:
        print('connection error')

    try:
        table = soup.find('table', class_='table_f')
        trs = table.find_all('tr')
    except AttributeError:
        print('no data for', date)
        return

    rows = trs[3:]
    data = []
    for row in rows:
        tds = row.find_all('td')
        cells = [td.text.strip() for td in tds]

        ths = row.find_all('th')        
        titles = [ths.text.strip() for ths in ths]


        if len(titles) == 3 and len(cells) ==12:
            product = titles[1:]
            data = product + cells

        elif len(titles) == 2 and len(cells) ==12:
            product = titles[0:1]
            data = titles + cells

        elif len(titles) == 1 and len(cells) ==12:
            if titles[0] == '期貨合計':
                data = titles + cells
            else:
                data = [product[0]] + titles + cells
        print(data)

        
            
            


date = datetime.today()
while True:
    crawl(date)
    date = date - timedelta(days=1)
    if date < datetime.today() - timedelta(days=1):
        break
    # crawl(date.year, daye.month, date.day)
    