import re
import requests

f = open('douban_source.txt', 'r', encoding="utf-8")
html = f.read()
f.close()

result_list = re.search('<div class="result-list">(.*?)result-list-ft">', html, re.S).group(1)
img_list = re.findall('<img src="(.*?)"', result_list, re.S)
i = 0
for img_item in img_list:
  print('now downloading: '+img_item)
  pic = requests.get(img_item)
  fp = open('pic\\'+str(i)+'.jpg', 'wb')
  fp.write(pic.content)
  fp.close()
  i += 1
