import requests
from lxml import etree

# base_url = "http://www.cd120.com/findDoctorListByRegService.jspx?regCode=33"
# html = requests.get(base_url)
f = open('huaxi_html.txt', 'r', encoding='utf-8')
html = f.read()
f.close()

selector = etree.HTML(html)
doctors = selector.xpath("//tr[@id='ret']")
for doctor in doctors:
  print("-----------", doctor.xpath("td[2]/span/a/i/text()")[0])
