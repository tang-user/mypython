# -*- coding: utf-8 -*-
import os
from lxml import etree
from selenium import webdriver
import requests
import time 
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 百姓网发布
def baixing():
    dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\souhu'
    # imgs_path=r'C:\Users\Administrator\Desktop\生产' 
    driver=webdriver.Chrome()
    # 打开登录百姓网
    driver.get('https://www.baixing.com/oz/login')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/a').click()
    driver.find_element_by_name('identity').send_keys('13980926167')
    driver.find_element_by_name('password').send_keys('a463459227')
    driver.find_element_by_id('id_submit').click()
    time.sleep(3)
    # 切换地区
    driver.find_element_by_xpath('/html/body/header/div[1]/div/div/a').click()
    time.sleep(1)
    # 选择地区
    driver.find_element_by_xpath('//*[@id="m23"]/ul/li[1]/a').click()
    time.sleep(1)
    # 发布
    driver.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[3]/a[1]').click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="m23"]/ul/li[1]/a').click()
    #    选择服务
    driver.find_element_by_xpath('//*[@id="select"]/ul/li[8]/a').click()
    time.sleep(2)
    # 进一步选择服务 
    driver.find_element_by_xpath('//*[@id="fuwu"]/ul/li[4]/a[30]').click()
    time.sleep(3)
    # 文章
    file_name=get_file_name(dir_path)
    # 标题处理
    for f in file_name:
        title=f.replace('.txt','').strip()
        driver.find_element_by_name('title').send_keys(title)
        driver.find_element_by_xpath('//*[@id="id_fuwuAreas"]/div[1]/div/label[1]').click()
        # 内容读取
        with open(dir_path+'\\'+f,mode='r',encoding='utf-8') as r: 
            cs = r.readlines()
            # 内容填写
        # time.sleep(3)
            # driver.find_element_by_xpath('//*[@id="id_content"]/div/textarea').clear()        
        driver.find_element_by_xpath('//*[@id="id_content"]/div/textarea').send_keys(cs)            
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="bxForm"]/div[2]/div[6]/div[1]/span/select[1]').click()
        driver.find_element_by_xpath('//*[@id="bxForm"]/div[2]/div[6]/div[1]/span/select[1]/option[4]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="id_联系人"]/div[1]/input').clear()
        driver.find_element_by_xpath('//*[@id="id_联系人"]/div[1]/input').send_keys('佳味添成')
        driver.find_element_by_xpath('//*[@id="id_contact"]/div[1]/input').clear()
        driver.find_element_by_xpath('//*[@id="id_contact"]/div[1]/input').send_keys('028-81811106')
        time.sleep(1)
        driver.find_element_by_id('fabu-form-submit').click()
        # WebDriverWait(driver,10).until(
        #     EC.text_to_be_present_in_element((By.XPATH,'/html/body/div[2]/p[@class="title"]'),u'恭喜，您的信息发布成功！')       
        time.sleep(3)
        driver.get('https://chengdu.baixing.com/fabu/qitafuwu')   
        print('文章{}发布完了'.format(f))
        os.remove(dir_path+'\\'+f)                          
    time.sleep(2)
# 拿到文件名字函数
def get_file_name(dir_path): 
    # 获取传来文件夹下的所有文件名
    file_name=os.listdir(dir_path)
    # 判断文件夹是否为空
    if  not file_name:
        print('该文件夹为空,没有文件可传')
        return
    else:
        return file_name
# baixing()
# 百姓网文章抓取
def get_baixing():
    datas=[]
    url='https://www.baixing.com/u/92147482/?src=vad_listing_7'
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    res=requests.get(url,headers=headers)    
    html=etree.HTML(res.text)    
    title=html.xpath('//ul[@class="list-ad-items"]/li[position()<6]/div/div[1]/a/text()')
    baixing_url=html.xpath('//ul[@class="list-ad-items"]/li[position()<6]/div/div[1]/a/@href')
    for i in range(0,5):
        datas.append(baixing_url[i].replace('?from=',''))
        datas.append(title[i])
    return datas
# 知乎
def zhihu():
    datas=[]
    url='https://www.zhihu.com/people/ding-ni-ge-fei-68-18/posts'
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    res=requests.get(url,headers=headers)
    html=res.text
    url_list=re.search('<script id="js-initialData" type="text/json">(.*?)</script>',html)[0]
    # title=html.xpath('//h2[@class="ContentItem-title"][position()<6]/a/text()')
    urls=re.findall('"author".*?},"url":"(.*?)","commentPermission"',url_list)
    title_list=re.findall('"linkbox":{.*?},"title":"(.*?)","voting',url_list)

    # print(t[0].encode('utf8').decode('unicode_escape'))
    for i in range(5,10):
        datas.append(urls[i].encode('utf8').decode('unicode_escape'))
        datas.append(title_list[i])
    return datas   
# datas=zhihu()
# print(datas)