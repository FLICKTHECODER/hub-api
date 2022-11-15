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

@app.route('/ph/<vid_url>')
def fetch_vidlink(vid_url):
    if "pornhub.com" in vid_url:
        vid_main_url = vid_url.replace("pornhub.com", "saveporn.net")
        print(vid_main_url)

    else:
        return "Not a valid url :("

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(vid_main_url)
    driver.implicitly_wait(2)
    vid_480_btn = driver.find_element(By.XPATH, "//*[@id='dtable']/table/tbody/tr[2]/td[3]/a").click()
    driver.implicitly_wait(3)
    file = driver.window_handles[1]
    driver.switch_to.window(file)
    driver.implicitly_wait(1)
    click_to_dl_btn = driver.find_element(By.XPATH, "//*[@id='sddlbtn']").click()
    driver.implicitly_wait(7)
    return(f'{driver.current_url}')
  
if __name__ == "__main__":
        app.run()
