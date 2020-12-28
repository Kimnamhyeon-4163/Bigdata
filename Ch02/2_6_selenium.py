"""
날짜 : 2020/12/28
이름 : 김남현
내용 :
"""
from selenium import webdriver

# 크롬 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 접속
browser.get('https://naver.com')

# 로그인버튼 클릭
a_login = browser.find_element_by_css_selector('#account > a')
a_login.click()

# 아이디, 비밀번호 저장

input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')

input_id.send_keys('abcd')
input_pw.send_keys('1234')


input_submit = browser.find_element_by_id('log.login')
input_submit.click()