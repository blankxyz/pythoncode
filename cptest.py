#coding:utf8
import requests
import re
import urllib2
import sys
import chardet
import time
reload(sys)
sys.setdefaultencoding('utf8')
import Tkinter
from ScrolledText import ScrolledText

root = Tkinter.Tk()
root.title('全媒声控数据收集')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()  # 布局
varl = Tkinter.StringVar()
printTxt = ''

web_name = '中国经营报'
baseurl = "http://www.cb.com.cn"
url = baseurl + "/fangdichan/"

req = urllib2.Request(url)
content = urllib2.urlopen(req).read()
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(content).get('encoding','utf-8')
html = content.decode(infoencode,'ignore').encode(typeEncode)
#print html

title = '未设置'
anthor = '未设置'
url = '未设置'
source = '未设置'
content = '未设置'
pub_time = '1970-1-1 0:0:0'
crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
keywords = '未设置'
description = '未设置'


def crawl_content(url1):
    req1 = urllib2.Request(url1)
    content1 = urllib2.urlopen(req1).read()
    html1 = content1.decode(infoencode, 'ignore').encode(typeEncode)
    return html1

reg = re.compile('<dt><a href="(.*?)" target="_blank" title=".*?">(.*?)</a></dt>')
regDetail = re.compile('<title>(.*?)</title>.*?<meta name="keywords" content="(.*?)">.*?<meta name="description" '
                       'content="(.*?)">.*?<div class="contentmes auto">(.*?)<span>(.*?)</span>.*?<i>'
                       '评论：<a href="#SOHUCS" id="changyan_count_unit">(.*?)</a>',re.S)
# print html
contents = re.findall(reg, html)
# print contents


def start():
    i = 0
    for link in contents:
        i = i+1
        url1 = baseurl+link[0]
        details = re.findall(regDetail, crawl_content(url1))
        printTxt = '=========== '+str(i)+' ===========\n'
        # print details
        # print details[0][0]
        # break
        # print 'web_name='+web_name
        printTxt = printTxt + 'title='+details[0][0]+'\n'
        printTxt = printTxt + 'url='+url1+'\n'
        printTxt = printTxt + 'source='+details[0][4]+'\n'
        # print 'content='+details[0][2]
        printTxt = printTxt + 'pub_time='+details[0][3].strip()+'\n'
        printTxt = printTxt + 'crawl_time='+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+'\n'
        printTxt = printTxt + 'keywords='+details[0][1]+'\n'
        printTxt = printTxt + 'description='+details[0][2]+'\n'
        text.insert(Tkinter.END, printTxt)
        # break
#print soup.get_text()


button = Tkinter.Button(root, text='开始爬取', font=('微软雅黑', 10), command = start)
button.grid()


label = Tkinter.Label(root, font=('微软雅黑', 10), fg='blue', textvariable = varl)
label.grid()
varl.set('爬虫已准备...')
root.mainloop()  # 进入主事件循环