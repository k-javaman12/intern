import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def to_video_click():
    to_video_btn = driver.find_element(By.XPATH, '//*[@id="itemlist"]/li/a')
    to_video_btn.click()
    # Adding delay after the click
    time.sleep(3)

def close():
    # Navigate back twice to return to the previous page (since you clicked twice to get to the video)
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)

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
url = "https://kms.ggc.go.kr/caster/content/vms/stdcommitteeVod.do?confcode=C001&daesu=11"

# Direct the WebDriver to open the specified URL.
driver.get(url)

# Adding delay to mimic real user interaction
time.sleep(3)

# Define the committee names
committees = [
    "assemblyOperationCommittee",
    "planningFinanceCommittee",
    "economyLaborCommittee",
    "safetyAdministrationCommittee",
    "cultureSportsTourismCommittee",
    "agricultureMarineCommittee",
    "healthWelfareCommittee",
    "constructionTransportCommittee",
    "urbanEnvironmentCommittee",
    "womenFamilyLifelongEducationCommittee",
    "educationPlanningCommittee",
    "educationAdministrationCommittee"
]

# Loop through each committee name and its index (starting from 1)
for idx, committee in enumerate(committees, start=1):
    btn_variable_name = committee + "_btn"
    xpath_str = f'//*[@id="codelist"]/li[{idx}]/a'

    # Use driver to find element and click
    parliament_btn = driver.find_element(By.XPATH, xpath_str)
    parliament_btn.click()

    # click the first meeting
    first_meeting_btn = driver.find_element(By.XPATH, '//*[@id="chalist"]/li[1]/a')
    first_meeting_btn.click()
    to_video_click()

    close()  # Close the video and return

    # click the second meeting
    second_meeting_btn = driver.find_element(By.XPATH, '//*[@id="chalist"]/li[2]/a')
    second_meeting_btn.click()
    to_video_click()

    close()  # Close the video and return

    # Adding delay after the click
    time.sleep(3)




