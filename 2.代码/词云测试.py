#导入词云的包
from wordcloud import WordCloud
#导入matplotlib作图的包
import matplotlib.pyplot as plt
import re


easy_words = ["it's",'text', 'were','does','about','also','questions','says','said','then','like','years','year','there','they','much','very','need',
            'there', 'those', 'their','could','since','being','take','just','words','great','long','where','hours','three',
            'that', 'them','with','have','from','they','four',
            'more','this','your','which','will','many','english','should','points','than','what',
            'people','been','its','would','part','some','answer','when','most','section','into','only','first',
            'each','other','following','such','much','these','first',
            'even','directions','because','however']
#过滤简单词
def getTxt():
    path=input('请输入路径名:\n')
    txt=open(path,'r',encoding='utf8').read() 
    txt= txt.lower()                    #将大写字母转换成小写字母,比较重要的一步
    txt=re.findall(r'[a-z]+',str(txt))       #匹配出英文单词小写,返回的是一个列表类型
    save=''                                 #定义空字符串用来接收列表中的数据
    for i in txt:
        save=save+'\n'+i      
    return save
EngTxt = getTxt()

#2.切割为列表格式
txtArr = EngTxt.split()
#3.遍历统计
counts = {}
for word in txtArr:
    flag=True
    for word1 in easy_words:
        if word==word1:
            flag=False
        else:
            continue
    if flag is True and len(word) > 3 and len(word) <=9:                    #过滤掉小于3的一些词,如介词,代词无参考价值
        counts[word] = counts.get(word, 0) + 1
    else:
        continue
print(counts)


#生成一个词云对象
wordcloud = WordCloud(
        background_color="white", #设置背景为白色，默认为黑色
        width=1500,              #设置图片的宽度
        height=960,              #设置图片的高度
        margin=10               #设置图片的边缘
        ).fit_words(counts)
# 绘制图片
plt.imshow(wordcloud)
# 消除坐标轴
plt.axis("off")
# 展示图片
plt.show()
# 保存图片
wordcloud.to_file('my_test3.png')
