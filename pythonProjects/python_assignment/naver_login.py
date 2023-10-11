import random  # Add this at the beginning of your script
import getpass
import time  # Import the time module

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def human_like_send_keys(element, text, tab_after=False):
    # Initializes an instance of ActionChains tied to the driver.
    # ActionChains are used to automate low-level interactions.
    actions = ActionChains(driver)

    # Loop to iterate over each character in the provided text.
    for char in text:
        # Add an action to the actions chain that sends (types) a single character to the element.
        actions.send_keys(char)

        # Add a pause action with a random duration between 0.05 and 0.25 seconds.
        # This simulates the variable time intervals of human typing.
        actions.pause(random.uniform(0.05, 0.25))

    # Check if a TAB keypress should be simulated after entering the text.
    if tab_after:
        # Add an action to simulate pressing the TAB key.
        actions.send_keys(Keys.TAB)

    # Execute all the actions that have been added to the actions chain.
    actions.perform()


# Create an instance of Chrome Options.
chrome_options = Options()

# Set a fake user-agent value
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

# Add the "detach" experimental option to prevent the browser from closing.
chrome_options.add_experimental_option("detach", True)

# Use these lines to disable the "Chrome is being controlled by automated software" infobar.
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# Initialize the Chrome WebDriver with the desired options.
driver = webdriver.Chrome(options=chrome_options)

# Define the target URL.
url = "https://www.naver.com"

# Direct the WebDriver to open the specified URL.
driver.get(url)

# Adding delay to mimic real user interaction
time.sleep(3)

login_page_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
login_page_btn.click()

# Adding delay after the click
time.sleep(3)

user_id = 'zizon1434243'
user_pw = 'aaa'

user_id_input = driver.find_element(By.ID, "id")
user_pw_input = driver.find_element(By.ID, "pw")

# Add delays to make input appear more human-like
# Use our function to send the user ID and then press TAB
human_like_send_keys(user_id_input, user_id, tab_after=True)
time.sleep(1)
human_like_send_keys(user_pw_input, user_pw)
time.sleep(1)


login_btn = driver.find_element(By.XPATH, '//*[@id="log.login"]')
login_btn.click()
