## Items
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
* hash_key, this field will serve as an id, we will use the sha256 algorithm
* origin, this field has not much relevance rigth now since we only scrape 'lefigaro.fr', but it can be useful later to determine the quality of the source
* date_crawled, if we schedule the crawler to run daily on the articles of the day, we can use this field as the datetime field and not worry about any missing date

We also need some field to store the data from the watson services:
* nlu_analysis
* tone_analysis

## Pipelines
Now that our spider works, we will want to feed the informations scraped to the watson services and store the result in Elasticsearch.
For that part we will implement [pipelines](https://doc.scrapy.org/en/1.4/topics/item-pipeline.html). They receive an item and perform actions over it, also deciding if the item should continue or be dropped and no longer processed.

We will implement 4 pipelines:
* Validation, this pipeline discards items where there is no text
* Duplicates, this pipeline discards articles already crawled (during the current session)
* Watson, this pipeline is where we send the data to Watson services and process the result (cf API reference for [Tone analysis](https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/?python#api_explorer) and [NLU](https://www.ibm.com/watson/developercloud/natural-language-understanding/api/v1/))
* Elasticsearch, this pipeline index the item in elasticsearch

Run _cd_crawler.bat_ and paste the following command to launch the crawl:  
_scrapy crawl figaro_
