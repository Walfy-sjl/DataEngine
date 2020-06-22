import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
}

def get_total_page(df):
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
    html_response = requests.get(url=url, headers=headers)
    # print(html_response.text)
    soup = BeautifulSoup(html_response.text, 'lxml')
    numpagestr = soup.select(".p_page a")[-1]['href']
    totalPage = int(numpagestr.split(".")[0].split("-")[-1])
    # totalPage = 2
    for i in range(1, totalPage + 1):
        page_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-{}.shtml'.format(i)
        print('=' * 10, page_url)
        items = parse_page(page_url)
        print('items--------',items)
        df = df.append(items, ignore_index=True)
    return df

def parse_page(url):
    items = pd.DataFrame(columns=['id', 'brand', 'model', 'modelline', 'question', 'questionlist', 'time', 'status'])
    html_response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html_response.text, 'lxml')
    tr_list = soup.find_all('tr')[1:]
    # print(tr_list)
    item = {}
    for tr in tr_list:
        tds = tr.find_all('td')
        print(tds)
        item['id'] = tds[0].text
        item['brand'] = tds[1].text
        item['model'] = tds[2].text
        item['modelline'] = tds[3].text
        item['question'] = tds[4].text
        item['questionlist'] = tds[5].text
        item['time'] = tds[6].text
        item['status'] = tds[7].text
        # print('item--------',item)
        items = items.append(item, ignore_index=True)
    # print('items--------',items)
    return items


res = pd.DataFrame(
    columns=['id', 'brand', 'model', 'modelline', 'question', 'questionlist', 'time', 'status'])

ress = get_total_page(res)
print('=' * 10, ress)
ress.to_csv("res.csv")
# print("hello world")
