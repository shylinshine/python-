import requests
url='http://t1.hxzdhn.com/uploads/tu/201910/9999/112e039ba1.jpg'
res=requests.get(url)
with open('mq.jpg','wb') as f:
    f.write(res.content)