# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class HexunPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        self.mdb = client[settings['MONGODB_DBNAME']][settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        self.mdb.insert(dict(item))
        return item
