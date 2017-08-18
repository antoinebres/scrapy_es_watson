The goal of this formation is to familiarize you with scrapy, watson NLU and Sentiment analysis APIs, and Elasticsearch.  
You will be building a simple agent that scrape a site, feed some parts to watson, and store the result into Elasticsearch.

Setting up the environment: 
* run setup/setup_env.bat
* download and put the src directory at the root

When the environment is set, run launch_es_and_scrapy_shell.bat

Use Scrapy shell to develop the core of the spider. We need to scrape the following:
* The title of the article
* The keywords of the article
* The author of the article
* The description of the article
* The text of the article
* The publication date of the article

Once you know the selector to get these information, use the following command to make a scrapy project: scrapy startproject crawler
