# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import re

driver=webdriver.Chrome()


driver.get('https://www.zhihu.com/')
# listCookies='UBI=fi_PncwhpxZ%7ETaO3mtFAQOp493ddHo%7EMwSlkfCcjQHXTNpc1k6U7sisSpDGJtz3Sqagcmo3R4ULrPubyp6BNoKgcikb4kmWh4n4%7Ezn4czsUL4faGlQwLnEVK6lB9VyD8PAI0-WUz614sacPfyZ9rhyrRBFCwA__; PASSID=Y2BJl5; BDUSS=lJBa3BXTy1WeTd6enc3QmdOfi16WHpBNko0Q0hQU0F6SXZCOVpweG9OQXQ2aHBhSVFBQUFBJCQAAAAAAAAAAAEAAAA1yJPJwtLK1bfRs7-yyQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC1d81ktXfNZT; SAVEUSERID=b9da581fb121d3763b62a576e5af06f6aa2339; PTOKEN=436ae6befe1ef825e920168a93b9ff6b; STOKEN=d978ae936e16b65b9e594a4059d0b9c6c1f06e67bce3f7126249f5d6a26cc855; HOSUPPORT=1; BAIDUID=3FFA0155DDEA27A1C8E45802BB11FA48:FG=1603778752'

listCookies='_xsrf=f7vHnCByyZonF2oXF3K9adgExYUsDois; _zap=fde57b60-240a-4be0-8e3a-e35bb9e09aba; d_c0="AGBmzrZ3RRCPTvKWXTaPc-DdVvKVHIn-Zpw=|1572319800"; _ga=GA1.2.1007914308.1584338380; tshl=; __utma=155987696.1007914308.1584338380.1599467756.1599467756.1; __utmz=155987696.1599467756.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tst=h; z_c0="2|1:0|10:1601199591|4:z_c0|92:Mi4xeW1jbURRQUFBQUFBWUdiT3RuZEZFQ1lBQUFCZ0FsVk41NnRkWUFEa29vMkNYVVJzYkpyalJsZHJweHRVUGw1dzFR|a9faa688b5b03d7c7b74086d0da9b883c4e980f79fee36b692e547b7d9a0c5ee"; q_c1=672eb59fa6ca4ed09abe5206ccf2ed24|1602832148000|1585114922000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1603412660,1603423018,1604048301,1604282294; SESSIONID=JT5XzMUvuMFDbMDNJsN2ar3JyifJdHS7t7NH735JgGu; JOID=UloWCk65ZTAK4sA9RLBSLEBNZPFW8TAPXp2PaTjJKndEjIh7CwUJqVzlwzZCrGgmpyFlYHMPkKYIBIOVSZXRL1U=; osd=U1kSBU64ZjQF4sE-QL9SLUNJa_FX8jQAXpyMbTfJK3RAg4h6CAEGqV3mxzlCrWsiqCFkY3cAkKcLAIyVSJbVIFU=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604284322; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1604285641|1604282293'
lists=re.findall('([\S*?]*?)=([\S*?]*?);',listCookies)

# print(lists)
for  l in lists:
    ck={'name':l[0],'value':l[1]}
    print(ck)
    driver.add_cookie(ck)           #来个正则把cookie字符串转成slenium的cookie格式字典，添加到driver。cookie字符串是请求贴吧时用f12查看的 network的headers的请求头的cookie，复制就可以了，这样selenium也可以免登陆
driver.get('https://www.zhihu.com/hot')
time.sleep(5)
driver.find_element_by_xpath('//div[@class="GlobalWrite-navTop"]/div[2]').click()
