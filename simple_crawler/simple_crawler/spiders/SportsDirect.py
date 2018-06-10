# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem


class SportsdirectSpider(scrapy.Spider):
    name = 'SportsDirect'
    allowed_domains = ['sportsdirect.com']
    start_urls = ['https://www.sportsdirect.com/mens/mens-shirts',
                  'https://www.sportsdirect.com/mens/mens-rugby-boots']

    def parse(self, response):
        products = response.css('.s-productthumbbox')

        for product in products:
            brand = product.css('.productdescriptionbrand::text').extract_first()
            name = product.css('.productdescriptionname::text').extract_first()
            price = product.css('.curprice::text').extract_first()
            product_url = product.css('a::attr(href)').extract_first()
            item = ProductItem()
            item['brand'] = brand
            item['name'] = name
            item['price'] = price
            item['url'] = response.urljoin(product_url)
            request = scrapy.Request(url=response.urljoin(product_url), callback=self.parse_product)
            request.meta['item'] = item
            yield request

        next_page_link_selector = response.css('.NextLink::attr("href")')
        if next_page_link_selector:
            next_page_link = next_page_link_selector[0].extract()
            yield scrapy.Request(url=response.urljoin(next_page_link))

    @staticmethod
    def parse_product(response):
        item = response.meta['item']
        image_urls = response.css('a::attr(srczoom)').extract()
        item['image_urls'] = image_urls
        yield item
