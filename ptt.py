import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'

r = requests.get('https://disp.cc/b/PttHot')

# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

# find_all

# spans = soup.find_all('span', class_='listTitle')
# # print([s.text for s in spans])
# for span in spans:
    
#     href = span.find('a').get('href')
    
#     if href == '796-59l9':
#         break

#     url = root_url + href
#     title = span.text

#     print(f'{title}\n{url}')
    

for span in soup.select('span.listTitle'):

    href = span.find('a').get('href')    
    if href == '796-59l9':
        break

    url = root_url + href
    title = span.text
    print(f'{title}\n{url}')