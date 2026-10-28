

# list1 = ["1", "2", "3"]
# print("".join(list1))

# import time

# start = time.time()
# for i in range(10):
#     print(i)
#     time.sleep(0.5)
# end = time.time()
# print(f"總共花費時間：{end - start} 秒")



# import requests

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
# }

# url = "https://www.thsrc.com.tw/"
# response = requests.get(url, headers=headers, verify=False)
# print(f"HTTP 狀態碼：{response.status_code}")

# with open("thsrc.html", "w", encoding="utf-8") as f:
#     f.write(response.text)
    

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome( )
driver.maximize_window()
driver.get("https://www.thsrc.com.tw/") # 以高鐵官網為例
wait = WebDriverWait(driver, 10)
try:
    # 1. 處理可能遮擋的 Cookie 或廣告彈窗
    clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))
    wait.until(clickable).click( ) #按下同意

    # 2. 定位並選擇起點站
    start_station = driver.find_element(By.ID, "select_location01")
    Select(start_station).select_by_visible_text("台北")
        
    # 3. 定位並選擇終點站
    end_station = driver.find_element(By.ID, "select_location02")
    Select(end_station).select_by_visible_text("左營")

    # 4. 點擊搜尋按鈕
    search_btn = driver.find_element(By.ID, "start-search")
    search_btn.click( )
    print("已送出查詢請求...")
    
    # 5. 確保 out 載入完成
    out = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.time-result-section.active-result")))
    print("查詢結果已載入...")

    # 6. 從 out 內部使用相對 XPath 抓取（注意開頭有小數點 .//）
    from_station = out.find_element(By.XPATH, ".//div[@class='from']").text
    to_station = out.find_element(By.XPATH, ".//div[@class='to']").text

    print(f"From: {from_station}, To: {to_station}")

    input("請按下 Enter 鍵以結束程式...")
except Exception as e:
    print(f"執行出錯：{type(e)}")
finally:
    driver.quit()

