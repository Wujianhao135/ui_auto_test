
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    brower = p.chromium.launch(headless=False)
    page = brower.new_page()
    page.goto("http://localhost")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("账号").fill("admin")
    page.get_by_placeholder("密码").fill("admin123")
    page.get_by_role("button",name="登 录").click()
    # 等页面真的跳转到首页（URL 里出现 index），最多等 10 秒
    page.wait_for_url("**/index**", timeout=10000)
    page.wait_for_load_state("networkidle")
    #进入用户管理页
    page.goto("http://localhost/system/user")
    page.wait_for_load_state("networkidle")
    #截图保存
    page.screenshot(path="screenshots/day2_user_list.png", full_page=True)
    # 打印当前页面信息
    print(f"标题: {page.title()}")
    print(f"网址: {page.url}")
