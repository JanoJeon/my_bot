# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:17:58 2018

@author: Adam
"""
import requests
from bs4 import BeautifulSoup

def Qestion(text): # 문의
    title_list = []
    days_list = []
    Matrix = []

    response = requests.get('https://cms.itc.ac.kr/site/inhatc/boardList.do?boardSeq=61&key=1436&category=&searchType=TITLE&searchKeyword='
                        + text, verify=False)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
    
    my_titles = soup.select('td[class=subject]')#div[class=tit3]인 애들만 선택해서 출력하
    my_days = soup.select('td[class=gray]')#div[class=gray]인 애들만 선택해서 출력하
        
    for title in my_titles:
        title_list.append(title.text.strip())

    for days in my_days:
        days_list.append(days.text.strip())

    for i in range(len(title_list)): #출력
        #print(title_list[i], days_list[i] + "\n")
        Matrix.append(title_list[i] + days_list[i])
        #print(Matrix[i])
    return Matrix

def Qestion_answer(text): # 문의  
    title_list = []
  
    response = requests.get('https://www.google.co.kr/search?ei=014qW82MOIu20ASC4qLwDA&q='
                        + text)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
    
    my_titles = soup.select('h3[class=r]')#div[class=tit3]인 애들만 선택해서 출력하
    
    for title, in my_titles:
        title_list.append(title.text.strip())

   # for i in range(len(title_list)): #출력
   #     Matrix.append(title_list[i] + days_list[i])
    
    return title_list