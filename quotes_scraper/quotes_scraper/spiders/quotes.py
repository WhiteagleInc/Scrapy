import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/page/1'
    ]

    def parse(self, response):
        print('*' * 20)
        print(response.status)
        print('\n')
        print(response.headers)
        print('*' * 20)