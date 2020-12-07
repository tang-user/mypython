# -*- coding: utf-8 -*-
import pandas as pd
import datetime
now_time=datetime.datetime.now().strftime('%Y-%m-%d')
df=pd.read_excel('C:/Users/Administrator/Desktop/唐富/唐富/5月工作表/{}工作日报.xlsx'.format(now_time))
print(format(df))