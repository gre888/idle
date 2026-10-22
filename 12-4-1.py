
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.thsrc.com.tw/")

wait = WebDriverWait(driver, 10)

try:
    # 1. 處理可能出現的 Cookie 或彈出視窗
    try:
        clickable = EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".swal2-confirm")
        )
        wait.until(clickable).click()
        print("已按下彈窗確認按鈕")
    except TimeoutException:
        print("沒有出現需要確認的彈窗，繼續執行")

    # 2. 選擇起點站
    start_station = wait.until(
        EC.presence_of_element_located(
            (By.ID, "select_location01")
        )
    )
    Select(start_station).select_by_visible_text("台北")

    # 3. 選擇終點站
    end_station = driver.find_element(
        By.ID, "select_location02"
    )
    Select(end_station).select_by_visible_text("左營")

    # 4. 點擊搜尋按鈕
    search_btn = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "start-search")
        )
    )
    search_btn.click()

    print("已送出查詢請求...")

    # 5. 等待查詢結果
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "section.time-result-section.active-result")
        )
    )

    # 6. 取得查詢結果
    tickets = driver.find_elements(
        By.CSS_SELECTOR, "section.time-result-section.active-result"
    )

    print(f"找到的結果區塊數量：{len(tickets)}")

    for ticket in tickets:
        # 修正 XPath：contains(屬性, '文字')
        from_elements = ticket.find_elements(
            By.XPATH, ".//div[contains(@class, 'from')]"
        )
        to_elements = ticket.find_elements(
            By.XPATH, ".//div[contains(@class, 'to')]"
        )

        from_station = (
            from_elements[0].text if from_elements else "找不到起點"
        )
        to_station = (
            to_elements[0].text if to_elements else "找不到終點"
        )

        print(f"起點站：{from_station}，終點站：{to_station}")

    input("請按 Enter 鍵結束...")

except Exception as e:
    print(f"執行出錯：{type(e).__name__}")
    print(f"錯誤原因：{e}")

finally:
    driver.quit()
