# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector 
from scrapy import Spider,FormRequest
from ndcg.items import NdcgItem
import json
class BingSpider(Spider) :
    name = 'bing'
    allowed_domains=['www.bing.com']
    sites = []
    
    rank = 1
    def start_requests(self) :
        f = open('source.json','r')
        urldict = json.loads(f.read())
        f.close()
        self.queries = [] 
        queries= urldict.keys()
        for ss in range(50) :
            query = queries.pop(0)
            for ii in range(5) :
                self.queries.append(query)
                yield FormRequest(urldict[query]+"&first=%s1" % ii)

    def parse(self,response):
        print(response.xpath('//title').extract())
        sel = response.xpath('//title')
        result_list = sel.xpath("//li[@class='b_algo']")
        items = []
        query = self.queries.pop(0)
        for result in result_list :
            item = NdcgItem()
            item['query']=query
            title = " ".join(result.xpath(".//h2/a//text()").extract())
            title=title.replace('- Wikipedia','').replace('…','').replace('...','')
            item['title']=title.encode('utf-8')
            item['rank']=self.rank
            items.append(item)
            self.rank += 1
            if(self.rank > 50) :self.rank=1
        for it in items :
            yield it
