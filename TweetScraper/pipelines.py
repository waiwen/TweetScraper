import os, logging, json
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User
from TweetScraper.utils import mkdirs
from scrapy.exporters import CsvItemExporter
import datetime
logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()

class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''

    def __init__(self):
        self.saveTweetPath = SETTINGS['SAVE_TWEET_PATH']
        self.saveUserPath = SETTINGS['SAVE_USER_PATH']
        mkdirs(self.saveTweetPath) # ensure the path exists
        mkdirs(self.saveUserPath)


    def process_item(self, item, spider):
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip tweet:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update tweet:%s"%item['id_'])
            else:
                self.save_to_file(item,savePath)
                logger.debug("Add tweet:%s" %item['id_'])

        elif isinstance(item, User):
            savePath = os.path.join(self.saveUserPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip user:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update user:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add user:%s" %item['id_'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        ''' input: 
                item - a dict like object
                fname - where to save
        '''
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(dict(item), f, ensure_ascii=False)

class CsvTweetPipline(object):
    def __init__(self):
        self.saveTweetPath = SETTINGS['SAVE_CSV_TWEET_PATH']
        mkdirs(self.saveTweetPath)  # ensure the path exists
        nt=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.file = open(self.saveTweetPath+nt+"_tweet.csv", 'wb')
        self.tweet_exporter = CsvItemExporter(self.file)
        self.tweet_exporter.start_exporting()

    def close_spider(self,spider):
        self.tweet_exporter.finish_exporting()
        self.file.close()

    def process_item(self,item,spider):
        if isinstance(item,Tweet):
            self.tweet_exporter.export_item(item)
        return item

class CsvUserPipeline(object):

    def __init__(self):
        self.saveUserPath = SETTINGS['SAVE_CSV_USER_PATH']
        mkdirs(self.saveUserPath)
        nt=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.file = open(self.saveUserPath+nt+"_user.csv",'wb')
        self.user_exporter = CsvItemExporter(self.file)
        self.user_exporter.start_exporting()

    def close_spider(self,spider):
        self.user_exporter.finish_exporting()
        self.file.close()

    def process_item(self,item,spider):
        if isinstance(item,User):
            self.user_exporter.export_item(item)
        return item

