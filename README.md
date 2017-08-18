## The spider
Let's create a new file named _figaro_spider.py_ inside the _crawler/crawler/spiders_ directory. This will be our [spider](https://doc.scrapy.org/en/1.4/topics/spiders.html).  
Copy/paste the following:

    import scrapy
    class figaroSpider(scrapy.Spider):
        name = "figaro"
        start_urls = [
            'http://www.lefigaro.fr/conjoncture/2017/08/15/20002-20170815ARTFIG00159-le-royaume-uni-va-proposer-un-brexit-en-douceur.php'
        ]

        def parse(self, response):
            pass

Then complete the parse fonction with the selectors of step 1 and make it return a dict with the informations we need.  
Run _cd_crawler.bat_ and paste the following command to launch the crawl:  
_scrapy crawl figaro_
