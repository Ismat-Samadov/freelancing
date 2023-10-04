import scrapy


class MainPySpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["brickset.com"]
    start_urls = ["https://brickset.com/sets/theme-Speed-Champions/year-2015"]

    def parse(self, response):
        for set_item in response.css('article.set'):
            numbers = response.css('h1 a span::text').get()
            title = set_item.css('h1 a::text').get()
            rrp = set_item.css('dt:contains("RRP") + dd::text').get()
            launch_exit = set_item.css('dt:contains("Launch/exit") + dd::text').get()
            yield {
                'product_number': numbers,
                'title': title,
                'rrp': rrp,
                'launch_exit': launch_exit,
            }

        next_page = response.css('div.browselinks a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
