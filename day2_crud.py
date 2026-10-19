"""
Day 2 主流程：登录 → 新增用户 → 搜索验证 → 删除用户
稳定版：每次都用 .el-dialog:visible 现取可见弹窗，不缓存失效引用
"""
import time
from playwright.sync_api import sync_playwright

username = f"test{int(time.time()) % 100000}"
print(f"本次要新增/删除的用户名: {username}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. 登录
    page.goto("http://localhost")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("账号").fill("admin")
    page.get_by_placeholder("密码").fill("admin123")
    page.get_by_role("button", name="登 录").click()
    page.wait_for_url("**/index**", timeout=10000)
    print("✓ 登录成功")

    # 2. 进入用户管理
    page.goto("http://localhost/system/user")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(800)

    # 3. 点新增
    page.get_by_role("button", name="新增").click()
    page.wait_for_timeout(800)

    # 4. 在"可见的添加用户弹窗"里填表单
    dlg = page.locator(".el-dialog:visible")  # 每次用这个现取
    dlg.get_by_placeholder("请输入用户昵称").fill("自动化测试昵称")
    dlg.get_by_placeholder("请输入用户名称").fill(username)
    dlg.get_by_placeholder("请输入用户密码").fill("Test@123456")
    dlg.get_by_placeholder("请输入手机号码").fill("13800138000")
    dlg.get_by_placeholder("请输入邮箱").fill("test@example.com")
    print("✓ 文本字段已填")

    # 选部门：vue-treeselect 输入过滤
    dlg.locator(".vue-treeselect__input").click()
    page.wait_for_timeout(300)
    dlg.locator(".vue-treeselect__input").fill("研发部门")
    page.wait_for_timeout(600)
    page.keyboard.press("Enter")
    page.wait_for_timeout(500)
    print("✓ 已选部门")

    # 5. 点确定提交
    page.locator(".el-dialog:visible").locator("button", has_text="确").click()
    page.wait_for_selector(".el-message--success", timeout=5000)
    print("✓ 新增成功")

    # 6. 搜索验证
    page.get_by_placeholder("请输入用户名称").first.fill(username)
    page.get_by_role("button", name="搜索").click()
    page.wait_for_timeout(800)
    page.get_by_role("cell", name=username).wait_for(timeout=5000)
    print(f"✓ 搜索验证成功：{username} 在列表中")
    page.screenshot(path="screenshots/day2_after_add.png")

    # 7. 删除：勾选 → 删除 → 确认
    page.locator(".el-table__body .el-checkbox").first.click()
    page.get_by_role("button", name="删除").first.click()
    page.wait_for_timeout(500)
    page.locator(".el-message-box:visible").locator("button", has_text="确").click()
    page.wait_for_selector(".el-message--success", timeout=5000)
    print("✓ 删除成功")

    page.wait_for_timeout(1000)
    page.screenshot(path="screenshots/day2_after_delete.png")
    browser.close()

print("\nDay 2 主流程全部跑通：登录→新增→搜索验证→删除")
