from flask import Flask, render_template
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime, timedelta
import requests
import com
import question
import db
import distance
import re

printt = []

def run_html(result):
    anwser = []
    app = Flask(__name__)
    @app.route('/')

    def home():
        anwser.append(result)
        return render_template('home.html', anwser=anwser)
    if __name__ == '__main__':
        app.run(debug=True)

def day(ask_text): #날짜 출력
    if "내일" in ask_text:
        data = datetime.now() + timedelta(days=1)  #현재날짜

    elif "오늘" in ask_text:
        data = datetime.now()  #현재날짜
    elif "모래" in ask_text:
         printt = "니 몸무게 생각좀 하고 물어봐라"
         return printt
    else:
        data = datetime.now()  #현재날짜
    today = data.strftime('%Y.%m.%d')
    return today

def food(today): #식단표 약간의 오류
    response = requests.get('http://cms.itc.ac.kr/site/inhatc/foodList.do?key=902', verify=False)
    response.raise_for_status()
    response.encoding='utf-8'
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다

    my_titles = soup.select(
                            'div > table > tbody > tr'
                            )
    for title in my_titles:
        if today in title.text:
            return title.text

def check(ask_text): #단어체크
   if "밥" in ask_text or "식단" in ask_text or "점심" in ask_text:
       today = day(ask_text)
       if today != "":
           a = food(today)
           printt = a

   elif "경쟁률" in ask_text or "지원현황" in ask_text:
       if "수시 1차" in ask_text or "수시1차" in ask_text:
          url = "http://addon.jinhakapply.com/RatioV1/RatioH/Ratio41260051.html"
          printt = "수시 1차"
          sub = com.subject_list(ask_text)
          com._find(url,sub)
       elif "수시 2차" in ask_text or "수시2차" in ask_text :
          url = "http://addon.jinhakapply.com/RatioV1/RatioH/Ratio41260061.html"
          printt = "수시 2차"
          sub = com.subject_list(ask_text)
          com._find(url,sub)
       elif "정시" in ask_text:
          url = "http://addon.jinhakapply.com/RatioV1/RatioH/Ratio41260071.html"
          printt = "정시"
          sub = com.subject_test(ask_text)
          com._find(url,sub)
       else:
           printt = "이해하지 못했습니다."
   elif "인천날씨" in ask_text or "날씨" in ask_text or "인천 날씨" in ask_text:
       if "인천날씨" in ask_text or "인천 날씨" in ask_text:
           db.weather()
       else:
           wtr = db.weather()
           printt = "인천날씨만 알려드립니다. \n인천날씨 : " + wtr
   else:
       try:
           near_list=[]
           text = parse.quote(ask_text) #인코딩
           q = question.Qestion_answer(text)

           for i in range(0, len(q)):
               a = distance.levenshtein(q[i], ask_text) # 가상 값 , 실제 값 비교
               near_list.append(a)

           num = min(near_list) #최소값 구하기

           if(a != num):
               number = near_list.index(num) + 1

           a = re.split('-', q[number])
           printt = a[0]

       except ZeroDivisionError as e:
           printt = e

   return printt
#---------------MAIN--------------------------

split_text = '내일 날씨 어때?'
result = check(split_text)
print(result)
run_html(result)
