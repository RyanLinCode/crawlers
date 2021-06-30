from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

import pandas as pd
from pprint import pprint

def crawl(date):
    print('crawling', date.strftime('%Y/%m/%d'))
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
        print('no data for', date.strftime('%Y/%m/%d'))
        return

    rows = trs[3:]
    data = {}
    row_data = []

    for row in rows:
        tds = row.find_all('td')
        cells = [td.text.strip() for td in tds]

        ths = row.find_all('th')        
        titles = [ths.text.strip() for ths in ths]

        if titles[0] == '期貨小計':
            break

        if len(titles) == 3 and len(cells) ==12:
            product = titles[1:]
            row_data = product + cells
            
        elif len(titles) == 1 and len(cells) ==12:
            row_data = [product] + titles + cells
        # print(type(row_data[0]))

        coverted = [int(d.replace(',', '')) for d in row_data[2:]]
        row_data = row_data[:2] + coverted

        headers = ['商品', '身份別', '交易多方口數', '交易多方金額', '交易空方口數', '交易空方金額', '交易多空淨口數', '交易多空淨額',
                   '未平倉多方口數', '未平倉多方金額', '未平倉空方口數', '未平倉空方金額', '未平倉淨口數', '未平倉多空淨額']

        # product -> who -> what
        product = row_data[0]
        who = row_data[1]

        contents = {headers[i]: row_data[i] for i in range(2, len(headers))}

        # pprint(contents)
        # print(type(product))
        if product not in data:
            data[product] = {who: contents}
        else:
            data[product][who] = contents
    print(data['臺股期貨']['外資'])
    # print(data['美國道瓊期貨']['自營商']['交易多方口數'])
    # pprint(data)
    return data

        

            


date = datetime.today()
while True:
    crawl(date)
    date = date - timedelta(days=1)
    if date < datetime.today() - timedelta(days=30):
        break
    # crawl(date.year, daye.month, date.day)
    