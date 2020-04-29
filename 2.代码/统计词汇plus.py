import re


easy_words = ["it's",'text', 'were','dose',
            'there', 'those', 'their','great',
            'that', 'them','with','have','from','they',
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

#1.获取单词
EngTxt = getTxt()
# print(getTxt())


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
value_word= { k:v for k, v in counts.items() if v > 2 and v <21}       #筛选3到20的频次的单词
# print(value_word)

#4.转换格式，方便打印，将字典转换为列表
# print(counts)
countsList = list(counts.items())
value_list = list(value_word.items())



countsList.sort(key=lambda x:x[1], reverse=True)                            #按次数从大到小排序,列表用sort,字典用sorted,x表示遍历出来的每一个元组,1表示第二个元素
value_list.sort(key=lambda x:x[1],reverse=True)                            #
print(value_list)
#5.打印输出
for word,count in countsList:
    with open(r'F:\vocabulary\所有单词.txt','a+') as f:
        str1=word+' : '+str(count)+ '次'
        f.writelines(str1+'\n')
        f.close()
print('完成!')

for word,count in value_list:
    with open(r'F:\vocabulary\价值单词.txt','a+') as f:
        str1=word+' : '+str(count)+ '次'
        f.writelines(str1+'\n')
        f.close()
print('完成!')