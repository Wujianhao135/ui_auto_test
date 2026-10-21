import pytest
import yaml
from ui_auto_test.pages.login_page import LoginPage

with open("data//login_cases.yaml",encoding="utf-8") as f:
    cases = yaml.safe_load(f)

@pytest.mark.login
@pytest.mark.parametrize("case",cases,ids=[c["case_name"] for c in cases])
def test_login_data(page,case):
    loginpage = LoginPage(page)
    loginpage.login(case["username"],case["password"])
    if case["expect_success"]:
        assert "/index" in page.url ,"正确密码应该登录成功"
    else:
        # 应该登录失败，URL 还在登录页
        error = page.locator(".el-message--error")
        assert error.count() > 0 or "/index" not in page.url, "错误密码应该登录失败"
