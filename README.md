To go further, you can:  
* Customize settings (polite crawl, stealth considerations, log)
* Improve robustness by looking at the logs to detect problems
* Get the links of the next pages

Now that we have a fully working spider, we can see the result of the crawling using kibana.  
Import the visualizations in kibana to see the following 3 dashboards:
* Basic informations
* NLU
* Tone Analysis

Run _launch_env.bat_ to start elasticsearch, kibana and a cmd with the environment active. Then go to http://localhost:5601 and import the visualizations in kibana.
