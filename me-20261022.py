from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException, TimeoutException
)

RESULT_CSS = "section.time-result-section.active-result"
FROM_XPATH = ".//div[contains(@class,'from')]"
TO_XPATH   = ".//div[contains(@class,'to')]"


def result_ready(d):
    """結果區塊存在，且 .from 內已有文字才算載入完成"""
    try:
        sec = d.find_element(By.CSS_SELECTOR, RESULT_CSS)
        f = sec.find_element(By.XPATH, FROM_XPATH)
        return sec if f.text.strip() else False
    except (NoSuchElementException, StaleElementReferenceException):
        return False


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.thsrc.com.tw/")  # 以高鐵官網為例
wait = WebDriverWait(driver, 10)

try:
    # 1. 處理可能遮擋的 Cookie 或廣告彈窗
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))).click()

    # 2. 選擇起點站
    start_station = wait.until(EC.presence_of_element_located((By.ID, "select_location01")))
    Select(start_station).select_by_visible_text("台北")

    # 3. 選擇終點站
    end_station = driver.find_element(By.ID, "select_location02")
    Select(end_station).select_by_visible_text("左營")

    # 4. 點擊搜尋按鈕
    wait.until(EC.element_to_be_clickable((By.ID, "start-search"))).click()
    print("已送出查詢請求...")

    # 5. 用 wait.until 取代 time.sleep：等到結果內容真的有文字
    out = WebDriverWait(driver, 30, poll_frequency=0.5).until(result_ready)
    print("查詢結果已載入...")

    # 6. 從 out 內部使用相對 XPath 抓取
    from_station = out.find_element(By.XPATH, FROM_XPATH).text
    to_station = out.find_element(By.XPATH, TO_XPATH).text
    print(f"From: {from_station}, To: {to_station}")

    input("請按下 Enter 鍵以結束程式...")

except TimeoutException:
    print("執行出錯：等待逾時，請確認網頁是否載入或 selector 是否正確")
except Exception as e:
    print(f"執行出錯：{type(e).__name__}: {e}")
finally:
    driver.quit()
    
    
    
    
    