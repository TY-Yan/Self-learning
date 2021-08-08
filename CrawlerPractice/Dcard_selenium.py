# 目標:用selenium打開Dcard網址, 搜尋關鍵字並印出所有標題

# ChromeDriver下載網址
#  https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Explicit Waits功能
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 本範例預設將ChromeDriver存至個人桌面, 可自行調整路徑
PATH = "C:/Users/user/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")
search.clear() # 清除欄位, 避免網頁帶有預設值
search.send_keys("工作")
search.send_keys(Keys.RETURN)

# 等待driver最多20秒, 直到class_name出現sc-3yr054-1
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
)

# 找出每個class_name, 用迴圈印出
titles = driver.find_elements_by_class_name("tgn9uw-3")
for title in titles:
    print(title.text)

link = driver.find_element_by_link_text("跟對方延後報到結果...怎麼辦")
link.click() # 點擊
driver.back() # 回上一頁
driver.forward() # 回下一頁

time.sleep(3)
driver.quit()
