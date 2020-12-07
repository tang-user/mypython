
# -*- coding: utf-8 -*-
from lxml import etree
import requests
import xlrd
from xlutils.copy import copy
def drinks888(url):
    datas=[]    
    res=requests.get(url)
    html=etree.HTML(res.text)
    res2=requests.get("http://www.drinks888.com/news/53/2.html")
    html2=etree.HTML(res2.text)
    url=url.split('/news')
    title=html.xpath('//div[@class="news_main2"]/dl[position()>1]/dd/h3/a/text()')
    urls=html.xpath('//div[@class="news_main2"]/dl[position()>1]/dd/h3/a/@href')
        # 第二页的两条
    title2=html2.xpath('//div[@class="news_main2"]/dl/dd/h3/a/text()')
    urls2=html.xpath('//div[@class="news_main2"]/dl/dd/h3/a/@href')
    for i in range(0,2):
        
        datas.append(url[0]+urls2[i])
        datas.append(title2[i])
    
    # print(url_s[0])
    for i in range(0,3):
        datas.append(url[0]+urls[i])
        datas.append(title[i])
    return datas
# 打开文件函数得到总行数
# def open_excel():
#     # 打开文件
#     workbook = xlrd.Workbook('C:/Users/Administrator/Desktop/唐富/唐富/5月工作表/各类长尾词统计.xlsx')
#     # 获取第一个sheet的总行数
#     sheet_rows = workbook.sheet_by_index(0).nrows
#     return sheet_rows
# 写入excel文件的尾部函数

 
excel_book=xlrd.open_workbook('C:/Users/Administrator/Desktop/唐富/唐富/5月工作表/各类长尾词统计.xlsx') 
sheet_rows = excel_book.sheet_by_index(0).nrows
copy_excel=copy(excel_book)
sheet1=copy_excel.get_sheet(0)
datas=drinks888('http://www.drinks888.com/news/53/1.html')
n=sheet_rows+1
for i in range(0,10,2):
    sheet1.write(n,3,datas[i]) #修改(1,0)单元格数据为小李
    sheet1.write(n,4,datas[i-1])
    n=n+1

# 保存修改过后的文件
copy_excel.save('C:/Users/Administrator/Desktop/唐富/唐富/5月工作表/各类长尾词统计1.xlsx')
   




# d=drinks888("http://www.drinks888.com/news/53/1.html")
# # 网站888文章
# print('网站888文章开始')
# datas=drinks888("http://www.drinks888.com/news/53/1.html")
# print(datas)
# n=5
# for i in range(0,10,2):
#     # worksheet.write(n,1,datas[i])
#     # worksheet.write(n,2,datas[i-1])
#     n=n+1
# workbook.close()
