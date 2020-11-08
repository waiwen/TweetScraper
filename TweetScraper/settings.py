# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
# USER_AGENT = 'TweetScraper'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'

PROXIES = ["127.0.0.1:1087"]

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    # 'TweetScraper.pipelines.SaveToFilePipeline':100,
    'TweetScraper.pipelines.CsvUserPipeline': 101,
    'TweetScraper.pipelines.CsvTweetPipline': 102,
}
DOWNLOADER_MIDDLEWARES = {
    'TweetScraper.middlewares.DownloaderProxyMiddleware': 543,
}

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'
SAVE_CSV_TWEET_PATH = './Data/csv/tweet/'
SAVE_CSV_USER_PATH = './Data/csv/user/'

DOWNLOAD_DELAY = 1.0

# settings for selenium
from shutil import which
SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_BROWSER_EXECUTABLE_PATH = "/Applications/Firefox.app/Contents/MacOS/firefox"
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS = ['-headless']  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
