from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException, TimeoutException
)

URL = "https://www.taiwanlottery.com/lotto/result/super_lotto638"
N = 3  # 要抓幾期


def results_ready(d):
    """至少有 N 期，且每期 7 顆球都已經有數字"""
    try:
        items = d.find_elements(By.CSS_SELECTOR, "div.result-item")
        if len(items) < N:
            return False
        for item in items[:N]:
            balls = item.find_elements(By.CSS_SELECTOR, ".result-item-simple-area .ball")
            if len(balls) < 7 or not all(b.text.strip() for b in balls):
                return False
        return items[:N]
    except StaleElementReferenceException:
        return False


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

try:
    items = WebDriverWait(driver, 20, poll_frequency=0.5).until(results_ready)
    print("開獎結果已載入\n")

    for item in items:
        period = item.find_element(By.CSS_SELECTOR, ".period-title").text
        date = item.find_element(By.CSS_SELECTOR, ".period-date").text

        balls = item.find_elements(By.CSS_SELECTOR, ".result-item-simple-area .ball")
        first_zone = [b.text for b in balls if "color-super" not in b.get_attribute("class")]
        second_zone = [b.text for b in balls if "color-super" in b.get_attribute("class")]

        print(f"{period}  {date}")
        print(f"  第一區：{' '.join(first_zone)}")
        print(f"  第二區：{' '.join(second_zone)}\n")

    input("請按下 Enter 鍵以結束程式...")

except TimeoutException:
    print("執行出錯：等待逾時，開獎結果沒有載入")
except Exception as e:
    print(f"執行出錯：{type(e).__name__}: {e}")
finally:
    driver.quit()
    
    
    