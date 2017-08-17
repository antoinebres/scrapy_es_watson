The goal of this formation is to familiarize you with scrapy, watson NLU and Sentiment analysis APIs, and Elasticsearch.
You will be building a simple agent that scrape a site, feed some parts to watson, and store the result into Elasticsearch.

Setting up the environment: Use the following command 'conda env create -f environment.yml'
    
Steps:
    Scrapy shell to develop the core of the spider
    
    Scrapy spider to scrape the page 
    Item
    
    Pipelines (Duplicates, Watson services, Elasticsearch)
    
    Add Start urls
    
    Links navigation
    
    Settings (polite crawl, stealth, log)

    Viz Kibana
        Basic informations  http://localhost:5601/goto/4f2e13476174889345d299735f1c2560
        NLU                 http://localhost:5601/goto/874ba5f6e803e0b23511a7193ee87356
        Tone Analysis       http://localhost:5601/goto/6072ddffa0d1c3224c1fb89afa14c649
    To go further (Aggregation, robustness log items loader, links navigation)