# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = (
        "http://www.thebestfreebooks.com/read/read-sabriel-abhorsen-1-online/291193",
    )

    def parse(self, response):
        plist = response.css('p::text').extract()
        plist_formatted = [paragraph.strip() for paragraph in plist]
        yield {
            'text': plist_formatted
        }
