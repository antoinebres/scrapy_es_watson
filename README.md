The goal of this formation is to familiarize you with scrapy.  
You will be building a simple agent that scrape a site, feed some parts to watson, and store the result into Elasticsearch.
You can find the documentation for scrapy at https://doc.scrapy.org/en/1.4/index.html

What you will need:
* [Anaconda](https://www.continuum.io/downloads) to manage the environment
* [Elasicsearch 5.5.1](https://www.elastic.co/downloads/past-releases/elasticsearch-5-5-1) to store the data
* [Kibana 5.5.1](https://www.elastic.co/downloads/past-releases/kibana-5-5-1) to visualize the data

I have created a branch for each step. The idea is to provide checkpoints.

* Step 1 - Use the scrapy shell to develop the core of the spider
* Step 2 - Implement a scrapy spider to scrape the page
* Step 3 - Implement a scrapy item to contain the data and Pipelines to process (Validation, Duplicates, Watson services) and to store it (Elasticsearch)
* Step 4 - Make your spider scrape multiple pages
* Step 5 - Ideas to go further (Aggregation, Item loaders for robustness, links navigation) and Visualization with Kibana
