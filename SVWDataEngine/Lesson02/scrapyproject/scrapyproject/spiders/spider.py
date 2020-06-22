# -*- coding: utf-8 -*-
import scrapy

from scrapyproject.items import ScrapyprojectItem

class SpiderSpider(scrapy.Spider):
    name = "12365auto"
    allowed_domains = ["www.12365auto.com"]
    start_urls = ['http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml']
    url_ll = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
    url_rr = '.shtml'

    def parse(self, response):
        numpagestr = response.xpath("//div[@class='p_page']/a/@href").getall()[-1]
        totalPage = int(numpagestr.split(".")[0].split("-")[-1])
        print("total page is:",totalPage)
        # totalPage = 2     为了减轻服务器压力，测试仅爬取两页
        for i in range(1,totalPage+1):
            pageUrl = self.url_ll + str(i) + self.url_rr
            yield scrapy.Request(pageUrl,callback=self.parse_page)

    def parse_page(self, response):
        trs = response.xpath("//div[@class='tslb_b']//tr")
        for tr in trs[1:]:
            item = ScrapyprojectItem()
            item['id'] = tr.xpath('./td[1]/text()').get()
            item['brand'] = tr.xpath('./td[2]/text()').get()
            item['model'] = tr.xpath('./td[3]/text()').get()
            item['modelline'] = tr.xpath('./td[4]/text()').get()
            item['question'] = tr.xpath('./td[5]/a/text()').get()
            item['questionlist'] = tr.xpath('./td[6]/text()').getall()
            item['time'] = tr.xpath('./td[7]/text()').get()
            item['status'] = tr.xpath('./td[8]/em/text()').get()
            yield item
