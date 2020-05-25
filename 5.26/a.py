import csv
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest

class node:    #定义node类用来储存每个月的数据
    def __init__(self,month,kaipan,shoupan,jine):
        self.month = month
        self.kaipan = kaipan
        self.shoupan = shoupan
        self.jine = jine
def __main__():
    month = re.compile(r'-\d{1,2}-')
    year_month = re.compile(r'\d{4}-\d{1,2}')
    #编译正则表达式查询月份和年月
    csv_reader=csv.reader(open('data.csv',encoding="GBK"))
    s = []
    flag = 1
    for i in csv_reader:
        if flag == 1:
            flag = 0
            continue
        temp = i[:3]
        temp.append(i[4])
        temp.append(i[7])
        temp.append(i[9])
        if temp[5] == 'N/A':
            continue
        s.append(temp)
    #处理数据，筛出有效数据
    kaipan = 0
    shoupan = 0
    jine = 0
    last = '00'
    data = []
    cnt = 0
    for i in s:
        mm = month.findall(i[2])
        mm = mm[0][1:-1]
        if mm != last and last != '00':
            now = node(i[2],float(kaipan)/cnt,float(shoupan)/cnt,jine)
            kaipan = 0
            shoupan = 0
            jine = 0
            last = mm
            cnt = 0
            data.append(now)
            print(year_month.findall(now.month)[0],now.kaipan,now.shoupan,now.jine)
        kaipan = kaipan + float(i[3])
        shoupan = shoupan + float(i[4])
        jine = jine + float(i[5])
        cnt = cnt+1
        last = mm
    #按照第二步要求处理数据
    writer = csv.writer(open('save.csv','w', newline=''))
    writer.writerow(["月份","开盘价","收盘价","成交额"])
    for i in range(len(data)):
        writer.writerow(year_month.findall(now.month)[0],data[i].kaipan,data[i].shoupan,data[i].jine])
    #将数据输出至save.csv
    x = []
    y1 = []
    y2 = []
    for i in range(len(data)):
        y1.append(data[i].kaipan)
        y2.append(data[i].shoupan)
        x.append(i+1)
    x = np.array(x)
    y1 = np.array(y1)
    y2 = np.array(y2)
    plt.plot(x,y1,label = "KAIPAN")
    plt.plot(x,y2,label = "SHOUPAN")
    plt.legend() 
    plt.show()
    #输出开盘价和收盘价随月份变化曲线

    y = []
    for i in range(len(data)):
        y.append(data[i].jine)
    y = np.array(y)
    print(kstest(y,'norm').pvalue>0.005)
    #因为数值的p值小于0.005,我们认为数据不服从正态分布
if __name__ == "__main__":
    __main__()
