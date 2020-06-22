import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


class ProcessData:
    def __init__(self, source_data, writer,year, month, day):
        self.source_data = source_data
        self.year = year
        self.month = month
        self.day = day
        self.writer = writer

    def Process_init(self):
        # self.data = pd.read_csv(self.source_data, encoding="ANSI", dtype={'month': np.str})
        self.data = pd.read_csv(self.source_data, encoding="ANSI")
        self.data = pd.DataFrame(self.data)
        self.data['brand_indicator']=self.data['brand_indicator'].apply(lambda x: 'Premium' if x == 'Luxury' else x)
        self.data_retail = self.data[(self.data['year'] > self.year-2) & (self.data['WRstatus'] == 'R/R')]
        self.data_wholesale = self.data[(self.data['year'] > self.year-2) & (self.data['WRstatus'] == 'W/W')]

    def PrintData(self):
        print(self.data_retail)
        print(self.data_wholesale)
        print(self.data_retail['brand_indicator'].value_counts())
        print(self.retail_202005)
        print(self.retail_20200105)
        print(self.retail_yoy)
        print(self.retail_acc_yoy)

    def ProcessPage2(self):
        self.retail_202005 = self.data_retail[(self.data_retail['year'] == self.year) & (self.data_retail['month'] == self.month)]['sales'].sum()
        self.retail_20200105 = self.data_retail[(self.data_retail['year'] == self.year) & (self.data_retail['month'] <= self.month)]['sales'].sum()
        self.retail_201905 = self.data_retail[(self.data_retail['year'] == self.year-1) & (self.data_retail['month'] == self.month)]['sales'].sum()
        self.retail_20190105 = self.data_retail[(self.data_retail['year'] == self.year-1) & (self.data_retail['month'] <= self.month)]['sales'].sum()
        self.retail_yoy = format((self.retail_202005/self.retail_201905-1),'.1%')
        self.retail_acc_yoy = format((self.retail_20200105/self.retail_20190105-1),'.1%')

    def ProcessPage4(self):
        p1 = self.data_retail.groupby(['year', 'month'])['sales'].sum()
        p1.unstack(0).to_excel(writer, sheet_name='第一表')
        table = pd.pivot_table(self.data_retail, values='sales', index=['year'], columns=['month'], aggfunc=[np.sum], fill_value='')
        table.to_excel(writer, sheet_name='第二表')


if __name__ == '__main__':
    writer = pd.ExcelWriter('filename.xlsx')
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month-2
    day = datetime.datetime.now().day

    pp = ProcessData("salesdata.csv",writer,year,month,day)
    pp.Process_init()
    pp.ProcessPage2()
    pp.ProcessPage4()
    pp.PrintData()

    writer.save()
    writer.close()

