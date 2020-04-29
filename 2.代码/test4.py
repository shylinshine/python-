import re


easy_words = ['the',"it's",'text','two','.' ,'of', 'to', 'and', 'in', 'a', 'is', 'were', 'was', 'you',
            'I', 'he', 'his', 'there', 'those', 'she', 'her', 'their',
            'that', '[a]', '[b]', '[c]', '[d]', 'them', 'or','for','as',
            'are','on','it','be','with','by','have','from','not','they',
            'more','but','an','at','we','has','can','this','your','which','will','many',',','us','english','now'
            'one','should','points)','________','________.','all','than','what',
            'people','if','been','its','new','our','would','part','may','some','i',
            'who','answer','when','most','so','section','no','into','do','only','first','i','him','her','she',
            'each','other','following','had','such','much','out','--','up','these','he','we','first','our','we','us',
            'even','how','directions:','use','because','(10','time','(15','[d].',
            '-','it.','[b],','[a],','however,','1','c','1.','2.','b','d','a','(10','()','【答案】',
            '2','12.','13.','29.','3.','4.','5.','6.','7.','8.','9.','10.','11.','14.','【解析】','【考点分析】',
            '15.']
#过滤简单词

txt=open(r'F:\vocabulary\v1.txt','r',encoding='utf8').read() 
txt= txt.lower()                    #将大写字母转换成小写字母
    
txt=re.sub(r'\d','',txt)                #去除数字
    
# txt=re.sub('^[a-z]+','',str(txt))
txt=re.findall(r'[a-z]+',str(txt))
save=''
for i in txt:
    save=save+'\n'+ i                                   
for ch in '!"@#$%^&*()+,-./:;<=>?@[]_`~{|}【(…“': #替换特殊字符
    save.replace(ch, ' ')
print(save)