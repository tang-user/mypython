from lxml import etree
import requests
import re
url="https://wenku.baidu.com/view/7deba6a8fd4ffe4733687e21af45b307e971f966.html"
header = {'User-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'}
res = requests.get(url , headers = header)
html=res.text
# with open('文库.txt',mode='w',encoding='utf-8') as f:
#     f.write(res.text)
# infos=html.xpath('//div[@id="doc-title"]/p/text()')
# print(infos)
infos=re.findall('<p .*> (.*)</p>',html,re.I)
print(infos)