# coding:utf-8
import requests
import json

query = '王祖贤'
url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(1)
print(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

# url='https://www.baidu.com'
r = requests.get(url, headers=headers)
print(r.status_code)  # 打印状态码
html=r.text
# html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
print(html)