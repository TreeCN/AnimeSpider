import scrapy
import re

from Anime.items import AnimeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#负责抓取网页数据的爬虫
class AnimeSpider(CrawlSpider):
  #爬虫名
	name = "Anime"

  #允许抓取的域
	allowed_domains = ["dmnico.cn"]

  #初始抓取URL
	start_urls = [
		"http://www.dmnico.cn/article/?aa3f8d5c14f17848ea25.html"
	]

  #抓取规则
	rules = (
		Rule(LinkExtractor(allow=(r'artttml/.*html')),callback='parse_item'),
	)

  #解析抓取的数据
	def parse_item(self, response):
		item = AnimeItem()
		item['AnimeName'] = re.split(r'\(|\[|\s', response.xpath(r'//title/text()').extract()[0])[0]
		item['AnimeEpisode'] = response.selector.re(r'<a.*?magnet.*?>([\s\S]*?)<\/a>')
		item['AnimeMagnet'] = response.selector.re(r'magnet:[?]xt=urn:btih:\w+')
		if item['AnimeMagnet'] != []:
			yield item
			return item
