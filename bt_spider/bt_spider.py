import requests
from lxml import etree

class BtSpider:
  def get_urls(self):
    urls = []
    for i in range(1, 2):
      urls.append("http://www.bttiantang.org/index-"+str(i)+".html")
    return urls

  def html_page_source(self, url):
    return requests.get(url).text

  def get_btn_item(self, html_page):
    selector = etree.HTML(html_page)
    movies = selector.xpath("//div[@class='title']")
    for movie in movies:
      print("---------电影名称： "+str(movie.xpath("p[1]/a/b/font/text()")))

if __name__=="__main__":
  bt_spider = BtSpider()
  for url in bt_spider.get_urls():
    bt_spider.get_btn_item(bt_spider.html_page_source(url))
