from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 启动浏览器（Selenium 4 自动找 driver）
driver = webdriver.Chrome()

# 2. 打开若依
driver.get("http://localhost")

# 3. 填账号密码（对比 Playwright 的 get_by_placeholder）
driver.find_element(By.CSS_SELECTOR, "input[placeholder='账号']").clear()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='账号']").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='密码']").clear()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='密码']").send_keys("admin123")


# 4. 点登录按钮
driver.find_element(By.XPATH, "//button[contains(., '登 录')]").click()

# 5. 显式等待：等 URL 变成 /index（Selenium 没有自动等待，必须手动写）
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("/index"))

print("登录成功，当前URL:", driver.current_url)

driver.quit()
