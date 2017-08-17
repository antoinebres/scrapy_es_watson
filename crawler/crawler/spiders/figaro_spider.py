import re
import datetime
import hashlib
from w3lib.html import remove_tags, remove_tags_with_content
import scrapy
from crawler.items import Article
from scrapy.linkextractors import LinkExtractor


class figaroSpider(scrapy.Spider):
    name = "figaro"
    articles_scraped = []
    start_urls = [
        'http://www.lefigaro.fr/economie/'
    ]
    # start_urls = [
    #     'http://www.lefigaro.fr/conjoncture/2017/08/15/20002-20170815ARTFIG00159-le-royaume-uni-va-proposer-un-brexit-en-douceur.php',
    #     'http://www.lefigaro.fr/conjoncture/2017/08/14/20002-20170814ARTFIG00055-alena-le-bras-de-fer-commence-entre-les-etats-unis-le-mexique-et-le-canada.php',
    #     'http://www.lefigaro.fr/conjoncture/2017/08/14/20002-20170814ARTFIG00206-charlottesville-le-pdg-de-merck-lache-trump-avec-fracas.php',
    #     'http://www.lefigaro.fr/conjoncture/2017/08/09/20002-20170809ARTFIG00240-comment-bercy-veut-combattre-l-optimisation-fiscale-des-geants-du-numerique.php',
    # ]
    # Back-up
    # start_urls = [
    #     './src/html/figaro_eco_0.html',
    #     './src/html/figaro_eco_1.html',
    #     './src/html/figaro_eco_2.html',
    #     './src/html/figaro_eco_3.html',
    # ]

    def parse(self, response):
        # Get links
        links = list(set(response.css('a::attr("href")').re(r'http:\/\/www\.lefigaro\.fr\/.*?\/\d+\/\d+\/\d+\/.*\.php')))
        for link in links:
            if link is not None:
                yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        article = Article()
        # Parsing the content
        # URL domain
        article['origin'] = response.url.split("/")[2] or 'www.lefigaro.fr'  # if back-up urls used
        # Date
        article['date_published'] = response.css('time[itemprop="datePublished"]::attr("datetime")').extract_first()
        # Title
        article['title'] = response.css('title::text').extract_first()
        # Keywords
        article['kw'] = response.css('meta[name="keywords"]::attr("content")').extract_first().split(",")
        # Author
        article['author'] = response.css('meta[name="author"]::attr("content")').extract_first()
        # Description
        article['description'] = response.css('meta[name="description"]::attr("content")').extract_first()
        # The actual article
        text = response.css('div.fig-main-col').extract()  # html tag to be cleaned
        text = ''.join(text)
        text = re.sub('\s\s+', ' ', text)
        text = remove_tags_with_content(text, ('style', 'script'))  # remove irrelevent content
        text = remove_tags(text)  # remove html tags
        article['text'] = text
        # Creating metadata
        # An id
        article['hash_key'] = hashlib.sha256(bytes(text, 'utf-8')).hexdigest()
        # the date of the crawl
        article['date_crawled'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
        yield article
        # Recursive call to get next links
        # self.parse(response)
