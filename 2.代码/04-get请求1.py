from urllib.request import Request, urlopen
from urllib.parse import quote

url = "https://www.baidu.com/s?wd={}".format(quote("尚学堂"))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}
request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())
