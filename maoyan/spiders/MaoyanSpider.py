# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
import time


class MaoyanspiderSpider(scrapy.Spider):
    name = 'MaoyanSpider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board']

    def parse(self, response):

        dl = response.css('.board-wrapper dd')
        print('#'*100)
        print(dl)

        print(type(dl))
        print('#' * 100)

        for dd in dl:
            item = MaoyanItem()
            item['index'] = dd.css('.board-index::text').extract_first()
            item['title'] = dd.css('.name a::text').extract_first()
            item['star'] = dd.css('.star::text').extract_first()
            item['releasetime'] = dd.css('.releasetime::text').extract_first()
            item['score'] = dd.css('.integer::text').extract_first()+dd.css('.fraction::text').extract_first()
            yield item
