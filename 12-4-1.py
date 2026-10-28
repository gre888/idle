
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 1. 開啟 Chrome
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 30)

try:
    # 2. 開啟高鐵官網
    driver.get("https://www.thsrc.com.tw/")

    # 3. 處理可能出現的彈窗
    try:
        confirm_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".swal2-confirm")
            )
        )
        confirm_btn.click()
        print("已按下彈窗確認按鈕")

    except TimeoutException:
        print("沒有出現彈窗，繼續執行")

    # 4. 選擇起點站：台北
    start_station = wait.until(
        EC.presence_of_element_located(
            (By.ID, "select_location01")
        )
    )
    Select(start_station).select_by_visible_text("台北")

    # 5. 選擇終點站：左營
    end_station = driver.find_element(
        By.ID, "select_location02"
    )
    Select(end_station).select_by_visible_text("左營")

    # 6. 點擊搜尋按鈕
    search_btn = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "start-search")
        )
    )
    search_btn.click()

    print("已送出查詢請求...")

    # 7. 等待載入畫面消失
    wait.until(
        EC.invisibility_of_element_located(
            (By.ID, "search-loading")
        )
    )

    # 8. 等待去程分頁出現內容
    wait.until(
        lambda d: d.find_element(
            By.ID, "ttab-01"
        ).get_attribute("innerHTML").strip() != ""
    )

    # 9. 取得去程查詢結果
    ticket_frame = driver.find_element(
        By.ID, "ttab-01"
    )

    print("\n===== 去程查詢結果 =====")
    print(ticket_frame.text)

    # 10. 印出 HTML，確認實際車次資料結構
    print("\n===== 去程 HTML（前 5000 字）=====")
    print(ticket_frame.get_attribute("innerHTML")[:5000])

    input("\n請按 Enter 鍵結束...")

except TimeoutException as e:
    print("等待網頁元素逾時。")
    print("可能原因：查詢尚未完成、網站載入失敗，或選擇器已變更。")
    print(f"錯誤內容：{e}")

except Exception as e:
    print(f"執行出錯：{type(e).__name__}")
    print(f"錯誤原因：{e}")

finally:
    driver.quit()
