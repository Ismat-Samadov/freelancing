import scrapy


class TelegramSpider(scrapy.Spider):
    name = "telegram"
    allowed_domains = ["www.bestoftelegram.com/channels/"]
    start_urls = ["https://www.bestoftelegram.com/channels/"]

    def parse(self, response):
        categories = response.xpath("/html/body/section[2]/div/div/div/div/div/a/@href").getall()
        for category in categories:
            yield {"   Links     ": f"https://www.bestoftelegram.com/channels/{category}"}
    #
    #
    #
    #
    #
    # response.follow(, callback=self.parse_country, meta={'link':category})
    #
    #
    # # scrapy.Request(url=f"https://www.bestoftelegram.com/channels/{category}")

# def parse_category(self, response):
#     channels = response.xpath("/html/body/section[2]/div/div/div/div/a[2]").getall()
#     for channel in channels:
#         yield {"link": channel}
