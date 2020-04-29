from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().chrome
}
request = Request(url, headers=headers)
# handler = ProxyHandler({"http": "username:password@ip:port"})
handler = ProxyHandler({"http": "398707160:j8inhg2g@120.27.224.41:16818"})
# handler = ProxyHandler({"http": "ip:port"})
handler = ProxyHandler({"http": "118.190.95.43:9001"})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
