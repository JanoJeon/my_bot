# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:34:20 2018

@author: Adam
"""
from bs4 import BeautifulSoup
#import pymysql
import requests

def Insert_Data():
    # MySQL Connection 연결
    conn = pymysql.connect(host='localhost', port=32768, user='root', password='test9131', db='chat')
    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    # SQL문 실행
    sql = "select * from word"
    curs.execute(sql)
    # 데이타 Fetch
    rows = curs.fetchall()
    print(rows)     # 전체 rows
    conn.close()


def weather():
    response = requests.get('https://search.daum.net/search?w=tot&DA=UMZ&t__nil_searchbox=suggest&sug=topex&sugo=16&sq=%EC%9D%B8%EC%B2%9C%EB%82%A0%EC%94%A8&o=1&q=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다

    my_titles = soup.select(
                            'div.coll_cont > div > div.wrap_region.today > div.cont_weather > div.cont_today > div.info_temp > div > span > span.desc_temp'
                            )
    for title in my_titles:
        s = title.text.strip()
#    print("인천날씨 : ",s)
    return s
