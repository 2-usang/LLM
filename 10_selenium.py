# 네이버웹툰 댓글 크롤링
# 주소 : https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon')
soup = BeautifulSoup(driver.page_source)        # page_source로 selenium으로 가져온 url을 beautifulsoup에 넣어줌
comment_area = soup.find_all('span', {'class':'u_cbox_contents'})
print('***********베스트댓글**********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-'*30)

# /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]
driver.find_element('xpath','/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]').click()
time.sleep(2)
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span', {'class':'u_cbox_contents'})
print('***********전체댓글**********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-'*30)
time.sleep(10)