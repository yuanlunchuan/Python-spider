import re
import requests

class PornSpider(object):
    def get_all_link(self, base_link, total_page):
        links = []
        for i in range(total_page+1):
            links.append(re.sub('/videolist-50-\d+.html', '/videolist-50-%d.html'%i, base_link, re.S))
        return links

    def get_page_source(self, link):
        return requests.get(link).text

    def get_img_urls(self, source):
        img_urls = []
        images = re.search('<ul class="ml mlt mtw cl">(.*?)</ul>', source, re.S).group(1)
        image_list = re.findall('<li(.*?)</li>', images, re.S)
        for image_li in image_list:
            img_urls.append(re.findall('src="(.*?)" alt=', image_li, re.S))
        return img_urls

    def save_image(self, image_url, image_name):
        print("----------image_url: ", image_url+'.jpg')
        pic = requests.get(image_url+'.jpg')
        fp = open('assets\\' + str(image_name) + '.jpg', 'wb')
        fp.write(pic.content)
        fp.close()

if '__main__' == __name__:
    porn_spider = PornSpider()
    base_link = 'http://cangjige.ml/videolist-50-1.html'
    links = porn_spider.get_all_link(base_link, 1)
    i = 1
    for link in links:
        print('-------link: ', link)
        for img_url in porn_spider.get_img_urls(porn_spider.get_page_source(link)):
            i += 1
            porn_spider.save_image(img_url[0], i)

