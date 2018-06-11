# -*- coding: utf-8 -*-
import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        # extract the csrf token value
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        # create a dict with the form value to be sent to the server on login
        data = {
            'csrf_token': token,
            'username': 'admin',
            'password': 'admin'
        }
        # create&submit a post request
        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        """parse  the main page after the spider has logged in"""
        quotes = response.css('div.quote')
        for q in quotes:
            yield {
                'author_name': q.css('small.author::text').extract_first(),
                'author_url': q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()
            }
