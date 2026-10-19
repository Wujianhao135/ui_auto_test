"""
Day 1 元素定位练习
目标：学会用 Playwright 精准找到登录页上的用户名框、密码框、登录按钮
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost")
    page.wait_for_load_state("networkidle")

    print("=" * 50)
    print("开始定位登录页元素")
    print("=" * 50)

    # 方式1：按 placeholder（输入框里的灰色提示文字）—— 若依输入框最好用
    # 注意：若依新版账号框的 placeholder 是"账号"，不是"用户名"！
    username_box = page.get_by_placeholder("账号")
    print(f"[placeholder] 账号输入框，找到 {username_box.count()} 个")

    password_box = page.get_by_placeholder("密码")
    print(f"[placeholder] 密码输入框，找到 {password_box.count()} 个")

    # 方式2：按角色+文字（按钮最常用：role=button，name=按钮文字）
    login_btn = page.get_by_role("button", name="登 录")
    print(f"[role] 登录按钮，找到 {login_btn.count()} 个")

    # 方式3：按文字（记住密码这个复选框）
    remember = page.get_by_text("记住密码")
    print(f"[text] 记住密码，找到 {remember.count()} 个")

    # 方式4：CSS 选择器（按 id / class，复杂页面用）
    pwd_css = page.locator("input[type='password']")
    print(f"[CSS] 密码框(input[type=password])，找到 {pwd_css.count()} 个")

    # 实战：真的操作一下——在用户名框里输入 "testuser"
    print("\n现在自动在用户名框输入 testuser ...")
    username_box.fill("testuser")
    page.wait_for_timeout(2000)  # 停2秒让你看到输入效果

    browser.close()
    print("\n定位练习完成！")
