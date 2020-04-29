from bs4 import BeautifulSoup
import requests
url="https://movie.douban.com/top250"
res=requests.get(url)
print(res)
html=res.text
print(html)
movies_name=[]
mysoup=BeautifulSoup(html,'lxml')
movie_zone=mysoup.find('ol')
print(movie_zone)
movie_list=movie_zone.find_all('li')
for movie in movie_list:
    name=movie.find('span',attrs={'class':'title'}).gettext()
    movies_name.append(name)
print(movies_name)