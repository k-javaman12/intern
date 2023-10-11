from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
options.add_argument('user-agent=' + user_agent)
URL = 'https://www.naver.com'
URL = 'https://www.daum.net'
browser = webdriver.Chrome()
browser.get(URL)


# user-agent
# https://hi-guten-tag.tistory.com/6

#account > div > a

browser.implicitly_wait(10)
