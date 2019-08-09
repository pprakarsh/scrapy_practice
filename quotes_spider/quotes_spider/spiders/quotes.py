# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
       # h1_tag = response.xpath("//h1/a/text()").extract_first
       # tags = response.xpath("//*[@class='tag-item']/a/text()").extract()
       # yield {'H1 tag': h1_tag, 'Tags': tags}
       quotes = response.xpath('//*[@class="text"]/text()').extract()
       authors = response.xpath('//*[@class="author"]/text()').extract()
       
       for i in range(len(quotes)):
           yield{'quote': quotes[i], 'author': authors[i]}

       next_page_url = response.xpath('//*[@class="next"]/a/@href').extract()
       if next_page_url != []:
           absolute_next_page_url = response.urljoin(next_page_url[0])
           yield scrapy.Request(absolute_next_page_url)

