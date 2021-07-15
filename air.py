import re
import requests
import pprint


r = requests.get('https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2021071511.json')
if r.status_code == requests.codes.ok:
    data = r.json()

    for d in data:
        name = d['Name']
        if 'AQI' not in name:
            continue

        result =re.search(r'(.+)\(AQI=(\d+)', name)
        if result == None:
            continue

        site_name = result.group(1)

        aqi = result.group(2)

        print(site_name, aqi) 