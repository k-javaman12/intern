import getpass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create an instance of Chrome Options.
chrome_options = Options()

# Add the "detach" experimental option to prevent the browser from closing.
chrome_options.add_experimental_option("detach", True)

# Add the option to disable the info bar.
# If the above method doesn't work for newer versions,
# there's no official way to remove the notification.
# It's intended as a security feature to let users know that the browser is being controlled programmatically.
chrome_options.add_argument("--disable-infobars")

# Initialize the Chrome WebDriver with the desired options.
driver = webdriver.Chrome(options=chrome_options)

# Define the target URL.
url = "https://www.naver.com"

# Direct the WebDriver to open the specified URL.
driver.get(url)

login_page_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
login_page_btn.click()

user_id = input('아이디 입력')
user_pw = getpass.getpass('비밀번호 입력')

user_id_input = driver.find_element(By.ID, "id")
user_id_input = driver.find_element(By.ID, "pw")

user_id_input.send_keys(user_id)
user_id_input.send_keys(user_pw)

login_btn = driver.find_element(By.XPATH, )



