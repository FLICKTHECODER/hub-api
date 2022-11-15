from flask import Flask
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


app = Flask(__name__)

@app.route("/bro")
def bruh():
  return "Hello"

@app.route('/ph')
def fetch_vidlink():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://www.saveporn.net/view_video.php?viewkey=ph602d29b697b36")
    driver.implicitly_wait(1)
    vid_480_btn = driver.find_element(By.XPATH, "//*[@id='dtable']/table/tbody/tr[2]/td[3]/a").click()
    driver.implicitly_wait(5)
    file = driver.window_handles[1]
    driver.switch_to.window(file)
    driver.implicitly_wait(3)
    click_to_dl_btn = driver.find_element(By.XPATH, "//*[@id='sddlbtn']").click()
    driver.implicitly_wait(6)
    return(f'{driver.current_url}')
  
if __name__ == "__main__":
        app.run()
