BOT_NAME = "city"
SPIDER_MODULES = ["city.spiders"]
NEWSPIDER_MODULE = "city.spiders"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 3
RETRY_TIMES = 10
DOWNLOAD_TIMEOUT = 3
CONCURRENT_REQUESTS = 128
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
