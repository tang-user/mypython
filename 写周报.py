import datetime
import xlrd
import xlwt 	
from xlwt import Workbook
# 主函数
def main():    
    # 新建的工作表
    print('新建的工作表')
    workbook_write = xlwt.Workbook(encoding = 'utf-8')
    sheet_wirte = workbook_write.add_sheet('Sheet1')
    # 设置宽度    
    sheet_wirte.col(1).width=10000
    sheet_wirte.col(2).width=10000
    sheet_wirte.col(3).width=10000
    sheet_wirte.col(4).width=10000
    sheet_wirte.col(5).width=10000
    sheet_wirte.col(6).width=10000
    sheet_wirte.col(7).width=10000
    # 创建对齐方式
    # alignment = xlwt.Alignment() 
    # alignment.vert = xlwt.Alignment.HORZ_CENTER
    # alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle() 
    al = xlwt.Alignment()
    al.horz = 0x02 
    style.alignment = al
    # 字体颜色
    fnt = xlwt.Font()
    fnt.colour_index = 2 # 设置其字体颜色 
    style.font=fnt
    # 合并行写入数据，参数分别为行、列、数据 	
    sheet_wirte.write_merge(1,1,0,1, '网站文章更新',style) 
    sheet_wirte.write_merge(1,1,2,3, '搜狐新浪',style) 
    sheet_wirte.write_merge(1,1,4,5, '818同城发布',style) 
    sheet_wirte.write_merge(1,1,6,7, '创头条',style) 

    # 打开表得到数据
    datas=open_excel()
    # 定入新表
    write_excel(datas[0],datas[1],datas[2],datas[3],sheet_wirte)    
    # 保存创建新表 
    workbook_write.save('C:/Users/Administrator/Desktop/唐富/唐富/5月工作表/{}周报.xls'.format(datetime.datetime.now().strftime("%m-%d")))
    # 打开工作表
def open_excel():
    inter_datas=[]
    tongcheng_datas=[]
    chuangtoutiao_datas=[]
    souhu_boke_datas=[]
    now_time =datetime.datetime.now()-datetime.timedelta(days=1)
    now_time=now_time.strftime("%Y-%m-%d")
    for i in range(0,5):
        now_time=datetime.datetime.now()-datetime.timedelta(days=i)
        need_time=now_time.strftime("%Y-%m-%d")
        reading_book=xlrd.open_workbook('C:/Users/Administrator/Desktop/唐富/唐富/5月工作表/{}工作日报.xlsx'.format(need_time))  
        sheet_read=reading_book.sheet_by_index(0)
        # 得到总行数
        count_rows=sheet_read.nrows
        # 调用得到
        datas=excel_datas(count_rows,sheet_read,inter_datas,tongcheng_datas,chuangtoutiao_datas,souhu_boke_datas)    
    return datas       
# 从行4，列1开始读取数据
# 取第4行，第1~3列（不含第3）
def excel_datas(count_rows,sheet_read,inter_datas,tongcheng_datas,chuangtoutiao_datas,souhu_boke_datas):
    for i in range(4,count_rows):
        # 818、创头条的数据
        col_infos=sheet_read.row_values(i, 3, 5) 
        if col_infos[0]=='创头条':
            # print(col_i[0])
            # del col_infos
            n=i+1        
            for n in range(n,count_rows):
                col_infos=sheet_read.row_values(n, 3, 5)
                if col_infos[0]=='':
                    break
                chuangtoutiao_datas.append(col_infos[0])
                chuangtoutiao_datas.append(col_infos[1])
            break
        tongcheng_datas.append(col_infos[0])
        tongcheng_datas.append(col_infos[1])

    for i in range(4,count_rows):
        # 拿到数据
        row_infos=sheet_read.row_values(i, 1, 3)    
        if row_infos[0]=='搜狐新浪':
            # del row_infos
            n=i+1
            for n in range(n,count_rows):
                row_infos=sheet_read.row_values(n, 1, 3)
                souhu_boke_datas.append(row_infos[0])
                souhu_boke_datas.append(row_infos[1])
            break
        if row_infos[1]=='' :
            del row_infos        
            continue
        inter_datas.append(row_infos[0])
        inter_datas.append(row_infos[1])
    return inter_datas,souhu_boke_datas,tongcheng_datas,chuangtoutiao_datas
    # 写入网站数据i[0],i[1],i[2],i[3],sheet_wirte
def write_excel(inter_datas,souhu_boke_datas,tongcheng_datas,chuangtoutiao_datas,sheet_wirte):
    n=2
    # print(inter_datas)
    print("网站数据写入")
    for i in range(0,len(inter_datas),2):
        sheet_wirte.write(n, 1,inter_datas[i])
        sheet_wirte.write(n, 2,inter_datas[i+1])
        n=n+1
        
    # 写入搜狐博客数据
    print("搜狐博客数据写入")
    n=2
    for i in range(0,len(souhu_boke_datas),2):
        sheet_wirte.write(n, 3,souhu_boke_datas[i])
        sheet_wirte.write(n, 4,souhu_boke_datas[i+1])
        n=n+1
    # 写入818数据
    print("818数据写入")
    n=2
    for i in range(0,len(tongcheng_datas),2):
        sheet_wirte.write(n, 5,tongcheng_datas[i])
        sheet_wirte.write(n, 6,tongcheng_datas[i+1])
        n=n+1
    # 写入创头条数据
    print("创头条数据写入")
    n=2
    for i in range(0,len(chuangtoutiao_datas),2):
        sheet_wirte.write(n, 7,chuangtoutiao_datas[i])
        sheet_wirte.write(n, 8,chuangtoutiao_datas[i+1])
        n=n+1
if __name__=='__main__':   
    main()
