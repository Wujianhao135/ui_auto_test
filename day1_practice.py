# day1_open_page.py
# 功能：打开若依系统登录页，截图保存

from playwright.sync_api import sync_playwright

# 1. 启动浏览器
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)  # headless=False 表示显示浏览器窗口
page = browser.new_page()

# 2. 打开若依登录页
page.goto("http://localhost")


# 3. 等页面加载完成
page.wait_for_load_state("networkidle")

# 输入账号
page.get_by_placeholder("账号").fill("admin")
page.get_by_placeholder("密码").fill("admin123")
page.get_by_role("button", name="登 录").click()

# 3. 1等登录页面加载完成
# 等页面真的跳转到首页（URL 里出现 index），最多等 10 秒
page.wait_for_url("**/index**", timeout=10000)
page.wait_for_load_state("networkidle")


# 4. 截图保存
page.screenshot(path="screenshots/day1_after_login.png", full_page=True)

# 5. 打印页面信息
print(f"标题: {page.title()}")
print(f"网址: {page.url}")

page.wait_for_timeout(2000)  # 停2秒让你看到输入效果
# 6. 关闭
browser.close()
playwright.stop()