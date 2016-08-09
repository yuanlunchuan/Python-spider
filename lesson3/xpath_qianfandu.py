from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree

def spider(url):
    print(url)
    html_source = requests.get(url).text
    selector = etree.HTML(html_source)
    articles = selector.xpath('/html/body/div[1]/div[1]/div[3]/div[2]/article')
    item = {}
    for article in articles:
        item['title'] = article.xpath('div[2]/h3/a/text()')[0]
        item['comment-count'] = article.xpath('div[1]/div[2]/strong/text()')[0]
        item['view-count'] = article.xpath('div[1]/div[1]/strong/text()')[0]
        item['public-time'] = article.xpath('div[2]/address/div[@class="time"]/text()')[0]
        save_date(item)

def save_date(item):
    f = open('xpath_qianfandu.txt', 'a', encoding='utf-8')
    f.writelines('标题：'+item['title']+'\n')
    f.writelines('评论数量：'+item['comment-count']+'\n')
    f.writelines('浏览量: '+item['view-count']+'\n')
    f.writelines('发布时间: '+item['public-time']+'\n\n')
    f.close()

if __name__ == '__main__':
    pool = ThreadPool(2)
    links = []
    for i in range(1, 20):
        links.append('http://www.qianfandu.com/major?page='+str(i))
    pool.map(spider, links)
    pool.close()
    pool.join()

