from lxml import etree

html = '''
  <html>
    <head>
      <title>测试</title>
    </head>
    <body>
      <div id='content'>
        <ul id='useful'>
          <li>这是第一条</li>
          <li>这是第二条</li>
          <li>这是第三条</li>
        </ul>
        <ul id='useless'>
          <li>不需要的信息1</li>
          <li>不需要的信息2</li>
          <li>不需要的信息3</li>
        </ul>
        <div id='url'>
          <a href='http://www.baidu.com/'>百度</a>
          <a href='http://jd.com/' title='京东'>点我打开京东</a>
        </div>
      </div>
    </body>
  </html>
  '''
selector = etree.HTML(html)
# 提取文本信息
# content = selector.xpath('//ul[@id="useful"]/li/text()')
# for each in content:
#     print(each)

# 提取属性
link = selector.xpath('//a/@href')
for each in link:
    print(each)