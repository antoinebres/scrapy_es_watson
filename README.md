
The goal of this formation is to familiarize you with scrapy.  
You will be building a simple agent that scrape a site, feed some parts to watson, and store the result into Elasticsearch.

What you need:
* [Anaconda](https://www.continuum.io/downloads)
* [Elasicsearch 5.5.1](https://www.elastic.co/downloads/past-releases/elasticsearch-5-5-1)
* [Kibana 5.5.1](https://www.elastic.co/downloads/past-releases/kibana-5-5-1)

Setting up the environment: run _setup/setup_env.bat_  
I have created a branch for each step. The idea is to provide checkpoints.

* Step 1 - Use the scrapy shell to develop the core of the spider
* Step 2 - Implement a scrapy spider to scrape the page
* Step 3 - Implement a scrapy item to contain the data and Pipelines to process (Validation, Duplicates, Watson services) and to store it (Elasticsearch)
* Step 4 - Make your spider scrape multiple pages
* Step 5 - Ideas to go further (Aggregation, Item loaders for robustness, links navigation) and Visualization with Kibana
    * Basic informations  http://localhost:5601/goto/4f2e13476174889345d299735f1c2560
    * NLU                 http://localhost:5601/goto/874ba5f6e803e0b23511a7193ee87356
    * Tone Analysis       http://localhost:5601/goto/6072ddffa0d1c3224c1fb89afa14c649
