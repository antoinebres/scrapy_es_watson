Let's create a new file named _figaro_spider.py_ inside the _crawler/crawler/spiders_ directory. This will be our spider.  
Copy/paste the following:

    import scrapy
    class figaroSpider(scrapy.Spider):
        name = "figaro"
        start_urls = [
            'http://www.lefigaro.fr/conjoncture/2017/08/15/20002-20170815ARTFIG00159-le-royaume-uni-va-proposer-un-brexit-en-douceur.php'
        ]

        def parse(self, response):
            pass

Then complete the parse fonction and make it return a dict with the informations we need.  
Run the following command to launch the crawl: _scrapy crawl figaro_
