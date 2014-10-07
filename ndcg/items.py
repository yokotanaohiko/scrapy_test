# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class NdcgItem(Item):
    # define the fields for your item here like:
    query = Field()
    title = Field()
    rank= Field()
    pass
