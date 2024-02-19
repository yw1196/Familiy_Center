from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 웹 드라이버 초기화
driver = webdriver.Edge()  # Chrome 드라이버를 사용하고 있다고 가정합니다.

# 웹 페이지 열기
url = "https://www.daejeon.go.kr/okradmin/admLogin.do"
driver.get(url)