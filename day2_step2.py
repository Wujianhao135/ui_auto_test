
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
    #新增
    page.get_by_role("button", name="新增").click()
    page.wait_for_timeout(1000)

    #填写内容
    dlg = page.locator(".el-dialog:visible")
    dlg.get_by_placeholder("请输入用户昵称").fill("测试昵称")
    dlg.get_by_placeholder("请输入用户名称").fill("test001")
    dlg.get_by_placeholder("请输入用户密码").fill("Test@123456")
    dlg.get_by_placeholder("请输入手机号码").fill("13800138000")
    dlg.get_by_placeholder("请输入邮箱").fill("test@test.com")
    # 选归属部门（树形下拉）
    dlg.locator(".vue-treeselect__input").click()
    page.wait_for_timeout(300)
    dlg.locator(".vue-treeselect__input").fill("研发部门")
    page.wait_for_timeout(600)
    page.keyboard.press("Enter")
    page.wait_for_timeout(500)
    # 点确定提交
    dlg.locator("button", has_text="确").click()

    # 等"操作成功"绿色提示出现（不用 sleep，等具体元素）
    page.wait_for_selector(".el-message--success", timeout=5000)

    # 1. 搜索刚建的用户
    page.get_by_placeholder("请输入用户名称").first.fill("test001")
    page.get_by_role("button", name="搜索").click()
    page.wait_for_timeout(800)

    # 2. 勾选表格里这个用户前面的复选框
    page.locator(".el-table__body .el-checkbox").first.click()

    # 3. 点"删除"按钮
    page.get_by_role("button", name="删除").first.click()
    page.wait_for_timeout(500)

    # 4. 弹出确认框，点"确定"
    page.locator(".el-message-box").locator("button", has_text="确").click()

    # 5. 等删除成功提示
    page.wait_for_selector(".el-message--success", timeout=5000)

    # 6. 截图
    page.screenshot(path="screenshots/day2_after_delete.png")

    # 打印当前页面信息
    print(f"标题: {page.title()}")
    print(f"网址: {page.url}")
