import scrapy


class StateSpider(scrapy.Spider):
    name = 'state'
    start_urls = ['https://www.city-data.com/']

    def parse(self, response):
        state_links = response.css('ul.tab-list.tab-list-short li a')[:52]
        for state_link in state_links:
            state_href = state_link.css('::attr(href)').get()
            state_name = state_link.css('::text').get()  # Extract state name
            yield response.follow(state_href, self.parse_state, meta={'state_name': state_name})

    def parse_state(self, response):
        cities = response.css('tr.rB td a::attr(href)').getall()
        for city in cities:
            yield response.follow(city, self.parse_city, meta=response.meta)

    def parse_city(self, response):
        city_name = response.css('h1.city span::text').get()
        state_name = response.request.meta['state_name']
        zip_code = response.css('section#zip-codes a::text').get()
        income_2021 = response.xpath('//b[contains(text(), "Estimated median household income in 2021:")]/following-sibling::text()[1]').get()
        income_2000 = response.xpath('//b[contains(text(), "it was")]/following-sibling::text()[1]').get()
        income_2021 = income_2021.split(' ')[1].replace(',', '') if income_2021 else None
        income_2000 = income_2000.split(' ')[1].replace(',', '') if income_2000 else None
        land_area = response.xpath('//*[@id="population-density"]/p[1]/text()').get()
        latitude = response.xpath('//*[@id="coordinates"]/p/text()[1]').get()
        longitude = response.xpath('//*[@id="coordinates"]/p/text()[2]').get()
        population = response.xpath('//*[@id="city-population"]/text()').get()
        data = {
            'city': city_name.split(', ')[0],
            'state': state_name,
            'zip_code': zip_code,
            'income_2021': income_2021,
            'income_2000': income_2000,
            'land_area': land_area,
            'latitude': latitude,
            'longitude': longitude,
            'population': population,
        }
        yield data
