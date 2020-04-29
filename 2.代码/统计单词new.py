import re
txt= open(r"F:\vocabulary\v1.txt",encoding="utf-8").read().split()
print(txt)

words=[i.lower() for i in re.findall('[a-zA-Z]+',str(txt)) if len(i) > 2]
d= dict()
common_word=['']     #常见的过滤
for word in words:
    if word not in common_word:
        d[word]=d.get(word,0) + 1      #获取key的值,默认为0
        data=sorted(d.items(),key=lambda x: x[1], reverse=True)
print(data)