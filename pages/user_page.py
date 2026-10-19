from playwright.sync_api import Page

class UserPage:
    def __init__(self, page: Page):
        self.page = page
        # 把元素定位写成变量，以后改定位只改这里
        self.add_button = page.get_by_role("button", name="新增")
        self.dialog = page.locator(".el-dialog:visible")

    def goto_user_list(self):
        """进入用户管理页"""
        self.page.goto("http://localhost/system/user")
        self.page.wait_for_load_state("networkidle")

    def add_user(self, nickname, username, password, phone, email):
        """新增一个用户"""
        # 1. 点新增
        self.add_button.click()
        self.page.wait_for_timeout(800)
        # 2. 在弹窗里填字段（你自己写，参考 day2_step2.py）
        self.dialog.get_by_placeholder("请输入用户昵称").fill(nickname)
        self.dialog.get_by_placeholder("请输入用户名称").fill(username)
        self.dialog.get_by_placeholder("请输入用户密码").fill(password)
        self.dialog.get_by_placeholder("请输入手机号码").fill(phone)
        self.dialog.get_by_placeholder("请输入邮箱").fill(email)
        # ... 剩下的你自己填：用户名、密码、手机、邮箱
        # 3. 选部门（参考 day2_step2.py 里 vue-treeselect 那段）
        self.dialog.locator(".vue-treeselect__input").click()
        self.page.wait_for_timeout(300)
        self.dialog.locator(".vue-treeselect__input").fill("研发部门")
        self.page.wait_for_timeout(600)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        # 4. 点确定提交
        self.dialog.locator("button", has_text="确").click()
        # 5. 等成功提示
        self.page.wait_for_selector(".el-message--success", timeout=5000)

    def search_user(self, username):
        """搜索用户"""
        # 自己写：在搜索框填 username，点搜索按钮
        self.page.get_by_placeholder("请输入用户名称").first.fill(username)
        self.page.get_by_role("button", name="搜索").click()
        self.page.wait_for_timeout(800)

    def delete_user(self):
        """删除当前搜索到的用户"""
        # 勾选
        self.page.locator(".el-table__body .el-checkbox").first.click()
        # 点删除
        self.page.get_by_role("button", name="删除").first.click()
        self.page.wait_for_timeout(500)
        # 确认框点确定
        self.page.locator(".el-message-box").locator("button", has_text="确").click()
        # 等成功提示
        self.page.wait_for_selector(".el-message--success", timeout=5000)

