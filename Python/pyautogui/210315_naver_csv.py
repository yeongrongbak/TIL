import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

search = input('검색어를 입력하세요. : ')
url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = soup.select('.api_txt_lines.total_tit') # 가져오고 싶은 컨텐츠의 Class 확인

# for i in total:
#     print(i.text)
#     print(i.attrs['href'])
#     print()

searchList = [] # 빈 리스트 생성

for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp) # 빈 리스트 내에 text와 href 컨텐츠 append

# print(searchList[0]) 잘 가져왔는지 확인

f = open(f'{search}.csv', 'w', encoding='utf-8', newline='') # 검색어를 제목으로 하는 csv 파일을 생성
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)

f.close()
print('완료되었습니다.')