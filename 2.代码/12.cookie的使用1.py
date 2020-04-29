from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = " http://noa.gnnu.cn/sso/login"
headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": "JSESSIONID=aaaZMmdYhrC0J7j1l3ndx; __clusterSessionCookieName=1DD2DF55536938CE3A25004D4382C64A; ecology_JSessionId=aaaZMmdYhrC0J7j1l3ndx; __randcode__=7dfbd637-c6b2-45da-bfef-ab60e1680de4"
}
form_data = {
    "username": "180706037",
    "password": "210411",
    "lt": "LT-309082-Bbtny3k2BEWchIRapCogYV9F9aTmec",
    # "referer": "http://noa.gnnu.cn/spa/portal/static4mobilelogindev/index.html?message=311&appid=jeewx&service=http%3A%2F%2Fentrance.gnnu.cn%2Fweb%2Fcaslogin.jsp%3Bjsessionid%3D2DB8FCDD717E38907905920C3E0E14A4",
    "execution": "e1s1",
    "_eventId": "submit"


}
request = Request(url, headers=headers,data=form_data)
response = urlopen(request)

print(response.read().decode())
