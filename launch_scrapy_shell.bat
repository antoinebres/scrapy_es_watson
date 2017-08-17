@echo off
if "%1" == "" GOTO start
if "%1" == "scrapy" GOTO scrapy
:start
    start cmd /k launch_env scrapy
    GOTO end
:scrapy
    call activate scrapy_es_watson
    scrapy shell "http://www.lefigaro.fr/conjoncture/2017/08/15/20002-20170815ARTFIG00159-le-royaume-uni-va-proposer-un-brexit-en-douceur.php"
    GOTO end
:end