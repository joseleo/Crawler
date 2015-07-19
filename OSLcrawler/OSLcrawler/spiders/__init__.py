# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from OSLcrawler.items import OslcrawlerItem

def parse_content(content):
    contentConcat = ""
    contentList = []

    for nodo in content:
        contentConcat += nodo

    contentList.append(contentConcat)
    return contentList

class oslSpider(CrawlSpider):
    name = 'OSL'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es']

    rules = (
        Rule(
            LinkExtractor(
                allow=(
                    '/page/\d+/',
                 ),
            ),
        ),

        Rule(
            LinkExtractor(
                allow=(
                    '/\d+/\d+/\d+/.+',
                ),
            ),
            callback = 'parse_item',
            follow = True
        ),
        
    )


    def parse_item(self, response):
        i = OslcrawlerItem()

        i['title'] = response.xpath('//h1[@class="entry-title format-icon"]/text()').extract()
        i['author'] = response.xpath('//span[@class="author vcard"]/a[@rel="author"]/text()').extract()
      	i['content'] = parse_content(response.xpath('//article/section/*[not(@class="shareinpost")]/node()').extract())
        i['categories'] = response.xpath('//header/div[@class="entry-meta"]/a[@class="btn btn-mini"]/text()').extract()
        i['labels'] = response.xpath('//header/div[@class="entry-meta"]/a[@class="btn btn-mini btn-tag"]/text()').extract() 

        return i


        
