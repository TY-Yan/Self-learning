# 目標:用selenium登入網頁版IG,搜尋關鍵字並下載圖片

# ChromeDriver下載網址
#  https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Explicit Waits功能
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import wget  #下載用, 亦可使用urlretrieve

# 本範例預設將ChromeDriver存至個人桌面, 可自行調整路徑
PATH = "C:/Users/user/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)

myID = input('輸入帳號: ')
myPassword = input('輸入密碼: ')
keyWord = input('輸入要搜尋的關鍵字: ')
page = input('搜尋幾頁: ')

driver.get("https://www.instagram.com/")

# 等待帳號密碼欄出現
username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

# 登入鍵
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

# 清除欄位, 避免預設值
username.clear()
password.clear()

username.send_keys(myID)
password.send_keys(myPassword)
login.click()
search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )

# 輸入欲搜尋的關鍵字, IG設定為要連按兩下enter
search.send_keys("#" + keyWord)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

# 等待頁面出現
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )

# 設定滾輪往下拉到底的次數, 本範例設定為要搜尋的頁數
for i in range(int(page)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# 建立以關鍵字為名之資料夾
path = os.path.join(keyWord)
os.mkdir(path)

# 用迴圈找出圖片連結, 並以wget進行下載
imgs = driver.find_elements_by_class_name("FFVAD")
count = 0
for img in imgs:
    save_as = os.path.join(path, keyWord + str(count) + ".jpg")
    # 參數為下載連結, 儲存路徑
    wget.download(img.get_attribute("src"), save_as)
    count += 1

time.sleep(3)
driver.quit()
