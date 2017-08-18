Scrapy spiders can return the extracted data as Python dicts. While convenient and familiar, Python dicts lack structure: it is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.

Let's create a [scrapy item](https://doc.scrapy.org/en/1.4/topics/items.html) in items.py. Item objects are simple containers used to collect the scraped data.
You need to create fields for each information:
* title
* kw
* author
* description
* text
* date_published

Since we want to upload it in Elasticsearch, we will add some more fields:
* hash_key
* origin
* date_crawled

We also need some field to store the data from the watson services:
* nlu_analysis
* tone_analysis

Now that our spider works, we will want to feed the informations scraped to the watson services and store the result in Elasticsearch.
For that part we will implement [pipelines](https://doc.scrapy.org/en/1.4/topics/item-pipeline.html). They receive an item and perform actions over it, also deciding if the item should continue or be dropped and no longer processed.

We will implement 4 pipelines:
* Validation
* Duplicates
* Watson
* Elasticsearch

Run _cd_crawler.bat_ and paste the following command to launch the crawl: _scrapy crawl figaro_
