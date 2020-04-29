# 1.实例化一个etree对象,且将待解析的页面源码数据加载到该对象中
# 2.调用etree对象中的xpath方法结合着不同的xpath表达式实现标签的定位和数据的提取


# 实例化一个etree对象
# 1.etree.parse("filename")   加载本地文档
# 2.etree.HTML(page-text)     加载网站获取的


# 如果最左侧以/   则要从根标签开始指定   //多个层级
import requests
import os
# from fake_useragent import UserAgent
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
dirName='girlslib'
if not os.path.exists(dirName):
    os.mkdir(dirName)
url='http://pic.netbian.com/4kmeinv/'
reponse=requests.get(url=url,headers=headers)
reponse.encoding='gbk'
page_text=reponse.text
tree=etree.HTML(page_text)
li_list=tree.xpath('//div[@class="slist"]//li')
for li in li_list:
    title=li.xpath('./a/img/@alt')[0]+'.jpg'    #局部数据解析./开头
    img_src='http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    img_data=requests.get(url=img_src,headers=headers).content
    imgPath=dirName +'/' +title
    with open(imgPath,'wb') as fp:
        fp.write(img_data)
    print(title,'保存成功!!!')

    #爬取多页的话
    # 先定义一个URL模版:不可变的
url='http://pic.netbian.com?4kmeinv/index_%d.html'
for page in range(1,6):
    if page==1:
        new_url='http://pic.netbian.com?4kmeinv/'
    else:
        new_url=formate(url%page)
    reponse=requests.get(url=new_url,headers=headers)   #向new_url发送请求
    reponse.encoding='gbk'
    page_text=response.text

    
    # 需要解析出携带html标签的局部数据
    # bs4在实现标签定位的时候返回的直接就是定位到标签的字符串数据
    # xpath如何才能更具有通用性
 