# -*- coding: utf-8 -*-
from lxml import etree
import requests
import  xlsxwriter
import datetime

def boke(url):
    datas=[]
    res=requests.get(url)
    html=etree.HTML(res.text)
    # title=html.xpath('//div[@class="articleList"]/div[position()<6]/p/span/a/text()')
    urls=html.xpath('//div[@class="articleList"]/div[position()<6]/p/span/a/@href')

    # print(titles)
    for i in range(0,5):
        
        res=requests.get(urls[i])
        html=etree.HTML(res.text)        
        titles=html.xpath('//div/h2/text()')
        datas.append(urls[i])
        # datas.append(titles[0])
        
    return datas
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
            }
# datas=boke("http://blog.sina.com.cn/s/articlelist_5226711056_0_1.html")
res=requests.get('http://blog.sina.com.cn/s/blog_1378948100102yed9.html',headers=headers)
html=etree.HTML(res.text)  
print(res.text)      
titles=html.xpath('//h2/text')
print(titles)


