import re
import scrapy
from w3lib.html import remove_tags, remove_tags_with_content


class figaroSpider(scrapy.Spider):
    name = "figaro"
    start_urls = [
        'http://www.lefigaro.fr/conjoncture/2017/08/15/20002-20170815ARTFIG00159-le-royaume-uni-va-proposer-un-brexit-en-douceur.php'
    ]

    def parse(self, response):
        # Parsing the content
        article = {}
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

        yield article
