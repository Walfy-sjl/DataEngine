# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    modelline = scrapy.Field()
    question = scrapy.Field()
    questionlist = scrapy.Field()
    time = scrapy.Field()
    status = scrapy.Field()
