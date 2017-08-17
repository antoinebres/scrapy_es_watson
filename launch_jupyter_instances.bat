call activate scrapy_es_watson
set /P n=
for /l %%v in (1, 1, %n%) do start cmd /k jupyter notebook --ip 192.168.73.211