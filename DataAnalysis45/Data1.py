import requests
from lxml import etree


# r = requests.get('https://www.douban.com')
# r = requests.post('http://xxx.com', data = {'key':'value'})
url='https://www.baidu.com'
r = requests.get(url)
html=r.content
html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
print(html_doc)
html = etree.HTML(html)
result = html.xpath('//div')
print(result)

