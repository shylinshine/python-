from selenium import webdriver
from lxml import etree
from time import sleep

url = 'https://search.jd.com/Search?keyword=mac&enc=utf-8&wq=mac&pvid=9862d03c24e741c6a58079d004f5aabf'

chrome = webdriver.Chrome()
chrome.get(url)

js = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js)
sleep(3)
html = chrome.page_source
e = etree.HTML(html)
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')

print(len(names))
for name, price in zip(names, prices):
    print(name.xpath('string(.)'), ":", price)
chrome.quit()