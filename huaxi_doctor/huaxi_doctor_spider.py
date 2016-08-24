import requests

base_url = "http://www.cd120.com/findDoctorListByRegService.jspx?regCode=33"
html = requests.get(base_url)
print("------------start crawl")
print(html.text)
