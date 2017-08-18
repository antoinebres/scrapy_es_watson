import re
import datetime
import hashlib
import scrapy
from w3lib.html import remove_tags, remove_tags_with_content
from crawler.items import Article


class figaroSpider(scrapy.Spider):
    name = "figaro"
    start_urls = [
        'http://www.lefigaro.fr/economie/'
    ]

    def parse(self, response):
        # Get links
        links = list(set(response.css('a::attr("href")').re(r'http:\/\/www\.lefigaro\.fr\/.*?\/\d+\/\d+\/\d+\/.*\.php')))
        for link in links:
            if link is not None:
                yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        article = Article()
        # Parsing the content
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
        article['text'] = remove_tags(text)  # remove html tags
        # Date
        article['date_published'] = response.css('time[itemprop="datePublished"]::attr("datetime")').extract_first()
        # Creating metadata
        # URL domain
        article['origin'] = response.url.split("/")[2]
        # An id
        article['hash_key'] = hashlib.sha256(bytes(text, 'utf-8')).hexdigest()
        # the date of the crawl
        article['date_crawled'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
        yield article
