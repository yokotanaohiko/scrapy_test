# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class NdcgPipeline(object):
    def __init__(self):
        self.tmp = codecs.open('result/bing_ranking.csv',"w",encoding='utf-8')
    def process_item(self, item, spider):
        #line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.tmp.write("%s,%s,%s\n" %(item['query'],item['title'],item['rank']))
        return item
    def spider_closed(self,spider) :
        self.tmp.close()
