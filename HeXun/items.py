# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunItem(scrapy.Item):
    # 文章标题
    art_title = scrapy.Field()
    # 链接
    art_link = scrapy.Field()
    # 点击数
    click_num = scrapy.Field()
    # 评论数
    comment_num = scrapy.Field()