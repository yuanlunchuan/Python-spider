import requests

html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')

print(html.text)
