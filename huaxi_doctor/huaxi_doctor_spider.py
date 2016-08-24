import requests
from lxml import etree

def urls():
    urls = []
    for i in [1, 2, 3, 4, 5]:
        urls.append("http://www.cd120.com/findDoctorListByRegService.jspx?pageNo="+str(i)+"&regCode=33")
    return urls

def get_html_source(url):
    return requests.get(url).text

def parse_html(html):
    selector = etree.HTML(html)
    doctors = selector.xpath("//tr[@id='ret']")
    i = 1
    for doctor in doctors:
      print(i, doctor.xpath("td[2]/span/a/i/text()")[0])
      i += 1

if __name__ == '__main__':
    url_collection = urls()
    for url in url_collection:
      parse_html(get_html_source(url))
