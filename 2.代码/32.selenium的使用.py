from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('http://www.baidu.com')
# chrome.save_screenshot('bjsxt.png')
html = chrome.page_source
print(html)
chrome.quit()