Scrapy spiders can return the extracted data as Python dicts. While convenient and familiar, Python dicts lack structure: it is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.

Let's create a Scrapy item in items.py. Item objects are simple containers used to collect the scraped data.
You need to create fields for each information:
    title
    kw
    author
    description
    text
    date_published

Since we want to upload it in Elasticsearch, we will add some more fields:
    hash_key
    origin
    date_crawled

We also need some field to store the data from the watson services:
    nlu_analysis
    tone_analysis

Next, the pipelines