"""调试2：选部门后立刻截图，看弹窗状态"""
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
    page.wait_for_timeout(1000)
    page.screenshot(path="screenshots/step1_dialog_open.png")
    print("步骤1: 新增弹窗已打开")

    dialog = page.get_by_role("dialog", name="添加用户")
    dialog.get_by_placeholder("请输入用户昵称").fill("测试昵称")
    dialog.get_by_placeholder("请输入用户名称").fill("debuguser")
    dialog.get_by_placeholder("请输入用户密码").fill("Test@123456")

    # 点部门输入框
    dialog.locator(".vue-treeselect__input").click()
    page.wait_for_timeout(800)
    page.screenshot(path="screenshots/step2_tree_open.png")
    print("步骤2: 部门树已展开")

    # 点研发部门（force）
    page.locator("span.node-label", has_text="研发部门").click(force=True)
    page.wait_for_timeout(800)
    page.screenshot(path="screenshots/step3_after_select_dept.png")
    print("步骤3: 已选研发部门")

    # 检查弹窗还在不在
    dialog_count = page.locator(".el-dialog__wrapper").count()
    print(f"页面上 .el-dialog__wrapper 总数: {dialog_count}")
    for i in range(dialog_count):
        w = page.locator(".el-dialog__wrapper").nth(i)
        try:
            visible = w.is_visible()
            title = w.locator(".el-dialog__title").inner_text() if w.locator(".el-dialog__title").count() else "(无标题)"
            print(f"  dialog[{i}]: visible={visible}, title={title!r}")
        except Exception as e:
            print(f"  dialog[{i}]: 读取失败 {e}")

    browser.close()
