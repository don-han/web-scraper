from utils.pipelines import AbstractMySQLPipeline
from labs.items import LinkItem, TextItem, PaperItem

class MySQLPipeline(AbstractMySQLPipeline):

    def process_item(self, item, spider):
        pass
        # if isinstance(item, LinkItem):
        #     Link(
        #         url=item.url,
        #
        # elif isinstance(item, TextItem):
        #
        # else:
        #     raise DropItem("Dropping item: {0}".format(item))


class MongoDBPipeline(AbstractMongoDBPipeline):
    """Pipeline for saving to a MongoDB database"""

    def __init__(self):
        from pymongo import MongoClient
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.external_link_collection = db[settings['MONGODB_EXTERNAL_LINK_COLLECTION']]
        self.internal_link_collection = db[settings['MONGODB_INTERNAL_LINK_COLLECTION']]
        self.text_collection = db[settings['MONGODB_TEXT_COLLECTION']]
        # self.paper_collection = db[settings['MONGODB_PAPER_COLLECTION']]

    def process_item(self, item, spider):
        if isinstance(item, ExternalLinkItem):
            self.external_link_collection.insert_one(dict(item))
            return item
        elif isinstance(item, InternalLinkItem):
            self.internal_link_collection.insert_one(dict(item))
            return item
        elif isinstance(item, TextItem):
            self.text_collection.insert_one(dict(item))
            return item
        elif isinstance(item, PaperItem):
            pass
            #self.paper_collection.insert_one(dict(item))
            #return item
        else:
            raise DropItem("Dropping item: {0}".format(item))
