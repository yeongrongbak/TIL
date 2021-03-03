import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&nso=&where=blog&sm=tab_viw.all'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)

title = soup.find_all(class_='api_txt_lines total_tit') # 특정 class를 가진 것들을 모두 불러온다
# 비교 soup.find(class_='api_txt_lines') # 특정 class를 가진 것 하나만 불러온다

#print(title)

for i in title:
    # print(i.attrs['title']) # 제목을 가져온다 (지금은 ui가 바뀌어서 이 방법으로 안되는 듯 함)
    print(i.attrs['href']) # 주소를 가져온다
    print() # 공백


