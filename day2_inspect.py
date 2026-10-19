"""Day2 探测：登录后进入用户管理页，看清楚页面结构"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 登录
    page.goto("http://localhost")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("账号").fill("admin")
    page.get_by_placeholder("密码").fill("admin123")
    page.get_by_role("button", name="登 录").click()
    page.wait_for_url("**/index**", timeout=10000)
    page.wait_for_load_state("networkidle")
    print("登录成功，当前URL:", page.url)

    # 直接导航到用户管理页（前端路由）
    page.goto("http://localhost/system/user")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)
    print("进入用户管理页，当前URL:", page.url)

    # 探测页面上的按钮
    print("\n=== 页面上的按钮 ===")
    btns = page.locator("button")
    for i in range(btns.count()):
        t = btns.nth(i).inner_text().strip().replace("\n", " ")
        if t:
            print(f"  button[{i}]: {t!r}")

    # 探测搜索区的输入框
    print("\n=== 搜索区输入框 ===")
    inputs = page.locator(".el-form input")
    for i in range(inputs.count()):
        el = inputs.nth(i)
        print(f"  input[{i}]: placeholder={el.get_attribute('placeholder')!r} type={el.get_attribute('type')!r}")

    # 探测表格列头
    print("\n=== 表格列头 ===")
    ths = page.locator(".el-table__header th .cell")
    for i in range(ths.count()):
        print(f"  列[{i}]: {ths.nth(i).inner_text().strip()!r}")

    page.screenshot(path="screenshots/day2_user_list.png", full_page=True)
    print("\n截图已保存: screenshots/day2_user_list.png")

    browser.close()
