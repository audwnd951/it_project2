# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:35:52 2018

@author: STU
"""

from bs4 import BeautifulSoup     #BeautifulSoup 임포트
from selenium import webdriver     #셀레니움 임포트
from selenium.webdriver.common.keys import Keys     # 스크롤 내리기
import time

# 사이트 주소 : https://freemidi.org/
# 장르(genre) : pop, rock, hip-hop-rap, jazz, blues, classical, rnb-soul, bluegrass, country, christian-gospel, opera, folk, punk, disco 

driver = webdriver.Chrome("c:/python/chromedriver") # 드라이버 선택 후 파일 다운로드 경로 설정

def midi_crawling(genre,midifile_number=None):    # midi_crawling(장르선택, 받을 midifile 개수)
    driver.get('https://freemidi.org/genre-'+str(genre))     # midi 사이트 주소 + 장르선택
    driver.implicitly_wait(10)
    time.sleep(2) # 창 로딩 완료 될 시간
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    url1 = []     # 전체 url
    url2 = []     # 곡 다운로드 페이지 url
        
    print("url 복사 시작합니다 잠시만 기다려주세요^^")
    for i in soup.select("#mainContent > div > div > a[href]"):
                         url1.append("https://freemidi.org/"+i.attrs['href'])
                         
    for j in url1:      
        driver.get(j)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for k in soup.select("#mainContent > div > div > div > div > div > span > a[href]"):
            url2.append("https://freemidi.org/"+k.attrs['href'])
    print("url 복사가 완료되었습니다.")
    
    long = len(url2)    
    for z in url2[:midifile_number]:
        driver.get(z)
        driver.implicitly_wait(30)            
        driver.find_element_by_xpath('//*[@id="downloadmidi"]').click()     # 다운로드 클릭
        print('다운로드')
        long = long-1
        print(str(long)+'개 파일 남음')
    driver.close()
    

midi_crawling('rock',2)