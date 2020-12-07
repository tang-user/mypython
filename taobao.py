from lxml import etree
import requests
from bs4 import BeautifulSoup
from http import cookiejar
import json
import re
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
  'cookie': 'tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=296071141639785912; cna=Qa05FjJcvUACAatYKFCXRVZE; UM_distinctid=172fe8c34a2979-089103f8f1da8c-6b1b1279-1fa400-172fe8c34a38bb; t=f84bca8239fb8542a45d378e0296eab5; thw=cn; v=0; _tb_token_=e3150bb9e763b; _m_h5_tk=7a15ab21c3fecd447432aa2696fb65ec_1600250628886; _m_h5_tk_enc=ebc526a42903a23f8fc087ac7cb4ec8c; xlly_s=1; enc=Wurmw6AawVDSvwNSNU%2FO7guQljJkxo4y0WvtMOuZpe2Dgghndc%2BDeUZ6obOkwMGVcZh7QJzWRb4wjBtrPeQjxw%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=14cd1f0222340804dfd48db91cf83ef7; hng=CN%7Czh-CN%7CCNY%7C156; _samesite_flag_=true; JSESSIONID=B228681DD1202851735B104FAC00D459; tfstk=cV2fBw13SEYforfw3osr70Nf50k1ZytIfsg0cSNCD2kdQVZfiivERqCQsFE-K01..; l=eBS4WBIIqGo4Kit9BOfwourza77OSIRAguPzaNbMiOCPOh1p5t7GWZrf2r89C3GVh67BR3z9IwcUBeYBqIv4n5U62j-la_kmn; isg=BJiYNlfYcxrLKl_rfqnIiVNXacYqgfwLW0ZMYtKJ5FOGbThXepHMm65PpaXd_bTj'
    }
# form_data = {   
#            '_xsrf': 'f7vHnCByyZonF2oXF3K9adgExYUsDois',
       
#     }
# url='https://s.taobao.com/search?q=%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88'

# session = requests.session()
# session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
# response = session.post(url,headers=headers) #session登录网站
# r=requests.get(url,headers=headers)
# html=etree.HTML(r.text)
# title=html.xpath('//script/text()')[3]
# title=''.join(title)
with open('淘宝.txt',mode='r',encoding='utf-8') as f:
  title=f.read()


resault=re.findall('.*?raw_title":"(.*?)","pic_url.*?"',title,re.I)
print(resault)


    

# t=html.xpath('//*[@id="J_Itemlist_TLink_581176557325"]/text()[2]')

