from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? :')
url = baseUrl + quote_plus(plusUrl)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:\\Users\\user\\python\\chromedriver.exe', options=options)
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')

x = soup.select('.yuRUbf') # 가져오고 싶은 컨텐츠를 포함하는 class를 찾아야 함
# print(type(g))
for i in x:
    print(i.select_one('.LC20lb.DKV0Md').text) # 사이트 제목 가져오기 (class 기준)
    print(i.a.attrs['href']) # 사이트 url 가져오기 (a 태그 기준)
    print()

driver.close()