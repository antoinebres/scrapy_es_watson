@echo off
if "%1" == "" GOTO start
if "%1" == "scrapy" GOTO scrapy
:start
    start cmd /k cd_crawler scrapy
    GOTO end
:scrapy
    call activate scrapy_es_watson
    cd crawler
    GOTO end
:end
