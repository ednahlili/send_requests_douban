"""
AUTHOR:LIYATING
DATE:2022-08-06
DESCRIPTION:爬取豆瓣电影top250
"""

import os
from lxml import etree
import requests
import xlwt

url = 'https://movie.douban.com/top250'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36 '
}


def get_imgs(num):
    # 获取url页面的源码文件
    html = requests.get(url+f'?start={str(num*25)}&filter=', headers=headers).text
    # 将字符串格式的HTML对象，解析成Element对象，方便使用xpath等方法
    html = etree.HTML(html)
    # 获取第一页所有图片的链接
    img_urls = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src')

    # 获取图片
    if not os.path.exists('./豆瓣电影图片'):
        os.mkdir('./豆瓣电影图片')
    for item in img_urls:
        # 获取图片内容
        content = requests.get(item, headers=headers).content
        # 获取图片名称
        fn = item.split('/')[-1]
        # 将图片内容写入这个文件
        with open('./豆瓣电影图片/' + fn, 'wb') as f:
            f.write(content)


def get_movie_content(num):
    # 获取url页面的源码文件
    html = requests.get(url+f'?start={str(num*25)}&filter=', headers=headers).text
    # 将字符串格式的HTML对象，解析成Element对象，方便使用xpath等方法
    html = etree.HTML(html)

    # 获取电影标签列表
    movies = html.xpath('//ol[contains(@class,"grid_view")]/li')
    print(movies)

    # 根据标签列表进一步解析出评分、导演等信息
    for movie in movies:
        movie_title = movie.xpath('.//span[contains(@class,"title")][1]/text()')[0]
        movie_author = movie.xpath('./div/div[2]/div[2]/p[1]/text()')[0].strip()
        movie_score = movie.xpath('.//span[contains(@class,"rating_num")][1]/text()')[0]
        movie_index = movie.xpath('./div/div[1]/em/text()')[0]
        movie_inq = movie.xpath('.//span[contains(@class, "inq")]/text()')
        # 处理简介为空的情况
        movie_inq = '' if not movie_inq else movie_inq[0]
        print(f'电影名:{movie_title} | 评分:{movie_score} | 排名:{movie_index} | 简介:{movie_inq} | 主创:{movie_author}')

        # 将内容保存到excel表
        # 使用全局变量
        global n
        sheet.write(n, 0, movie_index)
        sheet.write(n, 1, movie_title)
        sheet.write(n, 2, movie_score)
        sheet.write(n, 3, movie_inq)
        sheet.write(n, 4, movie_author)
        n+=1


if __name__ == '__main__':
    # 创建一个excel工作簿
    book = xlwt.Workbook(encoding='utf-8')
    # 为book添加sheet
    sheet = book.add_sheet('豆瓣电影top250')

    # 全局变量
    n = 1

    # 写表头
    sheet.write(0, 0, '排名')
    sheet.write(0, 1, '名称')
    sheet.write(0, 2, '评分')
    sheet.write(0, 3, '简介')
    sheet.write(0, 4, '主创')

    for i in range (10):
        # get_imgs(i)
        get_movie_content(i)

    book.save(u'豆瓣top250.xlsx')

