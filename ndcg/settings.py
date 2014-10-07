# -*- coding: utf-8 -*-

# Scrapy settings for ndcg project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ndcg'
USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'

SPIDER_MODULES = ['ndcg.spiders']
NEWSPIDER_MODULE = 'ndcg.spiders'
DOWNLOAD_DELAY=3
ROBOTTXT_OBEY=True
ITEM_PIPELINES = ['ndcg.pipelines.NdcgPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ndcg (+http://www.yourdomain.com)'
