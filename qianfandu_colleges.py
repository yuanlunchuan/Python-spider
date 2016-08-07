import requests
import re

class Spider(object):

    def __init__(self):
         print('start crawl ')

    def get_all_link(self, url, totalPage):
        all_link = []
        for i in range(1,totalPage+1):
          new_link = re.sub('page=\d+', 'page=%d'%i, url, re.S)
          all_link.append(new_link)
        return  all_link

    def get_source(self, url):
        return requests.get(url).text

    def get_school_list(self, source):
        scholl_list = re.search('<ul class="school-list">(.*?)<nav class="pagination">', source, re.S).group(1)
        return re.findall('<li>(.*?)</li>', scholl_list, re.S)

    def school(self, source):
        item = {}
        item['school_name'] = re.search('<h4><a target="_blank" href="(.*?)">(.*?)</a></h4>', source, re.S).group(2)
        item['school_address'] = re.search('<span>(.*?)</i>(.*?)</span>', source, re.S).group(2)
        spans = re.findall('<span>(.*?)</span>', source, re.S)
        item['school_range'] = re.search('<em>(.*?)</em>', spans[1], re.S).group(1)
        item['accept_rate'] = re.search('<em>(.*?)</em>', spans[2], re.S).group(1)
        item['fee'] = re.search('<em>(.*?)</em>', spans[3], re.S).group(1)
        item['total_watch'] = re.search('<em>(.*?)</em>', spans[4], re.S).group(1)
        return item

    def save_school(self, colleges):
        f = open('qianfandu_colleges.txt', 'a', encoding='utf-8')
        for college in colleges:
            f.writelines('school_name: '+college['school_name']+'\n')
            f.writelines('school_address: ' + college['school_address'] + '\n')
            f.writelines('school_range: ' + college['school_range'] + '\n')
            f.writelines('accept_rate: ' + college['accept_rate'] + '\n')
            f.writelines('fee: ' + college['fee'] + '\n')
            f.writelines('total_watch: ' + college['total_watch'] + '\n\n\n')
        f.close()

if __name__ == '__main__':
    colleges = []
    qianfandu_spider = Spider()
    url = 'http://www.qianfandu.com/colleges?page=1'
    all_link = qianfandu_spider.get_all_link(url, 20)
    for link in all_link:
        print('正在爬取： %s', link)
        html = qianfandu_spider.get_source(link)
        schools_list = qianfandu_spider.get_school_list(html)
        for schools_item in schools_list:
            colleges.append(qianfandu_spider.school(schools_item))
        qianfandu_spider.save_school(colleges)




