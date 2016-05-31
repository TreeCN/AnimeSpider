# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import pymysql

#抓取的数据存入数据库
class AnimePipeline(object):

  #连接数据库
	def __init__(self):
		self.dbpool = pymysql.connect(
			host = 'localhost',
			user = 'root',
			passwd = '****',
			db = 'ANIME',
			charset = 'utf8'
		)
		self.cur = self.dbpool.cursor()

  #存入数据库
	def process_item(self, item, spider):
		InsertData = 'INSERT INTO name(AnimeTitle) VALUES ("' + str(item['AnimeName']) + '")'
		sta = self.cur.execute(InsertData)

		SelectData = 'SELECT AnimeID FROM name where AnimeTitle = "' + str(item['AnimeName']) + '"'
		self.cur.execute(SelectData)

		AnimeID = 0
		for i in self.cur:
			AnimeID = str(i[0])

		for (episode, magnet) in zip(item['AnimeEpisode'], item['AnimeMagnet']):
			InsertData = 'INSERT INTO info(AnimeID, AnimeEpisode, AnimeMagnet) VALUES (' + str(AnimeID) + ', "' + str(episode) + '", "' + str(magnet) + '")'
			sta = self.cur.execute(InsertData)

		self.dbpool.commit()
		return item
