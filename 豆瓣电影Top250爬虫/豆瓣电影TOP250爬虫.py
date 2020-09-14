import urllib.request

import openpyxl
import requests
import bs4


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    res=requests.get(url,headers=headers)
    return res



def find_movies(res):
    soup=bs4.BeautifulSoup(res.text,'html.parser')

    # 电影名
    movies=[]
    movie_targets=soup.find_all('div',class_='hd')
    for movie in movie_targets:
        movies.append(movie.span.text)

    # 评分
    stars=[]
    star_targets=soup.find_all('span',class_='rating_num')
    for star in star_targets:
        stars.append(star.text)

    # 资料
    messages=[]
    message_targets=soup.find_all('div',class_='bd')

    for message in message_targets:
        try:
            messages.append((message.p.text.split('\n')[1].strip()+message.p.text.split('\n')[2].strip()))
        except:
            continue

    # 合并电影名，评分，资料
    result=[]
    for i in range(len(movies)):
        result.append((movies[i],stars[i],messages[i]))
    return result

def find_depth(res):
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    depth_targets=soup.find('span',class_='next').previous_sibling.previous_sibling.text
    return int(depth_targets)


def to_excel(data):
    wb=openpyxl.Workbook()
    wb.guess_types=True
    ws=wb.active
    ws.append(['电影名','评分','简介'])
    for each in data:
        ws.append(each)
    wb.save('D:\Directory\豆瓣TOP250电影.xlsx')

def main():
    host = 'https://movie.douban.com/top250'
    res = open_url(host)
    movie_result = []
    for i in range(find_depth(res)):
        host = 'https://movie.douban.com/top250'+'?start='+str(25*i)
        res = open_url(host)
        movie_result=find_movies(res)
    to_excel(movie_result)


if __name__ == '__main__':
    main()




