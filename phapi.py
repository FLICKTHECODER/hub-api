from flask import Flask
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route("/")
def check():
  return "I'm alive"

@app.route("/bro")
def bruh():
  return "Hello"

@app.route('/ph/<key>')
def fetch_vidlink(key):
    if "ph" in key:
      chrome_options = Options()  
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
      driver = webdriver.Chrome(options=chrome_options)
      driver.get("https://9xbuddy.in/process?url=https://www.pornhub.com/view_video.php?viewkey=" + key)
      driver.maximize_window()
      driver.implicitly_wait(10)
      driver.execute_script("window.scrollTo(0, 1300)")
      dm = driver.find_elements(By.XPATH, f"//span[contains(text(), 'Download Now')]")[1].click()
      file = driver.window_handles[0]
      driver.switch_to.window(file)
      return driver.current_url
    else:
      return "Not a valid hub video viewkey :("
  
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=random.randint(2000, 9000))
  
