import requests
from lxml import etree
from http import cookiejar
import json
import time
from selenium import webdriver
url='https://www.zhihu.com/signin?next=%2F'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
         }

form_data = {   
           '_xsrf': 'f7vHnCByyZonF2oXF3K9adgExYUsDois',
        'password': '46345927',
        "captcha_type": 'cn',
         'email': '顶你个肥',
    }
session = requests.session()

# url='https://zhuanlan.zhihu.com/write'
session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
response = session.post(url,headers=headers,data=form_data) #session登录网站
# html2=response.json()
# url2='https://www.zhihu.com/hot'
# res = session.get(url2,headers=headers)
# h=json.loads(res.text)
# h=res.json()
# html=etree.HTML(h)

# t=html.xpath('//*/a/text()')
# for data in h['data']:
#     print(data['question']['title']) 
# 热榜
url_hot='https://www.zhihu.com/hot'  
res = session.get(url_hot,headers=headers)
html=etree.HTML(res.text)
title=html.xpath('//section[@class="HotItem"]/div[@class="HotItem-content"]/a/h2/text()')
for t in title:
    print(t)
# driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')

# print("启动浏览器，打开界面")
# driver.get(url)
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/label/input').send_keys('顶你个肥')
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[3]/div/label/input').send_keys('46345927')
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button').click()
# time.sleep(100)