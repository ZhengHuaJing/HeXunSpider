# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from HeXun.items import HexunItem
import re
import requests


class HexunSpider(CrawlSpider):
    name = 'hexun'
    allowed_domains = ['hexun.com']
    start_urls = ['http://blog.hexun.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?.blog.hexun.com/.*?.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = HexunItem()
        # 文章标题
        item['art_title'] = response.xpath(".//*[@id='ArticeTextID']/div[1]/span/a/text()").extract()[0]
        # 链接
        item['art_link'] = response.url
        # 点击数
        item['click_num'] = self.get_num(response)[0]
        # 评论数
        item['comment_num'] = self.get_num(response)[1]

        yield item

    def get_num(self, response):
        pat_id = "http://click.tool.hexun.com/click.aspx\?articleid=(\d*)&blogid=(\d*)"
        res_id = re.compile(pat_id, re.S).findall(response.body.decode('utf-8','ignore'))[0]
        url = 'http://click.tool.hexun.com/click.aspx?articleid={}&blogid={}'.format(res_id[0],res_id[1])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Referer': response.url,
        }

        res = requests.get(url=url, headers=headers)
        pat_num = 'document.getElementById.*?= (\d*)'
        num = re.compile(pat_num, re.S).findall(res.text)

        return num
























