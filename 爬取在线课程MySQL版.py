from fake_useragent import UserAgent  # 导入伪造头部信息的模块
import asyncio  # 异步io模块
import aiohttp  # 异步网络请求模块
import requests  # 导入网络请求模块
from lxml import etree  # 导入lxml解析html的模块
import pandas  # 导入pandas模块
 
class HomeSpider():
    def __init__(self):
         self.data=[]
         self.headers={'User-Agent':UserAgent().random}
    async def request(self,url):
         async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url,headers=self.headers,timeout=3) as response:
                    print(response.status)
                    if response.status==200:
                        result= await response.text()
                        return result
            except Exception as e:
                print(e.args)
    def get_page_all(self,city):
        city_letter=self.get_city_letter(city)
        url = 'https://{}.lianjia.com/zufang/ab200301001000rco11rt200600000001rs{}/'.format(city_letter, city)
        response = requests.get(url,headers=self.headers)
        if response.status_code==200:
            html= etree.HTML(response.text)
            page_all=html.xpath('//*[@id="content"]/div[1]/div[2]/@data-totalpage')[0]
            print('租房信息总页码获取成功')
            return int(page_all)+1
        else:
            print('获取租房信息所有页码的请求失败')
    def get_city_letter(self,city_name):
        city_dict={'北京':'bj','上海':'sh','广州':'gz'}
        return city_dict.get(city_name)
    def remove_spaces(self,info):
        info_list=[]
        for i in info:
            x=i.replace(' ','').relpace('\n','')
            if x=='':
               pass
            else:
                info_list.append(x)
        return info_list
    def combined_region(self,big_region,small_region):
        region_list=[]
        for a,b in zip(big_region,small_region):
            region_list.append(a+'-'+b)
        return region_list    
    async def parse_data_all(self,page_all,city):
        for i in range(1,page_all):
            city_letter=self.get_city_letter(city)
            url= 'https://{}.lianjia.com/zufang/ab200301001000pg{}rco11rt200600000001rs{}/'.format(city_letter,i, city)
            html_text=await self.request(url)
            html =etree.HTML(html_text)
            print('获取'+url+'页信息')
            title_all=html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a/text()')
            big_region_all=html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[1]/text()') 
            small_region_all=html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[2]/text()') 
            square_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/text()[5]')
            floor_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/span/text()[2]')
            price_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()')
            title_list = self.remove_spaces(title_all)  # 删除标题信息中的空格与换行符
            region_list = self.combined_region(big_region_all, small_region_all)  # 组合后的区域信息
            square_list = self.remove_spaces(square_all)  # 删除面积信息中的空格与换行符
            floor_list = self.remove_spaces(floor_all)  # 删除楼层信息中的空格与换行符
            price_list = self.remove_spaces(price_all)  # 删除价格信息中的空格与换行符
        # 每页数据
            data_page = {'title': title_list,
                     'region': region_list,
                     'price': price_list,
                     'square': square_list,
                     'floor': floor_list}
            print('写入第'+str(i)+'页数据！')
            df = pandas.DataFrame(data_page)              # 创建DataFrame数据对象
            df.to_csv('{}租房信息.csv'.format(city),mode='a', encoding='utf_8_sig',index=None)  # 写入每页数据
    def start(self,page_all,city):
        loop=asyncio.get_event_loop()
        loop.run_until_complete(self.parse_data_all(page_all,city)) 


if __name__=='__main__':
    
    input_city = input('输入需要下载租房信息的城市名称！')
    home_spider=HomeSpider()
    page_all=home_spider.get_page_all(input_city)
    home_spider.start(page_all, input_city)
 
  
         