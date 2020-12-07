from bs4 import BeautifulSoup
import requests
import random
from fake_useragent import UserAgent



class spaider():

  
  try:

    def get_list(self,word):#得到列表页          
      
      list_url="https://www.baidu.com/s?wd={}&pn".format(word)
      
      res=requests.get(list_url,headers=head).text 
      
      soup=BeautifulSoup(res,'html.parser')        
      list_a=soup.find('div','content_left').find_all('div','result')
      print(len(list_a))             
      #for i in range(len(list_a)):
      #得到正确链接
        #title_url=list_a[i].find('a')['href']
        #h_url=requests.get(title_url).url        
      #得到标题
        #h3_t=list_a[i].find('a').text
        #写入文件 
        #with open('搜索结果.txt','a',encoding='utf-8') as o:
        #  o.write(h3_t+'-'+h_url+'\n')
  except:
    print('Handle Exception')

  
   #for i in a_list: 
                            
        #self.content(i)
       # with open('文章链接.txt','a',encoding='utf-8') as o:
          
        # o.write(i['href']+'\n')
      
   #def content(self,url):  
          
    #  aa=r'\/\:*？?"<>l'      
     # con_res=requests.get(url['href']).text      
     # soup = BeautifulSoup(con_res, "html.parser")
    #  ab=soup.find('div','content').find_all('p')
     # title=soup.find('h1').text    
              
      #for i in title:
       #  if i in aa:
    #        title=title.replace(i,'')
    #  for i in ab:
     #    i=str(i)
      #   with open(title+'.txt','a',encoding='utf-8') as o:         
     #       o.write(i) 
        # print(ab.text)
         #页码
      
   #def get_all(self,b):              
     # url=b #输入指定页码
     # res=requests.get(url).text    
     # soup=BeautifulSoup(res,'html.parser')
      #page_list=soup.find('select').find_all('option')[-1].text
      #a=soup.find('div','digg').find_all('span')
     # if int(page_list[1]):          
      #   return page_list[1]       
s=spaider()
#proxy = {
    #'https': 'https://60.168.207.153:8888'
#}
ua=UserAgent()
head={'User-Agent':'Mozilla/4.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

#b=input('输入指定关键词')
###b_list=input('输入列表')
#获取所有列表页
#list_all=int(s.get_all(b_list))+1
#for i in range(0,list_all):
  # s.get_list(i)

s.get_list('研发配方')





