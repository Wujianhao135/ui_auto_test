"""探测登录页元素的真实属性，搞清楚 placeholder、按钮文字到底是什么"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # headless=True 不弹窗，快
    page = browser.new_page()
    page.goto("http://localhost")
    page.wait_for_load_state("networkidle")

    print("=== 页面上所有 input 输入框 ===")
    inputs = page.locator("input")
    for i in range(inputs.count()):
        el = inputs.nth(i)
        print(f"  input[{i}]: type={el.get_attribute('type')!r}, "
              f"placeholder={el.get_attribute('placeholder')!r}, "
              f"name={el.get_attribute('name')!r}, "
              f"id={el.get_attribute('id')!r}")

    print("\n=== 页面上所有 button 按钮 ===")
    buttons = page.locator("button")
    for i in range(buttons.count()):
        el = buttons.nth(i)
        print(f"  button[{i}]: type={el.get_attribute('type')!r}, 文字={el.inner_text()!r}")

    browser.close()
