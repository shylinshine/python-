import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

main_url='http://www.shicimingju.com/book/sanguoyanyi.html'
page_text=requests.get(url=main_url,headers=headers).text
# print(page_text)
fp=open('./sanguo.txt','a',encoding='utf8')

soup=BeautifulSoup(page_text,'lxml')
a_list=soup.select('.book-mulu >ul >li >a')
for a in a_list:
    title=a.string
    detail_url='http://www.shicimingju.com'+a['href']

    page_text_detail=requests.get(url=detail_url,headers=headers).text
    soup=BeautifulSoup(page_text_detail,'lxml')
    div_tag=soup.find('div',class_='chapter_content')
    content=div_tag.text
    fp.write(title+':'+content+'\n')
    print(title,'保存成功!')
fp.close()