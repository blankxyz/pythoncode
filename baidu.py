__author__ = '������ľ��'
# -*- coding: utf-8 -*-
#�ɼ�SERP�����������
import urllib2
from bs4 import BeautifulSoup
import time
#д�ļ�
def WriteFile(fileName,content):
    try:
        fp = file(fileName,"a+")
        fp.write(content + "\r")
        fp.close()
    except:
        pass

#��ȡHtmlԴ��
def GetHtml(url):
    try:
        req = urllib2.Request(url)
        response= urllib2.urlopen(req,None,3)#���ó�ʱʱ��
        data    = response.read().decode('utf-8','ignore')
    except:pass
    return data

#��ȡ�������SERP�ı���
def FetchTitle(html):
    try:
        soup = BeautifulSoup(''.join(html))
        for i in soup.findAll("h3"):
            title = i.text.encode("utf-8")������������ 
��������������if any(str_ in title for str_ in ("����","����")):
����������������  continue
            else:
                print title
            WriteFile("Result.txt",title)
    except:
        pass

keyword = "58ͬ��"
if __name__ == "__main__":
    global keyword
    start = time.time()
    for i in range(0,8):
        url = "http://www.baidu.com/s?wd=intitle:"+keyword+"&rn=100&pn="+str(i*100)
        html = GetHtml(url)
        FetchTitle(html)
        time.sleep(1)
    c = time.time() - start
    print('�������к�ʱ:%0.2f ��'%(c))
