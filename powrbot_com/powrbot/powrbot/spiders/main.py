import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["powrbot.com"]
    base_url = "https://powrbot.com/companies/list-of-companies-in-saudi-arabia/?page={}"
    start_page = 1

    def start_requests(self):
        yield scrapy.Request(url=self.base_url.format(self.start_page), callback=self.parse)

    def parse(self, response):
        companies = response.css('.d-block')
        for company in companies:
            company_name = company.css('h5::text').get()
            company_name = company_name.strip() if company_name else None  # Clean up company name
            company_link = company.css('a::attr(href)').get()
            yield {
                'company_name': company_name,
                'company_link': company_link,
                'page': self.start_page,

            }

        self.start_page += 1

        next_page_url = self.base_url.format(self.start_page)
        yield scrapy.Request(url=next_page_url, callback=self.parse)
