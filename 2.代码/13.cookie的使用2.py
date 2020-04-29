from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor,build_opener

# 登录
login_url = "http://noa.gnnu.cn/sso/login"
headers = {
    "User-Agent": UserAgent().chrome,
}
form_data = {
    "username": "180706037",
    "password": "210411",
    "lt": "LT-309082-Bbtny3k2BEWchIRapCogYV9F9aTmec",
    # "referer": "http://noa.gnnu.cn/spa/portal/static4mobilelogindev/index.html?message=311&appid=jeewx&service=http%3A%2F%2Fentrance.gnnu.cn%2Fweb%2Fcaslogin.jsp%3Bjsessionid%3D2DB8FCDD717E38907905920C3E0E14A4",
    "execution": "e1s1",
    "_eventId": "submit"


}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=f_data)
#response = urlopen(request) 错误的
handler = HTTPCookieProcessor()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
# print(response.text())
# 访问页面
info_url = " http://entrance.gnnu.cn/web/caslogin.jsp;jsessionid=2DB8FCDD717E38907905920C3E0E14A4?isRememberAccount_=&isRememberPassword_=&loginid_=180706037&up_=3a45726ce88d4b5253fed67d242ef150_random_"

request = Request(info_url, headers=headers)
response = urlopen(request)
response = opener.open(request)
print(response.read().decode())
