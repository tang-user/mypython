# -*- coding: utf-8 -*-
import requests
import json
import re
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time 

def main():
    driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    print("启动浏览器，打开dede登录界面")
    driver.get('http://www.818u.com/basedo/poste.aspx?classid=104&citydm=beijing')
    driver.find_element_by_id("titles").send_keys('author')
    driver.find_element_by_id('neirong').send_keys('写入的内容')

def get_818(url):
    datas=[]
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
   
    # s = requests.session() #建立一个Session
    form_data = {   
        '__VIEWSTATE': '/wEPDwUKLTk4NDU4OTMzMWRk2n6a8smWQwShiX7p3Dw0lcMKWtXllwxr+A6O7EuLWfE=',
        '__VIEWSTATEGENERATOR': 'D399C246',
        'username': 'a463459227',    
        'userpassword':'463459227',
        'Button1': '登录',
    }

    session = requests.session()
    response = session.post(url,headers=headers,data=form_data) #session登录网站
    url="http://www.818u.com/members/infolist.aspx?uid=447889"
    response = session.get(url,headers=headers) #session浏览页面
    html=etree.HTML(response.text)
    title=html.xpath('//tr[position()<7]/td/a[@class="f0"]/text()')
    urls=html.xpath('//tr[position()<7]/td/a[@class="f0"]/@href')
    for i in range(0,5):
        datas.append('http://www.818u.com'+urls[i])
        datas.append(title[i])
    return datas

datas=get_818('http://www.818u.com/members/login.aspx')
for i in range(0,10,2):
    print(datas[i])
    print(datas[i+1])
