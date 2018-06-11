# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }
            yield item

        # Pagination logic:
        # get Next button relative url
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            # build absolute ur
            next_page_url = response.urljoin(next_page_url)
            # yield a new request object for the url that we just found. callback - the method that is going to handle
            # the response to this request
            yield scrapy.Request(url=next_page_url, callback=self.parse)