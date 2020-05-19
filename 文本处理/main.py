import functools
import re
import numpy as np
import matplotlib.pyplot as plt
#定义单词的类
class book_node:
    def __init__(self,word,cnt):
        self.word = word
        self.cnt = cnt
def cmp(self,s):
        if self.cnt < s.cnt: 
            return 1
        elif self.cnt > s.cnt:
            return -1
        else:
            return 0
def __main__():
    In = open('book.txt','r',encoding='utf-8')
    out = open('out.txt','w',encoding='utf-8')
    S = In.read()
    f = list(S)
#去除所有非字母元素I
    for i in range(len(f)):
        if f[i].isalpha():
            pass
        else:
            f[i] = ' '
        i = i+1
        
    f = ''.join(f)
    temp = f.split()
    book = []
    cnt = []
    dict_book = []
    #统计词频
    for i in temp:
        now = i.lower()
        if now in book:
            cnt[book.index(now)] += 1
        else:
            book.append(now)
            cnt.append(1)
    #将单词信息存进列表

    for i in range(len (book)):
        dict_book.append(book_node(book[i],cnt[i]))
    #按词频排序
    dict_book.sort(key = functools.cmp_to_key(cmp))
    #将单词及词频输出到out.txt中（避免在终端中输出过慢）
    for i in dict_book:
        out.write(i.word+" "+str(i.cnt)+'\n')
    
    #验证zipf-law
    y = sorted(cnt)
    y.reverse()
    x = []
    for i in range(len(y)):
        x.append(i+1)
    plot1 = plt.plot(x, y, 's',label='original values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4) #指定legend的位置右下角
    plt.title('Zipf-law')
    plt.show()

    #正则表达式实验
    #匹配文章中的所有年份
    pa = re.compile(r'\b\d\d\d\d\b')
    ans = pa.findall(S)
    print(ans)
if __name__ == "__main__":
    __main__()