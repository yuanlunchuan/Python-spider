import requests
from lxml import etree

class BtSpider:
  current_page = 1

  def get_urls(self):
    urls = []
    for i in range(1, 3):
      urls.append("http://www.bttiantang.org/index-"+str(i)+".html")
    return urls

  def html_page_source(self, url):
    return requests.get(url).text

  def get_btn_item(self, html_page):
    selector = etree.HTML(html_page)
    movies = selector.xpath("//div[@class='title']")
    for movie in movies:
      print(str(movie.xpath("p[1]/a/b/font")[0].xpath("string(.)"))+"  "+str(movie.xpath("p[1]/span/font/text()")[0]))

if __name__=="__main__":
  bt_spider = BtSpider()
  for url in bt_spider.get_urls():
    bt_spider.get_btn_item(bt_spider.html_page_source(url))
