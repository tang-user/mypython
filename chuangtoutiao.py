# -*- coding: utf-8 -*-
from lxml import etree
import requests
import  xlsxwriter


def chuangtout(url):
    datas=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    html=etree.HTML(res.text)   
    
    urls=html.xpath('//h2/a/@href')    
    title=html.xpath('//h2/a/text()')
    for i in range(0,5):    
        datas.append("http://www.ctoutiao.com"+urls[i].replace('\\','').replace('"',''))
        n=title[i].replace(r'\r\n','').encode('utf-8').decode('unicode_escape').strip()
        datas.append(n)
    return datas
          


datas=chuangtout("http://www.ctoutiao.com/ajax_new/ajax_data.php?page=newCompany&act=getPosts&uid=1729092&type=getPosts&pageno=1")
n=10
for i in range(0,10,2):
    print(datas[i])
    print(datas[i-1])  
    n=n+1
# print(datas)