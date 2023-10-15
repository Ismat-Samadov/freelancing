import scrapy


class SinglePageSpider(scrapy.Spider):
    name = "single_page"
    allowed_domains = ["www.city-data.com"]
    start_urls = ["https://www.city-data.com/city/Abernant-Alabama.html"]

    def parse(self, response):
        city_name = response.css('h1.city span::text').get()
        state = city_name.split(', ')[-1]
        zip_code = response.css('section#zip-codes a::text').get()
        income_2021 = response.xpath(
            '//b[contains(text(), "Estimated median household income in 2021:")]/following-sibling::text()[1]').get()
        income_2000 = response.xpath('//b[contains(text(), "it was")]/following-sibling::text()[1]').get()
        income_2021 = income_2021.split(' ')[1].replace(',', '') if income_2021 else None
        income_2000 = income_2000.split(' ')[1].replace(',', '') if income_2000 else None
        land_area = response.xpath('//*[@id="population-density"]/p[1]/text()').get().strip()
        latitude = response.xpath('//*[@id="coordinates"]/p/text()[1]').get().strip()
        longitude = response.xpath('//*[@id="coordinates"]/p/text()[2]').get().strip()
        population = response.xpath('//*[@id="city-population"]/text()').get().strip()
        data = {
            'city': city_name.split(', ')[0],
            'state': state,
            'zip_code': zip_code,
            'income_2021': income_2021,
            'income_2000': income_2000,
            'land_area': land_area,
            'latitude': latitude,
            'longitude': longitude,
            'population': population,
        }
        yield data
