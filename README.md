To get started: 
* run _setup/setup_env.bat_
* make a directory named _src_ at the root

        src/

            elasticsearch/      # elasticsearch directory

            kibana/             # kibana directory


When the environment is set, run _launch_scrapy_shell.bat_

Use [selectors](https://doc.scrapy.org/en/1.4/topics/selectors.html) inside the scrapy shell to target the informations. The shell is very usefull when writing or debugging a spider. We need to scrape the following:
* The title of the article
* The keywords of the article
* The author of the article
* The description of the article
* The text of the article
* The publication date of the article

Once you know the selectors to get these information, use the following command to make a scrapy project:  
_scrapy startproject crawler_
