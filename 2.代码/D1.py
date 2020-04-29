import requests
url="https://www.baidu.com/"
reponse= requests.get(url)
reponse.encoding='utf8'
print(reponse.text)
print(reponse.status_code)