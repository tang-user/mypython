# -*- coding: utf-8 -*-
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.select import Select


# 搜狐文章状态检查
def check_souhu(name,paw):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver=webdriver.Chrome(options=option)
    print('打开浏览器，打开搜狐登录')
    url='https://mp.sohu.com/mpfe/v3/login'
    driver.get(url)
    # 点击出现登录框
    driver.find_element_by_xpath('//div[@class="button"]').click()
    time.sleep(3)
    # name='13518183030'
    # paw='jwtc4000282990'
    #自动填入登录用户名
    driver.find_element_by_xpath("//input[@type='text']").send_keys(name)
    #自动填入登录密码
    driver.find_element_by_xpath("//input[@type='password']").send_keys(paw)
    #自动点击登录
    driver.find_element_by_xpath("//div[@class='login-import']/button").click()
    time.sleep(3)
    # d=driver.find_element_by_xpath('//*[@class="status"]/span[1]')
    d=driver.find_elements_by_xpath('//div[@class="status"]/span[1]')
    n=0
    for dd in d:
        if dd.text == '未通过':
            print('没有通过正在重新发布')
            driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/ul/li[4]/div/div[1]/div[3]/div/span[1]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="content-all"]/div[4]/div/div/div[2]/div[7]/div/div[2]/div/ul/li[2]').click()
        elif dd.text=='审核中':
            print('文章正常审核中请耐心等待')
            time.sleep(3)
        else:
            print('文章通过')
            n=n+1
    
    driver.close()
    driver.quit()  
    return n 

# 创头条文章状态检查/html/body/section/div/div/div[2]/div[3]/span
def check_chuang():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    url='http://www.ctoutiao.com/corp.php?act=logon'
    driver=webdriver.Chrome(options=option)
    print('打开浏览器，打开登录')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="J_logonForm"]/p[1]/input').send_keys('13980926167')
    driver.find_element_by_xpath('//*[@id="J_logonForm"]/p[2]/input[2]').send_keys('Aa463459227/')
    driver.find_element_by_xpath('//*[@id="J_lbton"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/header/div/div[2]/a[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/section/ul/div[3]/div/li[1]/a').click()
    time.sleep(2)
    t=driver.find_elements_by_xpath('//div[@class="gaolist"][position()<6]/div[@class="there"]/span/a')
   
    for tt in t:
        if tt.text=='已审核':
            print('文章审核通过')
           
        else:
            print('文章正在{}中请等会再来'.format(tt.text))
    
    driver.close()
    driver.quit()



check_chuang()
