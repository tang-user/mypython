from selenium import webdriver
from selenium.webdriver.support.select import Select
import time 
#用webdriver启动谷歌浏览器
def write_web():
    title = "Python发表文章测试55"
    content = "XPath即为XML路径语言，它是一种用来确定XML（标准通用标记语言的子集）文档中某部分位置的语言。XPath基于XML的树状结构，有不同类型的节点，包括元素节点，属性节点和文本节"
    # content2 = "这是"
    driver.find_element_by_name('title').send_keys(title)
    
    sel = driver.find_element_by_xpath("./*//select[@id='typeid']")
    Select(sel).select_by_value('3')
    # driver.find_element_by_link_text('新闻资讯')
    driver.find_element_by_xpath("//*[@id='cke_body']").send_keys(content)
    
    
    # driver.find_element_by_xpath("./*//input[@name='imageField']").click()
    time.sleep(5)
    # driver.find_element_by_link_text("继续发布文章").click()
    # title2 = "Python发表文章测试2"
    # content2 = "XPath即为XML路径语言，它是一种用来确定XML（标准通用标记语言的子集）文档中某部分位置的语言。XPath基于XML的树状结构，有不同类型的节点，包括元素节点，属性节点和文本节"
    # driver.find_element_by_xpath("//input[@name='title']").send_keys(title2)
    # sel = driver.find_element_by_xpath("./*//select[@id='typeid']")
    # Select(sel).select_by_value('1')
    # driver.find_element_by_xpath("//*[@id='cke_body']").send_keys(content2)
    # driver.find_element_by_xpath("./*//input[@name='imageField']").click()
    # print("发布文章成功")

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
write_web()

