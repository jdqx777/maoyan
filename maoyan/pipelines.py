# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class MaoyanPipeline(object):
    def __init__(self):
        self.score = 9
    def process_item(self, item, spider):
        if float(item['score']) < float(self.score):
            item['score'] = '评分低于9分，定义为不好看'
        if '\n' in item['star']:
            item['star'] = item['star'].replace('\n','').replace(' ','')
        return item

class JsonPipeline(object):
    def __init__(self):
        print('starting----------')
        self.file = codecs.open('maoyan.json','wb',encoding='utf-8')
    def process_item(self,item,spider):
        print('正在写入-------')
        line = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def close(self,spider):
        print('done------')
        self.file.close()