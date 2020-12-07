import requests
import xlsxwriter
from lxml import etree  # 导入lxml解析html的模块
from bs4 import BeautifulSoup
class spaider():
    #获取总页码
    def get_all(self,b):              
        url='http://www.drinks888.com/news/53/{}.html'.format(b) #输入指定页码
        res=requests.get(url).text
        html = etree.HTML(res)
        title_text = html.xpath('/html/body/div[6]/div[2]/div[3]/a[4]/text()')  
        totcount=int(title_text[0])  #得到总页码
        return totcount        
    #每个列表页内容
    def get_content(self,a):
        #存放每页的内容        
        url='http://www.drinks888.com/news/53/{}.html'.format(a)
        res_c=requests.get(url).text
        soup = BeautifulSoup(res_c, "html.parser")
        a=soup.find('div','news_main2')
        aa=a.find_all('a')
        html_c=etree.HTML(res_c)        
        for i in range(1,5):               
            title_t=html_c.xpath('/html/body/div[6]/div[2]/div[2]/dl[{}]/dd/h3/a/text()'.format(i)) 
            #con=html_c.xpath('/html/body/div[6]/div[2]/div[2]/dl[{}]/dd/p/text()'.format(i))
            for i in aa:
                if not i.get_text('h3') or  i.get_text('span')=='了解详情 +':
                    continue
                if i.get_text('h3')==title_t[0]:
                    url_2='www.drinks888.com'+i.get('href')
                    self.content(url_2)
                
            if not title_t:
                break  
            '''worksheet.write(n , 0,title_t[0])
            worksheet.write(n , 1,con[0])
            worksheet.write(n , 2,url_2)'''
            
    def get_ccc(self,count):#得到每个列表页内容
        n=1
        for i in range(1,count):
            dd.get_content(i) 
            n+=1 
    #内页内容
    def content(self,url_2):
        con_res=requests.get(url_2).text
        soup = BeautifulSoup(con_res, "html.parser")
        a=soup.find('div','fuwu_wenz')
        with open( soup.h2.text+'.txt','w',encoding='utf-8') as o:
            o.write(str(a)+'/n')


