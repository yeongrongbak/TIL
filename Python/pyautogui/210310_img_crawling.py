from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요:')
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find_all(class_='_image _listImage') # 현재 네이버의 url 내 class를 활용해서 크롤링 할 경우 진행이 안됨 (다른 방법 시도 필요)

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f: # Url을 불러와서 연다
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h: # 파일명 설정
            img =f.read()
            h.write(img)
    n += 1
    print(imgUrl)

print('다운로드 완료')