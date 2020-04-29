from urllib.request import urlopen

url = "http://www.baidu.com"
# 发送请求
response = urlopen(url)
# 读取内容
info = response.read()
# if response.status_code==200:
    # print("got it")
# else:
    # print("fail")
# 打印内容
print(info.decode())

# 打印状态码
# print(response.getcode())
# # 打印真实url
# print(response.geturl())
# # 打印响应头
# print(response.info())
