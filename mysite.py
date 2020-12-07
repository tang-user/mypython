# -*- coding: utf-8 -*-
import os
import random
dir_path=r'C:\Users\Administrator\Desktop\唐富\唐富\新建文件夹\未处理文件\组合1'
file_name=os.listdir(dir_path)
sss=file_name[random.randint(0,len(file_name)-1)]
with open(dir_path+'\\'+sss,'r',encoding='utf-8') as ff:
    aa=ff.readlines()
cc=[]
if len(aa)>1:
    print('多行')
    for a in aa:
        if a==' ' or a== '\n\r' :
            continue
        cc.append(a.replace('\n','').replace('<!--fdnewword end-->',''))
    print(cc[3])
else:
    print('单行')
    cc.append(aa[0].replace('\n','').replace('<!--fdnewword end-->',''))

    print(cc)
# print(cc)