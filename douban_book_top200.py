"""
功能：导出豆瓣读书评分排行top200的名著
作者：李雅婷
日期：2022-08-06
"""

import requests
from lxml import etree
import xlwt


def get_books(num):
    url = "https://book.douban.com/tag/%E5%90%8D%E8%91%97"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    html = requests.get(url + f'?start={str(num * 20)}&type=S', headers=headers)
    html = etree.HTML(html.text)

    # 获取图书列表
    books = html.xpath('//*[@id="subject_list"]/ul/li')

    for book in books:
        book_name = book.xpath('.//div[2]/h2/a/text()')[0].strip()
        book_info = book.xpath('.//div[2]/div[1]/text()')[0].strip()
        book_inq = book.xpath('.//div[2]/p/text()')
        book_inq = '' if not book_inq else book_inq[0].strip().replace("\n", "")
        print(f'书名：{book_name} | 出版信息：{book_info} | 简介：{book_inq}')

        global n
        sheet.write(n, 0, book_name)
        sheet.write(n, 1, book_info)
        sheet.write(n, 2, book_inq)
        n += 1


if __name__ == '__main__':
    excel_book = xlwt.Workbook(encoding='utf-8')
    sheet = excel_book.add_sheet('豆瓣图书top200')
    sheet.write(0, 0, '书名')
    sheet.write(0, 1, '出版信息')
    sheet.write(0, 2, '简介')
    n = 1

    for i in range(10):
        get_books(i)
    excel_book.save(u'豆瓣图书top200.xlsx')
