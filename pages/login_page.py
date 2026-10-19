from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.get_by_placeholder("账号")
        self.password_input = page.get_by_placeholder("密码")
        self.login_button = page.get_by_role("button",name="登 录")

    def login(self,username,password):
        self.page.goto("http://localhost")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(1000)