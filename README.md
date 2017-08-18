To get started: 
* run _setup/setup_env.bat_
* make a directory named _src_ at the root

    src/

        elasticsearch/      # elasticsearch directory
        
        kibana/             # kibana directory


When the environment is set, run _launch_scrapy_shell.bat_

Use the scrapy shell to develop the core of the spider. We need to scrape the following:
* The title of the article
* The keywords of the article
* The author of the article
* The description of the article
* The text of the article
* The publication date of the article

Once you know the selector to get these information, use the following command to make a scrapy project: _scrapy startproject crawler_
