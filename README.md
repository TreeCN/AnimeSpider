#动漫下载链接爬虫
***
>本代码只作学习交流，仅供个人研究之用，请支持正版版权<br>

##开发环境
[Ubuntu 14.04.4 LTS](http://www.ubuntu.org.cn/index_kylin)<br>
[Python 3.4.3 64-bit](https://www.python.org/)<br>
[MySQL 14.14](http://www.mysql.com/)<br>

##需要的库
[scrapy](http://scrapy.org/)<br>
Python开发的一个快速,高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。<br>

[pyMySql](https://github.com/PyMySQL/PyMySQL/)<br>
Python连接数据库并进行处理的模块。<br>

##使用说明
进入根目录，执行<br>
`$ scrapy crawl Anime`<br>
即可开始抓取，抓取完毕后，执行<br>
`$ python QueryAnime.py`<br>
输入需要查询的内容，会在当前目录下生成`result.txt`文件存放查询结果<br>

##文件说明
*/QueryAnime.py*<br>
连接数据库查询，并将查询结果写入文件。<br>

*/CreateTable.sql*<br>
创建数据库，并创建两个表。其中*name*表存储动漫标题, *info*表存储动漫的集数和连接。

*/Anime/items.py*<br>
说明需要抓取的数据项。

*/Anime/pipelines.py*<br>
抓取数据后的处理动作，在这里实现将数据写入数据库。

*/Anime/settings.py*<br>
爬虫设置文件，在这里可以设置爬虫速度。

*/Anime/spiders/AnimeSpider.py*<br>
爬虫文件，在这里写入爬虫规则。<br>

##待改进的部分
+ 界面采用GUI
+ 动漫查询支持模糊搜索
+ 抓取与查询的整合

##许可
本代码采用GPL协议，具体请参照GPL协议内容。