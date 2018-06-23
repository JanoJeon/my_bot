# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:10:37 2018

@author: Adam
"""
import requests
import distance
import numpy as np
from bs4 import BeautifulSoup

def _find(url, _list): # 수시 1차 2차 정시
    title_list = []
    response = requests.get(url, verify=False)
    response.raise_for_status()
    response.encoding='utf-8'
    html = response.text
    #html = response.text
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다

    my_titles = soup.select('div[id=SelType' + _list +'] tr[onmouseover]') #div[class=tit3]인 애들만 선택해서 출력하

    for title in my_titles:
        title_list.append(title.text.strip().replace('\n', ' '))
    printt = title_list
    return printt
    #return Matrix

def subject_test(ask_text):
    near_list = []
    word_list =["일반 주간", "농어촌", "수급자", "일반 야간"]

    for i in range(0, len(word_list)):
        a = distance.levenshtein(word_list[i], ask_text) # 가상 값 , 실제 값 비교
        near_list.append(a)

    a = np.mean(near_list)
    num = min(near_list) #최소값 구하기

    if(a != num):
       number = near_list.index(num)

       if number == 0:
           return "4A"
       elif number == 1:
           return "4G"
       elif number == 2:
           return "4R"
       elif number == 3:
           return "4B"
    else:
       printt = "니 말 하나도 못 알아 듣겠다 임마"
       return printt

def subject_list(ask_text):
    near_list = []
    word_list =["영어 특기자","중국어 특기자", "일본어 특기자", "일반 주간","전문 주간","일반 야간", "전문 야간", "특기자", "농어촌", "수급자"]

    for i in range(0, len(word_list)):
        a = distance.levenshtein(word_list[i], ask_text) # 가상 값 , 실제 값 비교
        near_list.append(a)

    a = np.mean(near_list)
    num = min(near_list) #최소값 구하기

    if(a != num):
       number = near_list.index(num)

       if number == 0:
           return "4E"
       elif number == 1:
           return "4V"
       elif number == 2:
           return "4F"
       elif number == 3:
           return "4T"
       elif number == 4:
           return "4C"
       elif number == 5:
           return "4U"
       elif number == 6:
           return "4D"
       elif number == 7:
           return "4Z"
       elif number == 8:
           return "4G"
       elif number == 9:
           return "4R"

    else:
       printt = "니 말 하나도 못 알아 듣겠다 임마"
       return printt


def login(): # 로그인
    LOGIN_INFO = { 'userId': '201245053','password': '1055513'}
    with requests.Session() as s: #세션유지
          res = s.post('https://portal.inhatc.ac.kr/user/loginProcess.face', data=LOGIN_INFO)
          redirect_cookie = res.headers['Set-Cookie']
          redirect_url = res.headers['Location']
          headers = {"Cookie": redirect_cookie}
          s.get(redirect_url, headers=headers)
          print(req.text)
    '''
    with requests.Session() as s: #세션유지
        req = s.post('https://portal.inhatc.ac.kr/user/loginProcess.face', data=LOGIN_INFO)
        #cookie = response.headers.get('Set-Cookie')
        #sessionid = s.cookies.get('SESSIONID')
        print(req.text)
'''
