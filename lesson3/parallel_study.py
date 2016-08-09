from multiprocessing.dummy import  Pool as ThreadPool
import requests
import time

def getsource(url):
    html = requests.get(url)

urls = []

for i in range(1, 21):
    newpage = 'http://www.qianfandu.com/major?page='+str(i)
    urls.append(newpage)

time1 = time.time()
for i in urls:
    print(i)
    getsource(i)
time2 = time.time()
print('单线程耗时： ', (time2-time1))

pool = ThreadPool(2)
time3 = time.time()
results = pool.map(getsource, urls)
pool.close()
pool.join()
time4 = time.time()
print('多线程爬虫： ', (time4-time3))