import requests
from lxml import etree
from pymongo import MongoClient

class BtSpider:
  current_page = 1
  client = MongoClient("localhost", 27017)

  def __init__(self):
    self.db = self.client.bt_sources
    self.collection = self.db.bts

  def get_urls(self):
    urls = []
    for i in range(1, 100):
      print("----------page: "+str(i))
      urls.append("http://www.bttiantang.org/index-"+str(i)+".html")
    return urls

  def html_page_source(self, url):
    return requests.get(url).text

  def get_btn_item(self, html_page):
    selector = etree.HTML(html_page)
    movies = selector.xpath("//div[@class='title']")
    for movie in movies:
      movie_name = str(movie.xpath("p[1]/a/b/font")[0].xpath("string(.)"))
      movie_time = str(movie.xpath("p[1]/span/font/text()")[0])
      alis_name = str(movie.xpath("p[2]/a/text()"))
      score = str(movie.xpath("p[4]/strong/text()"))

      self.collection.insert({'movie_name': movie_name, 'movie_time': movie_time, 'alis_name': alis_name, 'score': score})

if __name__=="__main__":
  bt_spider = BtSpider()
  for url in bt_spider.get_urls():
    bt_spider.get_btn_item(bt_spider.html_page_source(url))
