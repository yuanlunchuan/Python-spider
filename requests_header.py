import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
html = requests.get('http://www.qianfandu.com', headers=headers)

school_list = re.search('<section class="colleges">(.*?)<div class="aside">', html.text, re.S).group(1)
articles = re.findall('<article>(.*?)</article>', school_list, re.S)

for article in articles:
    school_name = re.search('<h5>(.*?)</h5>', article, re.S).group(1)
    print(str(re.findall('">(.*?)</a>', school_name, re.S)[0]))
