
### 作业

Action1：汽车投诉信息采集：

数据源：http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml

投诉编号，投诉品牌，投诉车系，投诉车型，问题简述，典型问题，投诉时间，投诉状态

可以采用Python爬虫，或者第三方可视化工具

![image-20200622133536388](.\img\image-20200622133536388.png)

##### 方案一：采用现成的爬虫采集器（本方案采用UI Path），完成网页抓取

相关的流程图设计如下：

![image-20200622133950130](.\img\image-20200622133950130.png)



##### 方案二：采用成熟的爬虫框架Scrapy，进行数据的抓取。



##### 方案三：采用requests和beautifulsoup等第三方库工具，进行数据的抓取。