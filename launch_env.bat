@echo off
if "%1" == "" GOTO start
if "%1" == "elasticsearch" GOTO elasticsearch
if "%1" == "kibana" GOTO kibana
if "%1" == "scrapy" GOTO scrapy
:start
    start cmd /k launch_env scrapy
    start cmd /k launch_env elasticsearch
    start cmd /k launch_env kibana
    GOTO end
:elasticsearch
    src/elasticsearch/bin/elasticsearch
    GOTO end
:kibana
    src/kibana/bin/kibana
    GOTO end
:scrapy
    call activate scrapy_es_watson
    cd crawler
    rem scrapy shell ./src/html/figaro_eco_0.html
    GOTO end
:end