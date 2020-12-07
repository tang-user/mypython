# -*- coding: utf-8 -*-
from selenium import webdriver
import re,os,json,random
import time
from lxml import etree
import requests

# 文件重命名
def re_name():
    new_path =r'C:\Users\Administrator\Desktop\唐富\唐富\2020\scrapy'
    dir_path =r'C:\Users\Administrator\Desktop\唐富\唐富\2020\scrapy2'
    file_name=os.listdir(dir_path)

    for files in file_name:
        with open (dir_path+'\\'+files,'r',encoding='utf=-8') as ff:
            infors=ff.readlines()
        if '植物饮料招商' in files or '植物饮料招商厂家':
            new_name=files.replace('植物饮料招商','植物饮料配方研发专家').replace('厂家','')
        if '袋装饮料加工' in files:
            new_name=files.replace('袋装饮料加工','饮料配方研发')
        if '固体饮料代加工' in files:
            new_name=files.replace('固体饮料代加工','固体饮料配方技术')
        if '胶原蛋白肽饮料代加工' in files:
            new_name=files.replace('胶原蛋白肽饮料代加工','胶原蛋白肽饮料配方')
        if '液体饮料' in files:
            new_name=files.replace('液体饮料','液体饮料配方研发').replace('代加工','').replace('厂家','').replace('加工厂','')
        if "饮料贴牌定制" in files:
            new_name=files.replace('饮料贴牌定制','饮料配方研发')
        # else:
        #     new_name=files
        
        ff=open(new_path+'\\'+new_name,'a+',encoding='utf-8')
        for inf in infors:
            ff.write(inf)         
        ff.close()
        
# re_name()

# 改写文件内容和标题
def overwrite():
    cont='''<p>成都市佳味添成饮料科技研究所是经政府部门颁证认可的饮料技术科研机构，是中国饮料工业协会会员单位，四川省食品科学技术学会副理事长单位／饮料专业委员会主任单位，四川大学食品学科学生实习基地，四川大学农产品加工研究院战略合作单位，中国食品报网战略合作单位，中国食品品牌研究院会员单位等资质的组织，包括中国工程院院士朱蓓薇教授、四川大学食品学院原院长卢晓黎教授等专家顾问在内，共有60余人的饮料专业技术人员团队，在成都、北京、上海、杭州、济南和四川大学有6大专业实验室，工程技术人员具有27年行业资深经验，服务了包括新希望乳业、完达山、太子奶、扬子江、燕之屋、汇源果汁、娃哈哈、王老吉、冰点、初元、熊出没等上千家饮料生产企业的产品开发和技术支持服务。</p>
    <p>成都市佳味添成饮料科技研究所是中国饮料产品设计整体方案服务平台，提供以饮料配方研发为核心的整体方案服务，服务内容包括食品饮料技术研究，食品饮料产品开发，食品饮料技术咨询、指导、转让等一站式饮料项目服务。作为专业的饮料配方研发公司，提供饮料配方研发,饮料配方调味,饮料配方技术,饮料配方专家咨询，饮料配方生产技术指导等饮料行业所需的各类技术和资源；联系电话：13518183030  13518182323</p>
    '''
    new_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\scrapy2'
    dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\scrapy'
    file_name=os.listdir(dir_path)

    for old_name in file_name:
        with open(dir_path+'\\'+old_name,'r',encoding='utf=-8') as dd:
            cc=dd.readlines()
        new_name=old_name.replace(' ','').replace('（一）','').replace('”','').replace('【','').replace('】','').replace('，','').replace('（二）','').replace('?','').replace('“','')
        ff=open(new_path+'\\'+new_name,'a+',encoding='utf=-8') 
        for c in cc:
            if '植物饮料招商' in c or '植物饮料招商' in old_name:
                cc=c.replace('饮料加工厂家','饮料配方研发专家')
                new_name=old_name.replace('饮料加工厂家','饮料配方研发专家')
            elif '饮料贴牌厂家' in c or '饮料贴牌厂家' in old_name:
                cc=c.replace('饮料贴牌厂家','饮料技术研发专家') 
                new_name=old_name.replace('饮料贴牌厂家','饮料技术研发专家')
            elif '饮料代加工' in c or '饮料代加工' in old_name:
                dd=c.replace('饮料代加工','饮料配方技术') 
                new_name=old_name.replace('饮料代加工','饮料配方技术')
            elif '饮料贴牌' in c or '饮料贴牌' in old_name:
                cc=c.replace('饮料贴牌','饮料配方工艺') 
                new_name=old_name.replace('饮料贴牌','饮料配方工艺')
            ff.write(c)            
        ff.close()
        
        # with open(new_path+'\\'+new_name,'a+',encoding='utf-8') as ff:
        #     ff.write(cc)
        # dd=cc[0].replace(' ','')
        # ff=open(new_path+'\\'+old_name,'a+',encoding='utf=-8') 
        # dd=cc[0].replace(' ','')
        # for c in range(0,len(dd),150):            
        #     ff.write('<p>'+dd[c:c+150]+'</p>')
        # ff.write(cont)
        # ff.close()
# overwrite()
# 删除不满条件的文件


# path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\scrapy'
# files_name=os.listdir(path)
# for f in files_name:
#     with open(path+'\\'+f,'r',encoding='utf-8') as ff:
#         cc=ff.read()
#     os.remove(path+'\\'+f)
#     dd=re.findall('-.*?.',f)
#     dd=str(dd)
#     if '配方' not in f:
#         f=f.replace('饮料','饮料配方研发')
#     with open(path+'\\'+f,'a+',encoding='utf-8') as dd:
#         dd.write(cc)
def bilibili():
    driver=webdriver.Chrome()
    driver.get('https://member.bilibili.com/platform/home')
    path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\boke'
    file_name=os.listdir(path)

    driver.find_element_by_id('login-username').send_keys('13980926167')
    driver.find_element_by_id('login-passwd').send_keys('a463459227')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
    time.sleep(10)
    print('输入验证码')
    print('登录成功')
    time.sleep(5)
  
    n=1
    while True:
        if n > 5:
            break
        driver.find_element_by_id('nav_upload_btn').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="tab-container"]/a[2]').click()
        time.sleep(1)
        iframe1=driver.find_element_by_xpath('//*[@id="edit-article-box"]/div/iframe')
        driver.switch_to_frame(iframe1)
        random_name=file_name[random.randint(0,len(file_name)-1)]
        with open(path+'\\'+random_name,'r',encoding='utf-8') as ff:
           information=ff.readlines() 
        title=random_name.replace('.txt','')
        driver.find_element_by_xpath('//div[@class="original-editor-wrap"]/div[1]/div/div[1]/textarea').send_keys(title)
        driver.switch_to.default_content()
        # 跳转到内容填写iframe/html/body//*[@id="edit-page"]/div[2]/div[1]/div/div[1]/textarea
        print('跳转到内容填写iframe2')
        iframe2=driver.find_element_by_id('ueditor_0')
        driver.switch_to_frame(iframe2)
        driver.find_element_by_xpath('/html/body').send_keys(information)
        driver.switch_to.default_content()
        print('第{}篇文章发布完成'.format(n))
        # 删除发过的文章
        os.remove(path+'\\'+random_name)
        n+=1        
        time.sleep(10)

bilibili()
#b站栏目文章抓取
def bili_cont():
    datas=[]
    url='https://api.bilibili.com/x/space/article?mid=702710400&pn=1&ps=12&sort=publish_time&jsonp=jsonp'
    res=requests.get(url)
    html=res.text
    title=re.findall('日常.*?"title":"(\S+?)"',html)
    url_id=re.findall('{"id":(\d+),"category',html)
    for i in range(0,5):
        datas.append('https://www.bilibili.com/read/cv{}'.format(url_id[i]))
        datas.append(title[i])
    return datas

# 列表页
def zs_spaider():
    url='http://www.zshksp.com/comp/portalResNews/list.do?compId=portalResNews_list-15613804400872150&cid=3&pageSize=3&currentPage={}'

    for i in range(1,33):
        res=requests.get(url.format(i))
        html=etree.HTML(res.text)
        # 列表链接
        list_url=html.xpath('//a[@class="e_link"]/@href')
        for lis in list_url:
            Details('http://www.zshksp.com'+lis)

# 详情页内容
def Details(url_det):
    res=requests.get(url_det)
    html=etree.HTML(res.text)
    # url='http://www.zshksp.com/news/15.html'
    t=html.xpath('//h1/div/text()')    
    path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\scrapy'
    title=t[0].replace('\n','').replace(' ','').replace('?','').replace('"','')
    infors=html.xpath('//*[@id="c_portalResNews_detail-15613806917746494"]/div/div[@data-ename="资讯详细描述"]//text()')
   
    ff=open (path+'\\'+title+'.txt','a+',encoding='utf-8') 
    for infor in infors:
        infor=infor.replace('\n\n','\n').replace('中山市惠康食品饮料有限公司','成都市佳味添成饮料科技研究所').replace('惠康','')
        ff.write(infor)
    ff.close()
   
# zs_spaider()
