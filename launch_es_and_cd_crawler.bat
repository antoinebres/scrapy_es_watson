@echo off
if "%1" == "" GOTO start
if "%1" == "elasticsearch" GOTO elasticsearch
if "%1" == "scrapy" GOTO scrapy
:start
    start cmd /k launch_es_and_cd_crawler scrapy
    start cmd /k launch_es_and_cd_crawler elasticsearch
    GOTO end
:elasticsearch
    src/elasticsearch/bin/elasticsearch
    GOTO end
:scrapy
    call activate scrapy_es_watson
    cd crawler
    GOTO end
:end
