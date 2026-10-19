from playwright.sync_api import sync_playwright
from ui_auto_test.pages.login_page import LoginPage


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login = LoginPage(page)
        login.login("admin", "admin123")
        print(f"网页链接：{page.url}")
        browser.close()
