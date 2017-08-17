import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    kw = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    text = scrapy.Field()
    nlu_analysis = scrapy.Field()
    tone_analysis = scrapy.Field()
    hash_key = scrapy.Field()
    origin = scrapy.Field()
    date_crawled = scrapy.Field()
    date_published = scrapy.Field()
