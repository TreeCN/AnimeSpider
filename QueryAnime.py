# -*- coding:utf8 -*-

import pymysql

#连接数据库
dbpool = pymysql.connect(
			host = 'localhost',
			user = 'root',
			passwd = '*****',
			db = 'ANIME',
			charset = 'utf8'
)

cur = dbpool.cursor()

QueryStr = input('请输入要查询的动漫名: ')

#查询数据库
SelectData = 'SELECT AnimeTitle, AnimeEpisode, AnimeMagnet FROM name, info where AnimeTitle = "' + QueryStr + '" and name.AnimeID = info.AnimeID'
cur.execute(SelectData)

#写入文件
with open("result.txt", "w") as f:
	f.write(QueryStr + ':\n')
	for item in cur:
		f.write(str(item[1]) + ' ' + str(item[2]) + '\n')

cur.close()
dbpool.close()
