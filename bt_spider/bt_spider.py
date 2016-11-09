import requests
from lxml import etree

class BtSpider:
  def get_urls(self):
    urls = []
    for i in range(1, 10):
      urls.append("http://www.bttiantang.org/index-"+str(i)+".html")
    return urls

  def html_page_source(self, url):
    return requests.get(url).text

  def get_btn_item(self, html_page):
    return
if __name__=="__main__":
  bt_spider = BtSpider()
  for url in bt_spider.get_urls():
    print(bt_spider.html_page_source(url))
