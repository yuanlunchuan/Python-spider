import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool

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
    for doctor in doctors:
      f = open('huaxi_doctor_result.txt', 'a', encoding='utf-8')
      f.writelines("医生名字: "+doctor.xpath("td[2]/span/a/i/text()")[0])
      f.writelines("    "+doctor.xpath("td[3]/span/text()")[0])
      f.writelines("    " + doctor.xpath("td[4]/span/em/text()")[0]+"\n")
      f.close()

if __name__ == '__main__':
    url_collection = urls()
    for url in url_collection:
      parse_html(get_html_source(url))
