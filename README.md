## Crawl
We can scrape data, get watson's inputs, and store the whole thing into elasticsearch but as of now we only scrape one page.  
Let's scale our crawler.  

First we can add pages in the start_urls array.
Let's add these:
* http://www.lefigaro.fr/conjoncture/2017/08/14/20002-20170814ARTFIG00055-alena-le-bras-de-fer-commence-entre-les-etats-unis-le-mexique-et-le-canada.php
* http://www.lefigaro.fr/conjoncture/2017/08/14/20002-20170814ARTFIG00206-charlottesville-le-pdg-de-merck-lache-trump-avec-fracas.php
* http://www.lefigaro.fr/conjoncture/2017/08/09/20002-20170809ARTFIG00240-comment-bercy-veut-combattre-l-optimisation-fiscale-des-geants-du-numerique.php

With this approach, you would have to list every pages you want to scrape data from. That's fine if you want to get informations on very specific pages, but not very pratical otherwise.

In order for our spider to actually crawl sites, we need to retrieves some links.  
Let's start at the main page http://www.lefigaro.fr/economie/ and try to capture the links corresponding to the articles. 
We will then follow those links, parse these pages and scrape them.
