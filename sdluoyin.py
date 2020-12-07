from bs4 import BeautifulSoup
import requests
class spaider():
   def get_list(self,p):#得到列表页
      p=str(p)
      
      list_url="http://www.sdluoyin.com/news/p{}.html".format(p)
      list_res=requests.get(list_url).text
      list_soup=BeautifulSoup(list_res,'html.parser')
      a_list=list_soup.find('ul','news_list').find_all('a')
      
      for i in a_list: 
                            
        self.content(i)
        with open('文章链接.txt','a',encoding='utf-8') as o:
          
         o.write(i['href']+'\n')
      
   def content(self,url):  
          
      aa=r'\/\:*？?"<>l'      
      con_res=requests.get(url['href']).text      
      soup = BeautifulSoup(con_res, "html.parser")
      ab=soup.find('div','content').find_all('p')
      title=soup.find('h1').text    
              
      for i in title:
         if i in aa:
            title=title.replace(i,'')
      for i in ab:
         i=str(i)
         with open(title+'.txt','a',encoding='utf-8') as o:         
            o.write(i) 
        # print(ab.text)
         #页码
      
   def get_all(self,b):              
      url=b #输入指定页码
      res=requests.get(url).text    
      soup=BeautifulSoup(res,'html.parser')
      page_list=soup.find('select').find_all('option')[-1].text
      #a=soup.find('div','digg').find_all('span')
      if int(page_list[1]):          
         return page_list[1] 
      
s=spaider()
#b=input('输入指定列表页链接')
b_list=input('输入列表')
#获取所有列表页

list_all=int(s.get_all(b_list))+1
for i in range(0,list_all):
   s.get_list(i)

