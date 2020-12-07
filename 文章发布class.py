# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time 
import random
from selenium.webdriver.common.keys import Keys
from lxml import etree
import requests

class published:
    def __init__(self,url,n):
        self.url=url
        self.n=n
        self.dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\新建文件夹\file'
        self.imgs_path=r'C:\Users\Administrator\Desktop\生产'

    # 读取文件内容函数 title_name,img_url
    def red_file(self,title_name,img_url):
        # 要插入的文章尾的一段公司介绍
        conpy='''  
        <p>成都市佳味添成饮料科技研究所由一支在管理、研发、生产、包装、工艺等方面具有多年经验的高学历高素质的人才队伍组成，公司设有6大实验室，研发队伍由中国工程院院士和食品专业教授率领，为产品质量提供了坚实的保障。</p>
        <p>1. 配套提供产品研发服务。</p>
        <p>公司研发团队按客户要求的口感，为客户组织配方，调试出样品让客户品评，调试出客户满意的产品。公司保证研发出来的产品符合食品安全法和相关产品国家标准的规定。</p>
        <p>2. 配套提供包装设计服务。</p>
        <p>包括：瓶形设计、瓶盖设计、标签和纸箱装潢设计、易拉罐装潢设计等。公司有专业资深的设计师队伍，专人对接，可大大提高设计开发的效率。</p>
        <p>3. 配套提供采购服务。</p>
        <p>公司有长期合作的优质供应商队伍，由于长期合作且采购量大，若客户交由我公司统一采购物料，则可享受到优惠的价格，降低产品成本，提高采购效率，而且品质有保障。</p>
        <p>本文只采取了饮料配方及工艺研究中的某部分研究内容，如需得到完整的饮料配方技术及工艺流程可联系成都市佳味添成饮料科技研究所，作为专业的饮料配方研发公司，提供饮料配方研发整体方案,饮料配方调味整体方案,饮料配方技术整体方案,饮料配方专家咨询整体方案，饮料配方生产技术指导等饮料行业所需的各类技术和资源的饮料开发整体解决方案服务，联系电话：13518183030  13518182323</p>'''
        
        # title_name='大米和糙米乳饮料工艺条件的研究.txt'
        # 拿到目录下的文件名字并打开 
        file_path=self.dir_path+'\\'+title_name
        with open(file_path,encoding='gb18030') as f:
            # 以行的形式拿到文件内容
            p=f.readlines()
            # 存放内容  
            content2=[]                  
            # 先对拿到的单个文件内容进行处理，删除文章前后一段话并在后面随机加入一段.replace('\n','')

            for i in range(1,len(p)-2):  

                if i==5:
                    content2.append('<img src="{}">'.format(img_url))      
                content2.append('<p>'+p[i].replace('\n','').replace(' ','')+'</p>')   
            content2.append(conpy)
        if os.path.exists(title_name):
            os.remove(title_name) 
        for i in content2: 
            with open(title_name,mode='a+',encoding='gb18030') as ff:
                ff.write(i)
            
        # os.remove(file_path)
        # return content2  
        with open(title_name,mode='r',encoding='gb18030')  as r:
            cont=r.readlines()
        os.remove(file_path)
        os.remove(title_name)
        # print(cont)
        return cont
    

    # 拿到文件名字函数
    def get_file_name(self): 
        # 获取传来文件夹下的所有文件名
        file_name=os.listdir(self.dir_path)
        # 判断文件夹是否为空
        if  not file_name:
            print('该文件夹为空,没有文件可传')
            return
        else:
            return file_name
    def write_content(self,imgs_name,driver):
        
        for i in range(0,self.n):
            self.n=i
            # # 调用函数得到所有文件名
            file_name=self.get_file_name() 
            # 随机图片的路径
            img_path_name=self.imgs_path+'\\'+imgs_name[random.randint(0,len(imgs_name)-1)]       
             # 得到上传后图片的url，可直接用于网站内容中
            img_url=self.uploat_img(img_path_name,driver)
            # 随机文件名
            if len(file_name)==1:
                random_name=file_name[0]
            else:
                random_name=file_name[random.randint(0,len(file_name)-1)] 
            # 处理后的内容
            content2=self.red_file(random_name,img_url)
            if content2=='':
                print('内容为空不能进行下一步')
                return
            # 标题处理
            title=random_name.replace('.txt','').replace(' ','').replace('、','').replace('－','')
            # 写入标题
            driver.find_element_by_xpath("//input[@name='title']").send_keys(title)
            # 单击进入源码写入内容
            driver.find_element_by_xpath("//*[@id='cke_8']").click()
            time.sleep(5)
            # 写入内容
            driver.find_element_by_xpath("//*[@id='cke_body']").send_keys(content2)
            time.sleep(5)
            # 单击发布内容
            driver.find_element_by_xpath("./*//input[@name='imageField']").click()
            time.sleep(5)
            # 继续发布内容
            try:
                driver.find_element_by_link_text("继续发布文章").click()
            except:
                driver.find_element_by_link_text("继续发布文章").click()
            print('第{}篇文章发布完成,等待5秒'.format(i+1))
            time.sleep(5)
            # 一键更新网站
        driver.get(self.url+"/jwtcaaa028/makehtml_all.php") 
        try:   
            driver.find_element_by_name("Submit").click()
        except:
            driver.find_element_by_name("Submit").click()


    # 写入网站函数       
    def write_web(self,driver):     
        # 调用函数得到所有图片名字
        imgs_name=self.get_file_name()
        try:
            self.write_content(imgs_name,driver)
        except:
            if self.url=='http://www.drinks999.com' and self.n<=4:
                self.n=5-self.n
                self.write_content(imgs_name,driver)
            else:
                print(self.n)

        time.sleep(10)   


    # 上传图片
    def uploat_img(self,img_path_name,driver):
        # 找到图片上传框
        time.sleep(3)
        # driver.find_element_by_name('title').send_keys('title')
        try:
            driver.find_element_by_xpath('//*[@id="cke_27"]/span[1]').click()   
        except:
            print('没有找到che_27')     
        time.sleep(3)
        # 找到上传按钮
        driver.find_element_by_xpath('//*[@id="cke_dialog_tabs_84"]/a[3]').click()
        time.sleep(3)
        # 上传图片
        iframe=driver.find_element_by_id("cke_138_fileInput")
        driver.switch_to_frame(iframe)
        driver.find_element_by_xpath("//input[@name='upload']").send_keys(img_path_name)
        driver.switch_to.default_content()
        time.sleep(3)
        # 确定上传图片到服务器
        driver.find_element_by_xpath('//*[@id="cke_141_uiElement"]').click()
        time.sleep(3)
        # 图片插入文章
        # driver.find_element_by_xpath('//*[@id="cke_173_uiElement"]').click()
        # 上传图片的地址
        img_url=driver.find_element_by_id('cke_87_textInput').get_attribute('value')
        time.sleep(3)
        # 点击取消上传图片
        driver.find_element_by_id('cke_174_label').click()
        time.sleep(2)
        # 弹出对话框的处理，单击确定退出
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(2)
        return img_url


    # 搜狐发布
    def souhu(self,name,paw):
        # 所有文件路劲
        dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\souhu'
        imgs_path=r'C:\Users\Administrator\Desktop\生产' 

        # 登录地址
        url='https://mp.sohu.com/mpfe/v3/login'
        driver=webdriver.Chrome()
        print('打开浏览器，打开搜狐登录')
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
        for i in range(0,5):
            # 单击发布内容按钮
            driver.find_element_by_xpath("//a[@class='positive-button']/span").click()
            time.sleep(3)
            #  调用函数得到所有文件名
            file_name=self.get_file_name()   
            # 调用函数得到所有图片
            imgs_name=self.get_file_name()
            # 随机拼接图片在本地的地址
            img_path_name=imgs_path+'\\'+imgs_name[random.randint(0,len(imgs_name)-1)] 
            #文件名    
            random_name=file_name[random.randint(0,len(file_name)-1)]
            # 处理后的文件名即为需要的标题
            sou_title=random_name.replace('.txt','')
            # 拼接文件地址
            file_path=dir_path+'\\'+random_name
            # 按行读取内容 
            with open(file_path,mode='r',encoding='utf-8') as f:
                content2=f.readlines()    
            #自动填入标题    
            driver.find_element_by_xpath("//div[@class='publish-title']/input").send_keys(sou_title)
            time.sleep(3)
            # 填入内容，先点击内容输入框，再写入内容    
            driver.find_element_by_xpath("//div[@id='editor']/div").click()
            time.sleep(3)
            # 按行填入内容
            for c in range(0,len(content2)):
                if c==2:
                    # 点击上传图片
                    driver.find_element_by_xpath("//button[@class='ql-image']").click()    
                    time.sleep(3)
                    driver.find_element_by_xpath("//div[@class='upload-button']/input").send_keys(img_path_name)
                    time.sleep(3)
                    driver.find_element_by_xpath("//div[@class='bottom-buttons']/p[1]").click() 
                # 按行写入内容   
                driver.find_element_by_xpath("//div[@id='editor']/div").send_keys(content2[c])         
            # 最终发布按钮
            driver.find_element_by_xpath("//ul[@class='button-list']/li[2]").click()
            # 删除已发布的内容
            os.remove(file_path)
            print('第{}篇内容发布完成'.format(i+1))
            time.sleep(3)
        print('发布完成')

        driver.close()
        driver.quit()

    # 搜狐文章状态检查
    def check_souhu(self,name,paw):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver=webdriver.Chrome(options=option)
        # driver=webdriver.Chrome()
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
        for dd in range(0,5):
            if d[dd].text == '未通过':
                print('没有通过正在重新发布')
                driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/ul/li[4]/div/div[1]/div[3]/div/span[1]').click()
                print('这个点击到了')        
                time.sleep(5)
                driver.find_element_by_xpath('//ul[@class="button-list"]/li[2]').click()
            elif d[dd].text=='审核中':
                print('文章正常审核中请耐心等待')
                time.sleep(3)
            else:
                print('文章通过')
                n=n+1   
        driver.close()
        driver.quit() 
        return n  

    # 搜狐文章抓取
    def souhu_info(self,url):
        
        headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        datas=[]
        # 第一个
        res=requests.get(url,headers=headers)
        html=etree.HTML(res.text)
        # title=html.xpath('//ul/li[position()<6]/article/div/h4/a/text()')
        urls=html.xpath('//ul/li[position()<6]/article/div/h4/a/@href')
        
        for i in urls:        
            res1=requests.get('https:'+i,headers=headers)
            html=etree.HTML(res1.text)
            # 标题
            # title=html.xpath('//div[@class="text-title"]/h1/text()')[0]
            # title=title.strip()
            # # 内容
            # info=html.xpath('//article[@class="article"]/p[position()>1]/text()')
            # if os.path.exists(dir_path+'\\'+title+'.txt'):
            #     print('文章已存在，跳过此文章')
            #     continue
            # for c in range(0,len(info)):          
            #     if info[c]=='责任编辑：':
            #         continue
            #     with open(dir_path+'\\'+title+'.txt',mode='a',encoding='utf-8') as f:
            #         f.write(info[c]+'\r\n')
            # 图片
            img_url=html.xpath('//article[@class="article"]/p/img/@src')[0]
            if 'http:' not in img_url:
                img_url='http:'+img_url
            datas.append(img_url)
        return datas
    # 博客发布
    def sinaboke(self):    # 本地内容的保存位置
        url='https://mp.sohu.com/profile?xpt=Y2hvdWZlaTkwN0Bzb2h1LmNvbQ==&_f=index_pagemp_2&spm=smpc.content%2F179_5.author.3.1600398780179XlOQK0Z'
        dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\souhu'
        # 得到图片地址及抓取内容
        infos_img=published.souhu_info(self,url)

        url='http://blog.sina.com.cn/'  
        driver=webdriver.Chrome()
        print('打开浏览器，登录新浪博客')
        driver.get(url)
        # 填入用户名密码登录博客
        name='wanglan904@sohu.com'
        passw='463459227'
        driver.find_element_by_id('loginName').send_keys(name)
        driver.find_element_by_id('loginPassword').send_keys(passw)
        driver.find_element_by_id('submit-btn').click()
        time.sleep(3) 
        # 拿到文件名
        file_name=self.get_file_name()
        # 博客发文数量
        for i in range(0,4):        
            # 直接访问发布页面
            driver.get('http://control.blog.sina.com.cn/admin/article/article_add.php?is_new_editor=2')  
            # 从本地读取标题和内容
            with open(dir_path+'\\'+file_name[i],mode='r',encoding='utf-8') as f:
                infos=f.readlines()
            
            # 填入标题
            # 处理标题
            title=file_name[i].replace('.txt','')
            # driver.find_element_by_xpath('//*[@class="cInfo"]/input').send_keys('标题')//*[@id="upload_file_li"]/div/input
            driver.find_element_by_id('articleTitle').send_keys(title)
            # 切换到ifram框中填入内容/html/body
            time.sleep(5)
            f1=driver.find_element_by_xpath('//*[@id="SinaEditor_Iframe"]/iframe')
            time.sleep(5)
            driver.switch_to_frame(f1) 
            # 按行写入内容，第3行插入图片
            for c in range(0,len(infos)):
                if c == 2:
            # driver.find_element_by_xpath('/html/body').send_keys('内容')
            # time.sleep(5)
                    driver.switch_to.default_content()
                    # 单击打开上传图片对话框//*[@id="upload_file_li"]/div/input//*[@id="editorForm"]/div/div[1]/ul/li/div[1]//*[@id="img_74571599816454050"]//*[@id="uploadimage_11941599817248353"]
                    driver.find_element_by_class_name('ico_img_1').click()
                    time.sleep(5)
                    f2=driver.find_element_by_xpath('//*[@class="tMid"]/iframe')    
                    driver.switch_to_frame(f2)
                    # imgs_path=r'C:\Users\Administrator\Desktop\生产\荸荠.jpg'//*[@id="headerTab"]/ul/li[3]
                    driver.find_element_by_xpath('//*[@id="headerTab"]/ul/li[3]').click()
                    time.sleep(3)
                    # 清除已有的内容
                    driver.find_element_by_xpath('//*[@id="web_image_input"]').clear()
                    time.sleep(3)
                    # 填入要插入图片的地址
                    driver.find_element_by_xpath('//*[@id="web_image_input"]').send_keys(infos_img[i])
                    time.sleep(3)
                    # 单击添加按钮
                    driver.find_element_by_xpath('//*[@id="web_image_submit"]').click()
                    time.sleep(3)
                    # 单击插入图片到正文
                    driver.find_element_by_xpath('/html/body/div[1]/div[9]/a').click()
                    time.sleep(3)
                    driver.switch_to.default_content()
                    driver.switch_to_frame(f1)
                    driver.find_element_by_xpath('/html/body').send_keys('\r\n')                
                # 写入内容             
                driver.find_element_by_xpath('/html/body').send_keys(infos[c])
            driver.switch_to.default_content()
            # 选择栏目//*[@id="componentSelect"]
            driver.find_element_by_xpath('//*[@id="componentSelect"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="componentSelect"]/option[4]').click()
            time.sleep(1)
            # 填写标签
            driver.find_element_by_xpath('//*[@id="hotTagList"]/a[1]').click()
            driver.find_element_by_xpath('//*[@id="hotTagList"]/a[2]').click()
            time.sleep(1)
            # 点击发布//*[@id="_7161600072934812_btnOk"]
            driver.find_element_by_xpath('//*[@id="articlePostBtn"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@class="CP_w_btns_Mid"]/a').click()
            print('第{}{}篇发布完成需要等待两分钟'.format(i+1,title))
            # os.remove(dir_path+'\\'+file_name[i])
            for t in range(1,120):
                print('等待中...还有{}秒...'.format(120-t))
                time.sleep(1)
                        
    #   网站888发布
    def drinks888(self):
        # 所有文件路劲
        dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\2020'
        imgs_path=r'C:\Users\Administrator\Desktop\生产' 
        # drinks888文章要插入的内容
        drinks='本文只采取了饮料配方及工艺研究中的某部分研究内容，如需得到完整的饮料配方技术及工艺流程可联系成都市佳味添成饮料科技研究所，作为专业的饮料配方研发公司，提供饮料配方研发整体方案,饮料配方调味整体方案,饮料配方技术整体方案,饮料配方专家咨询整体方案，饮料配方生产技术指导等饮料行业所需的各类技术和资源的饮料开发整体解决方案服务，联系电话：13518183030  13518182323'
        url='http://www.drinks888.com/admin/login.aspx'
    
        #  调用函数得到所有图片名字
        imgs_name=self.get_file_name()
        print('打开浏览器，打开drinks888网站登录')
        driver=webdriver.Chrome()
        driver.get(url)
        # 用户名密码
        txtUserName='jiaweitiancheng'
        txtPassword='jwtc028'
        #找到用户名密码登录框 txtUserName  btnSubmit
        driver.find_element_by_id("txtUserName").send_keys(txtUserName)
        driver.find_element_by_id("txtPassword").send_keys(txtPassword)
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(3)
        # 发布5篇文章
        for i in range(0,5):
            driver.get('http://www.drinks888.com/admin/article/article_edit.aspx?action=Add&channel_id=6')
            # 选择栏目
            driver.find_element_by_xpath('//a[@class="select-tit"]').click()
            driver.find_element_by_xpath('//div[@class="select-items"]/ul/li[3]').click()  
            driver.find_element_by_id('autoImg').click()  
            time.sleep(3) 
            #  调用函数得到所有文件名
            file_name=self.get_file_name()        
            #随机文件名    
            random_name=file_name[random.randint(0,len(file_name)-1)] 
            # 处理标题
            title=random_name.replace('.txt','')
            #随机文件名写入标题   
            driver.find_element_by_id("txtTitle").send_keys(title)
            time.sleep(3)
            #选择详细信息
            driver.find_element_by_xpath('//div[@class="content-tab-ul-wrap"]/ul/li[2]/a').click()
            time.sleep(3)
            # 先选择字体
            driver.find_element_by_id('edui104_button_body').click()
            #选择宋体
            driver.find_element_by_id('edui106').click()  
            time.sleep(1)  
            # 调用函数得到所有图片名字
            imgs_name=self.get_file_name()
            # 拿到图片的具体名字和路径
            img_path_name=imgs_path+'\\'+imgs_name[random.randint(0,len(imgs_name)-1)] 
            time.sleep(3) 
            # 详细文件的名字和路径
            file_path=dir_path+'\\'+random_name
            # 按行读取内容 
            with open(file_path,encoding='utf-8') as f:
                content2=f.readlines()
            # 向内容中追加公司信息 
            content2.append(drinks)
            # 切换到内容发布的iframe框中  
            iframe=driver.find_element_by_xpath('//*[@id="edui165_body"]/div/iframe') #//*[@id="edui_input_kev2kau1"]    
            driver.switch_to_frame(iframe)
            for c in range(0,len(content2)):
                if c==2:
                    # 图片上传
                    driver.find_element_by_name('upfile').send_keys(img_path_name)
                    time.sleep(3)
                    driver.switch_to.default_content()
                    # 切换到主内容框单击使上传的图片局中
                    driver.find_element_by_id('edui44_state').click()
                    # 再切换到内容发布iframe中
                    driver.switch_to_frame(iframe)
                    # 上传图片后按回车键避免图片后面直接有文字
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)                
                    time.sleep(3) 
                # 向内容发布iframe框中按行追加内容                                  
                driver.find_element_by_xpath('/html/body').send_keys(content2[c])            
            time.sleep(3)
            # 内容追加完成后切换回主内容框并单击提交，一篇文章就发布完成   
            driver.switch_to_default_content()        
            driver.find_element_by_id('btnSubmit').click()
            print('第{}篇更新完成'.format(i+1))
            time.sleep(3)
            # 为避免重发发布文章完，每发布一篇文章就在目录中删除此文件
            os.remove(file_path)
            # 切换到主内容框中，进行下一篇文章的发布
            # driver.switch_to.default_content()
            time.sleep(3)
        print('发布完成')
        driver.close()
        driver.quit()

    # 818同城发布
    def tongcehng818(self):
        dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\souhu'
        url='https://mp.sohu.com/profile?xpt=Y2hvdWZlaTkwN0Bzb2h1LmNvbQ==&_f=index_pagemp_2&spm=smpc.content%2F179_5.author.3.1600398780179XlOQK0Z'
        # souhu_info(dir_path,url)
        # 登录地址
        url='http://www.818u.com/members/login.aspx'
        driver=webdriver.Chrome()
        print('打开浏览器，打开搜狐登录')
        driver.get(url)
        name='a463459227'
        passw='463459227'
        # 点击出现登录框/html/body/div[3]/div[2]/div/div[4]/table/tbody/tr/td[1]/a
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
        driver.find_element_by_xpath('//*[@id="userpassword"]').send_keys(passw)
        driver.find_element_by_xpath('//*[@id="Button1"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/div[4]/table/tbody/tr/td[1]/a').click()
        i=1
        while True:
            if i>5:
                break
            driver.find_element_by_xpath('//*[@id="Select_B"]/option[4]').click()
            driver.find_element_by_xpath('//*[@id="Select_M"]/option[2]').click()
            driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[4]/div/div[3]/input').click()
            time.sleep(3)
            #  调用函数得到所有文件名
            file_name=self.get_file_name()
            if len(file_name)==1:
                random_name=file_name[0]
            else:
                random_name=file_name[random.randint(0,len(file_name)-1)]   
            with open(dir_path+'\\'+random_name,encoding='utf-8') as f:
                con=f.readlines()
                
            title=random_name.replace('.txt','').strip()

            driver.find_element_by_xpath('//*[@id="titles"]').send_keys(title)  
            driver.find_element_by_xpath('//*[@id="keywords"]').send_keys('饮料配方研发')
            driver.find_element_by_xpath('//*[@id="neirong"]').send_keys(con)
            time.sleep(3)
            t=driver.find_element_by_xpath('//*[@id="titlesTip"]')            
            if t.text=='标题已经重复存在或者包含非法字符,请修改':
                print('标题重复，跳过重新发')
                driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/div[4]/table/tbody/tr/td[1]/a').click()
                continue
            print('30秒内手动填写验证码')
            time.sleep(30)
            driver.find_element_by_xpath('//*[@id="Button1"]').click()
            print('第{}篇文章发布'.format(i))
            i=i+1
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/table/tbody/tr/td[1]/a').click()
            
        print('今日文章发布完成')
        driver.close()
        driver.quit()

    # 创头条文章发布/html/body/section/ul/div[3]/div/li[1]/a
    def check_chuang(self):
        # 图片地址
        imgs_path=r'C:\Users\Administrator\Desktop\生产' 
        # 文件地址
        dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\2020\souhu'    
        url='http://www.ctoutiao.com/corp.php?act=logon'
        driver=webdriver.Chrome()
        print('打开浏览器，打开搜狐登录')
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="J_logonForm"]/p[1]/input').send_keys('13980926167')
        driver.find_element_by_xpath('//*[@id="J_logonForm"]/p[2]/input[2]').send_keys('Aa463459227/')
        driver.find_element_by_xpath('//*[@id="J_lbton"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/header/div/div[2]/a[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/section/ul/div[3]/div/li[1]/a').click()
        time.sleep(5)
        #  调用函数得到所有文件名/html/body/section/div/div/h1/b/a/html/body/header/div/div[2]/a[3] /html/body/section/div/div/h1/b/a
        for i in range(0,5):
            file_name=self.get_file_name()        
            #随机文件名    
            random_name=file_name[random.randint(0,len(file_name)-1)] 
            # 处理标题并填入
            title=random_name.replace('.txt','')
            driver.find_element_by_xpath('/html/body/section/div/div/h1/b/a').click()
            print('20秒内手动输入验证码')
            time.sleep(20)
            driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title) 
            time.sleep(3)  
            driver.find_element_by_xpath('//*[@id="cate26"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="post_tags"]').send_keys('饮料配方')
            # 详细文件的名字和路径
            file_path=dir_path+'\\'+random_name
            # 按行读取内容 
            with open(file_path,mode='r',encoding='utf-8') as f:
                content2=f.readlines()
            os.remove(file_path)
            # 内容
            f1=driver.find_element_by_xpath('//*[@id="ueditor_0"]')
            driver.switch_to_frame(f1)
            for c in range(0,len(content2)):
                if c==2:
                    # 调用函数得到所有图片名字
                    imgs_name=self.get_file_name()
                    # 拿到图片的具体名字和路径
                    img_path_name=imgs_path+'\\'+imgs_name[random.randint(0,len(imgs_name)-1)] 
                    time.sleep(3) 

                    # 图片上传    
                    driver.switch_to.default_content()
                    driver.find_element_by_xpath('//*[@id="edui59_body"]').click()
                    time.sleep(2)
                    # 打开图篇上传框//*[@id="queueList"]/div[1]/div[3]/div[2]//*[@id="edui57_body"]
                    
                    f_tu=driver.find_element_by_xpath('//*[@id="edui55_iframe"]')
                    driver.switch_to_frame(f_tu)
                    driver.find_element_by_xpath('//input[@name="file"]').send_keys(img_path_name)
                    time.sleep(2)                
                    driver.find_element_by_xpath('//*[@id="queueList"]/div[1]/div[3]/div[2]').click()                
                    time.sleep(3) 
                    driver.switch_to.default_content()
                    driver.find_element_by_xpath('//*[@id="edui57_body"]').click()                               
                    driver.switch_to_frame(f1)
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
                if '佳味添成' in content2[c]:
                    driver.switch_to.default_content()
                    driver.find_element_by_xpath('//*[@id="edui18_body"]').click()
                    time.sleep(1)
                    driver.switch_to_frame(f1)
                    driver.find_element_by_xpath('/html/body').send_keys(content2[c])
                    driver.switch_to.default_content()
                    driver.find_element_by_xpath('//*[@id="edui18_body"]').click()
                    driver.switch_to_frame(f1)
                    continue
                if content2[c]==' ':                
                    continue
                driver.find_element_by_xpath('/html/body').send_keys(content2[c])    
            driver.switch_to.default_content()  
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="J_btnbox"]/em[3]').click()
            time.sleep(5)
            # 确定发布//*[@id="J_btnbox"]/em[3]//*[@id="J_btnbox"]/em[3]
            driver.find_element_by_xpath('//h3/a[2]').click()
            print('第{}篇文章发布'.format(i+1))
            time.sleep(5)
        driver.close()
        driver.quit()
   

    # 主函数
    def main(self):
        
        if self.url=='http://www.drinks999.com':
            url_cid=self.url+'/jwtcaaa028/article_add.php?channelid=1&cid=2'
        elif self.url=='http://www.drinkssss.com':
            url_cid=self.url+'/jwtcaaa028/article_add.php?channelid=1&cid=4'
        else:
            url_cid=self.url+'/jwtcaaa028/article_add.php?channelid=1&cid=3'
        driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        print("启动浏览器，打开{}登录界面".format(self.url))
        driver.get(url_cid)
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
        # 所有上传的文件夹路径
        # dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\新建文件夹\file'
        # # # 所有图片存放的文件夹路径
        # imgs_path=r'C:\Users\Administrator\Desktop\生产'    
        # 写入网站内容         
        self.write_web(driver)   
        


        print('网站{}更新完成'.format(self.url))
        time.sleep(3)
        # 关闭
        driver.close()
        # # 退出
        driver.quit()



main=published('http://www.drinks999.com',5)
main.main()
        

# if __name__=='__main__':

#     dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\新建文件夹\file'
        # try:
        #     main('http://www.drinks999.com',5)
        # except:
        #     print('999网站发布出错')
        # try:
        #     main('http://www.drinksaaa.com',1)
        # except:
        #     print('aaa网站发布出错')
        #     main('http://www.drinksaaa.com',1)
        # try:
        #      main('http://www.drinksbbb.com',1)
        # except:
        #     print('bbb网站发布出错')
        #     main('http://www.drinksbbb.com',1)
        # try:
        #     main('http://www.drinksccc.com',1)
        # except:
        #     print('ccc网站发布出错')
        #     main('http://www.drinksccc.com',1)
        # try:
        #     main('http://www.drinksddd.com',1)
        # except:
        #     print('ddd网站出错')
        #     main('http://www.drinksddd.com',1)
        # try:
        #     main('http://www.drinkseee.com',1)
            
        # except:
        #     print('eee网站出错')
        #     main('http://www.drinkseee.com',1)
        # try:
        #     main('http://www.drinksqqq.com',1)
        # except:
        #     print('qqq网站出错')
        #     main('http://www.drinksqqq.com',1)
        # try:
        #     main('http://www.drinksrrr.com',1)
        # except:
        #     print('rrr网站出错')
        #     main('http://www.drinksrrr.com',1)
        # try:
        #     main('http://www.drinkssss.com',1)
        # except:
        #     print('sss网站出错')
        #     main('http://www.drinkssss.com',1)
        # try:    
        #     main('http://www.drinkskkk.com',1)
        # except:
        #     print('kkk网站出错')
        #     main('http://www.drinkskkk.com',1)
        # try:
        #     main('http://www.drinkshhh.com',1)
            
        # except:
        #     print('hhh网站出错')
        #     main('http://www.drinkskkk.com',1)
        # try:

        #     main('http://www.drinksggg.com',1)
        # except:
        #     print('ggg网站出错')
        #     main('http://www.drinksggg.com',1)
        # try:
        #     main('http://www.drinksjjj.com',1)
        # except:
        #     print('jjj网站出错')
        #     main('http://www.drinksjjj.com',1)
        # try:
        #     main('http://www.drinksfff.com',1)
        # except:
        #     print('fff网站出错')
        #     main('http://www.drinksfff.com',1)
        # try:   
        #     main('http://www.drinkslll.com',1)
        # except:
        #     print('lll网站出错')
        #     main('http://www.drinkslll.com',1)
        # try:
        #     main('http://www.drinksooo.com',1)
        # except:
        #     print('ooo网站出错')
        #     main('http://www.drinksooo.com',1)
        # try:
        #     main('http://www.drinksppp.com',1)
        # except:
        #     print('ppp网站出错')
        #     main('http://www.drinksppp.com',1)
        # try:
        #     main('http://www.drinksmmm.com',1)
        # except:
        #     print('mmm网站出错')
        #     main('http://www.drinksmmm.com',1)
        # try:
        #     main('http://www.drinksnnn.com',1)
        # except:
        #     print('nnn网站出错')
        #     main('http://www.drinksnnn.com',1)
        # file_number=len(get_file_name(dir_path))
        # print('还剩下{}个文件未发，还能继续发布{}天'.format(file_number,file_number/23))
        # print('网站888开始更新')
        # drinks888()
        # print('所有网站更新完成')
        # print('搜狐第一个账号登录发布')  
        # souhu('13518183030','jwtc4000282990') 
        # print('搜狐第二个账号登录发布')
        # souhu('choufei907@sohu.com','hzdklx25456')
        # time.sleep(120)
        # print('等待中.....')
        
        # 搜狐文章通过检查
        # print('搜狐第一个账号登录发布')  
        # check_souhu('13518183030','jwtc4000282990') 
        # print('搜狐第二个账号登录发布')
        # check_souhu('choufei907@sohu.com','hzdklx25456')
        # time.sleep(10)
        # print('博客登录发布')
        # sinaboke()
        # print('818登录发布')
        # try:
        #     tongcehng818()
        # except:
        #     print('发布错误')
        # 创头条的
        # check_chuang()
        
    

