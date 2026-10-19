# from playwright.sync_api import sync_playwright
# from ui_auto_test.pages.login_page import LoginPage
# from ui_auto_test.pages.user_page import UserPage


# def test_login_user():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         login = LoginPage(page)
#         login.login("admin", "admin123")
#         user = UserPage(page)
#         user.goto_user_list()
#         user.add_user("测试昵称1","test002","Test@123456","13800138001","test1@test.com")
#         # 验证：搜索后能在表格里找到 test002
#         user.search_user("test002")
#         row = page.locator(".el-table__body tr", has_text="test002")
#         assert row.count() > 0, "新增后搜索不到 test002"
#
#         user.delete_user()
#         # 验证：删除后搜索不到了
#         user.search_user("test002")
#         row_after = page.locator(".el-table__body tr", has_text="test002")
#         assert row_after.count() == 0, "删除后还能搜到 test002"
#
#         browser.close()
#         print("✅ 新增→搜索→删除 全流程通过")

from ui_auto_test.pages.login_page import LoginPage
from ui_auto_test.pages.user_page import UserPage
import time
import random
import pytest

@pytest.mark.smoke
def test_login_user(page):
    username = f"test_{int(time.time())}_{random.randint(100, 999)}"
    login = LoginPage(page)
    login.login("admin", "admin123")
    user = UserPage(page)
    user.goto_user_list()
    user.add_user("测试昵称1", username, "Test@123456", "13800138001", "test1@test.com")
    user.search_user(username)
    row = page.locator(".el-table__body tr", has_text=username)
    assert row.count() > 0
    user.delete_user()
    user.search_user(username)
    row_after = page.locator(".el-table__body tr", has_text=username)
    assert row_after.count() == 0
    print("✅ 全流程通过")

