import scrapy


class TelegramSpider(scrapy.Spider):
    name = "telegram"
    allowed_domains = ["www.bestoftelegram.com"]
    start_urls = ["https://www.bestoftelegram.com"]

    def parse(self, response):
        pass
