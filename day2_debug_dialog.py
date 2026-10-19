"""调试：填完表单选完部门后，看弹窗真实状态和按钮结构"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("账号").fill("admin")
    page.get_by_placeholder("密码").fill("admin123")
    page.get_by_role("button", name="登 录").click()
    page.wait_for_url("**/index**", timeout=10000)
    page.goto("http://localhost/system/user")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(800)

    page.get_by_role("button", name="新增").click()
    page.wait_for_timeout(800)
    dialog = page.get_by_role("dialog", name="添加用户")
    dialog.get_by_placeholder("请输入用户昵称").fill("测试昵称")
    dialog.get_by_placeholder("请输入用户名称").fill("debuguser")
    dialog.get_by_placeholder("请输入用户密码").fill("Test@123456")
    dialog.locator(".vue-treeselect__input").click()
    page.wait_for_timeout(500)
    page.locator("span.node-label", has_text="研发部门").click(force=True)
    page.wait_for_timeout(500)

    print("=== 可见 dialog 里所有按钮 ===")
    visible_btns = page.locator(".el-dialog__wrapper:visible button")
    for i in range(visible_btns.count()):
        el = visible_btns.nth(i)
        if el.is_visible():
            print(f"  btn[{i}]: text={el.inner_text().strip()!r}, "
                  f"class={el.get_attribute('class')!r}")

    print("\n=== 添加用户 dialog 的 HTML 结构（前 500 字符） ===")
    html = page.get_by_role("dialog", name="添加用户").inner_html()
    print(html[:800])

    page.screenshot(path="screenshots/day2_debug_state.png")
    browser.close()
