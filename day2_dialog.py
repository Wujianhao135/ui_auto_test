"""Day2 探测新增用户弹窗：点新增按钮，看弹窗里的表单字段"""
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

    # 点"新增"按钮
    page.get_by_role("button", name="新增").click()
    page.wait_for_timeout(800)  # 等弹窗动画

    # 探测弹窗里的输入框
    print("=== 新增弹窗里的输入框 ===")
    inputs = page.locator(".el-dialog input")
    for i in range(inputs.count()):
        el = inputs.nth(i)
        print(f"  input[{i}]: type={el.get_attribute('type')!r}, "
              f"placeholder={el.get_attribute('placeholder')!r}")

    # 探测弹窗里的下拉框（el-select）
    print("\n=== 新增弹窗里的表单项文字（label） ===")
    labels = page.locator(".el-dialog .el-form-item__label")
    for i in range(labels.count()):
        print(f"  label[{i}]: {labels.nth(i).inner_text().strip()!r}")

    # 探测弹窗底部按钮
    print("\n=== 弹窗底部按钮 ===")
    dlg_btns = page.locator(".el-dialog__footer button, .el-dialog button")
    for i in range(dlg_btns.count()):
        t = dlg_btns.nth(i).inner_text().strip().replace("\n", " ")
        if t:
            print(f"  button: {t!r}")

    page.screenshot(path="screenshots/day2_add_dialog.png")
    print("\n弹窗截图: screenshots/day2_add_dialog.png")

    browser.close()
