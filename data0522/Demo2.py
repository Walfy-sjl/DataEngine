import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def getYearQuarter(year,month):
    # print(year+month)
    list = []
    nn = month // 3
    n = 4
    while n > 0:
        list.append(str(year) + " Q" + str(nn))
        nn = nn - 1
        if nn == 0:
            nn = 4
            year = year - 1
        n = n - 1
    list.reverse()
    return list

def getYearMonth(year,month):
    list = []
    mm = '{:0>2d}'.format(month)
    yy = year
    if (month-1) == 0:
        mm_last = 12
        yy_last = year-1
    else:
        mm_last = '{:0>2d}'.format(month-1)
        yy_last = year
    list.append(str(yy_last) + "-" + str(mm_last))
    list.append(str(yy) + "-" + str(mm))
    return list

year = datetime.datetime.now().year
month = datetime.datetime.now().month-2
source_data = "salesdata.csv"

segbodmap = {'C NB':'C Sedan','B SUV':'B SUV','B NB':'B Sedan','A SUV':'A SUV',
             'A MPV':'A MPV','A HB':'A HB','A NB':'A Sedan',
            'A0 HB':'A0 HB','A0 SUV':'A0 SUV'}
segbodlist = list(segbodmap.keys())
segbodlist.append('Others')
subsublist = ['NEV','Premium','Plus','Main','Entry','Low']

data = pd.read_csv(source_data, encoding="ANSI")
data = pd.DataFrame(data)
data['brand_indicator']=data['brand_indicator'].apply(lambda x: 'Premium' if x == 'Luxury' else x)
data['segbody'] = data['segment']+' '+data['bodytype']
data['year_quarter'] = data['year'].astype(str)+' '+data['quarter']
# data['segbodyy'] = data['segbody'].apply(lambda x : x.strip() if x.strip() in segbodlist else('Others'))
data['segbodyy'] = data['segbody'].apply(lambda x : x if x in segbodlist else('Others'))
data['segbodyy'] = data['segbodyy'].astype('category').cat.set_categories(segbodlist)
data['subsubsegment'] = data['subsubsegment'].astype('category').cat.set_categories(subsublist)

data_retail = data[(data['year'] > year-2) & (data['WRstatus'] == 'R/R')]
data_wholesale = data[(data['year'] > year-2) & (data['WRstatus'] == 'W/W')]

retail_202005 = data_retail[(data_retail['year'] == year) & (data_retail['month'] == month)]['sales'].sum()
retail_20200105 = data_retail[(data_retail['year'] == year) & (data_retail['month'] <= month)]['sales'].sum()
retail_201905 = data_retail[(data_retail['year'] == year-1) & (data_retail['month'] == month)]['sales'].sum()
retail_20190105 = data_retail[(data_retail['year'] == year-1) & (data_retail['month'] <= month)]['sales'].sum()
retail_yoy = format((retail_202005/retail_201905-1),'.1%')
retail_acc_yoy = format((retail_20200105/retail_20190105-1),'.1%')


p11_mid = data_retail.groupby(['year_quarter','segbodyy'])['sales'].sum()
# print(p11_mid.unstack(0).unstack(0))
p11_mid2 = pd.DataFrame(p11_mid.unstack(0),columns=getYearQuarter(year,month))
print(p11_mid2)
p11_ll = data_retail[data_retail['month'] <= month].groupby(['year','segbodyy'])['sales'].sum()
p11_ll2 = pd.DataFrame(p11_ll.unstack(0))
print(p11_ll2)
p11_rr = data_retail[data_retail['month'] <= month].groupby(['YearMon','segbodyy'])['sales'].sum()
p11_rr2 = pd.DataFrame(p11_rr.unstack(0),columns=getYearMonth(year,month))
print(p11_rr2)
p11_ll_reset = p11_ll2.reset_index(drop=False)
p11_mid_reset = p11_mid2.reset_index(drop=False)
p11_rr_reset = p11_rr2.reset_index(drop=False)
p11_res = pd.merge(p11_ll_reset, p11_mid_reset, on='segbodyy')
p11_res = pd.merge(p11_res,p11_rr_reset, on='segbodyy')
print(p11_res)

# writer = pd.ExcelWriter('filename.xlsx')
# p11_res.to_excel(writer, sheet_name='第二表')
# writer.save()
# writer.close()
p12_dataset = data_retail[(data_retail['month'] <= month) & (data_retail['segment'] == 'B') & (data_retail['bodytype'] == 'SUV')]
p12_ll = pd.DataFrame(p12_dataset.groupby(['year','subsubsegment'])['sales'].sum().unstack(0))
p12_ll_reset = p12_ll.reset_index(drop=False)
print(p12_ll_reset)
p12_ll_reset[2019] = p12_ll_reset[2019].apply(lambda x: format((x/retail_20190105),'.1%'))
p12_ll_reset[2020] = p12_ll_reset[2020].apply(lambda x: format((x/retail_20200105),'.1%'))
print(p12_ll_reset)

