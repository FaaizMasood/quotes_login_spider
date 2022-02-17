import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoginspiderSpider(scrapy.Spider):
    name = 'loginSpider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath(
            './/*[@name="csrf_token"]/@value').extract_first()
        # This is new funtion that is usefull to login    #rememberPoint1
        yield FormRequest('https://quotes.toscrape.com/login', formdata={'csrf_token': csrf_token, 'username': 'foobar', 'password': 'foobar'},
                          callback=self.parse_after_login)

    def parse_after_login(self, response):
        # if response.xpath('.//a[text()="Logout"]'):
        #self.log('Wow Faaiz you logged in')
        open_in_browser(response)
