
# -*- coding: utf-8 -*-
from lxml import etree
import requests
import  xlsxwriter
import datetime
import os

def souhu(url):
    dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\boke'
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    datas=[]
    # 第一个
    res=requests.get(url,headers=headers)
    html=etree.HTML(res.text)
    # title=html.xpath('//ul/li[position()<6]/article/div/h4/a/text()')
    urls=html.xpath('//ul/li[position()<5]/article/div/h4/a/@href')
    
    for i in urls:        
        res1=requests.get('https:'+i,headers=headers)
        html=etree.HTML(res1.text)
        # 标题
        title=html.xpath('//div[@class="text-title"]/h1/text()')[0]
        title=title.strip()
        # 内容
        info=html.xpath('//article[@class="article"]/p[position()>1]/text()')
        if os.path.exists(dir_path+'\\'+title+'.txt'):
            print('有重复的内容，删掉再重新写入')
            os.remove(dir_path+'\\'+title+'.txt')
        for c in range(0,len(info)):            
            with open(dir_path+'\\'+title+'.txt',mode='a',encoding='utf-8') as f:
                f.write(info[c]+'\r\n')
        # 图片
        img_url=html.xpath('//article[@class="article"]/p/img/@src')[0]
        if 'http:' not in img_url:
            img_url='http:'+img_url
        datas.append(img_url)

    return datas
        # print(i)
d=souhu("https://mp.sohu.com/profile?xpt=Y2hvdWZlaTkwN0Bzb2h1LmNvbQ==&_f=index_pagemp_2&spm=smpc.content.author.3.1600062058180TWhMOU2")
# for i in data:
#     print(i)
print(d)