import scrapy

class MainPySpider(scrapy.Spider):
    name = "preproc"
    allowed_domains = ["brickset.com"]

    start_year = "2015"
    start_urls = [f"https://brickset.com/sets/theme-Speed-Champions/year-{start_year}"]

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

        next_year = str(int(self.start_year) + 1)
        next_page = response.css(f'div.browselinks a[href*="/year-{next_year}"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
