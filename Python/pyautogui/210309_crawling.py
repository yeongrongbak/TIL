import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
plusUrl = input('검색어를 입력하세요:')
url = baseUrl + urllib.parse.quote_plus(plusUrl) # urllib.parse.quote_plus 는 한글을 코드화 해주는 것 때문에 필요함

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_txt_lines total_tit') # 특정 class를 가진 것들을 모두 불러온다

for i in title:
    # print(i.attrs['title']) # 제목을 가져온다 (지금은 ui가 바뀌어서 이 방법으로 안되는 듯 함)
    print(i.attrs['href']) # 주소를 가져온다
    print() # 공백