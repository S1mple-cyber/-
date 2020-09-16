```
import random
import urllib.request

import re


def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    return html


def get_img(html):
    # p=r'src="([^"]+\.jpg)"'
    # p=r'<img[^>]*?(src="[^"]*?")[^>]*?>'
    p=r'img src="(.*?)"'
    img_list=re.findall(p,html)
    for each in img_list:
        print(each)
    return img_list

def save_img(img_list):
    for each in img_list:
        img_url='http:'+each
        filename='D:\\Pyhton\\code\小甲鱼\\爬虫\\伪装\\B站图片\\'+str(img_list.index(each))+'.jpg'
        # print(filename)
        with open(filename,'wb') as f:
            try:
                img = urllib.request.urlopen(img_url).read()
                f.write(img)
            except:
                continue

def main():
    url = "https://www.bilibili.com/"
    html = open_url(url)
    images=[]
    images=get_img(html)
    save_img(images)
    print(images)
if __name__ == '__main__':
    main()
```
b站的图片地址
![image](https://github.com/S1mple-cyber/Crawler-applet/blob/master/b站首页图片爬取/B站图片地址.jpg)
