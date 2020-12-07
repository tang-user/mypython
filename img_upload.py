import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time 
driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
print("启动浏览器，打开dede登录界面")
driver.get("http://www.drinksaaa.com/jwtcaaa028/article_add.php")
author = "admin"
passowrd = "jwtcaaa028"
#自动填入登录用户名
driver.find_element_by_xpath("//input[@name='userid']").send_keys(author)
#自动填入登录密码
driver.find_element_by_xpath("./*//input[@name='pwd']").send_keys(passowrd)
#自动点击登录按钮进行登录
driver.find_element_by_xpath("./*//button[@type='submit']").click()
print("登陆成功")
# 休息5秒
time.sleep(5)
# 下面这个可以放在一个函数

# 找到图片上传框
# driver.find_element_by_name('title').send_keys('title')
driver.find_element_by_xpath('//*[@id="cke_27"]').click()
time.sleep(3)
# 找到上传按钮
driver.find_element_by_xpath('//*[@id="cke_Upload_143"]').click()
time.sleep(3)
# 上传图片
patha=r'C:\Users\Administrator\Desktop\生产\1.png'
iframe=driver.find_element_by_id("cke_138_fileInput")
driver.switch_to_frame(iframe)
driver.find_element_by_xpath("//input[@name='upload']").send_keys(patha)
driver.switch_to.default_content()
time.sleep(3)
# 确定上传图片到服务器
driver.find_element_by_xpath('//*[@id="cke_141_uiElement"]').click()
time.sleep(3)
# 图片插入文章
# driver.find_element_by_xpath('//*[@id="cke_173_uiElement"]').click()
# 上传图片的地址
imgs=driver.find_element_by_id('cke_87_textInput').get_attribute('value')
time.sleep(3)
# 点击取消上传图片
driver.find_element_by_id('cke_174_label').click()

