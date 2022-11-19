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

@app.route('/ph/<key>')
def fetch_vidlink(key):
    vid_main_url = "https://www.saveporn.net/view_video.php?viewkey=" + key
    print(vid_main_url)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(vid_main_url)
    driver.implicitly_wait(1)
    vid_480_btn = driver.find_element(By.XPATH, "//*[@id='dtable']/table/tbody/tr[2]/td[3]/a").click()
    file = driver.window_handles[1]
    driver.switch_to.window(file)
    return(f'{driver.current_url}')
    driver.close()
  
if __name__ == "__main__":
        app.run()
