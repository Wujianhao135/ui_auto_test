"""
Day 1 第一个 Playwright 脚本
目标：自动打开浏览器，访问若依登录页，截图保存
"""
# 1. 从 playwright 引入同步模式入口（入门先用同步，代码从上往下执行，好懂）
from playwright.sync_api import sync_playwright

# sync_playwright() 是一个"启动器"，用 with 语句包住，结束会自动清理
with sync_playwright() as p:
    # 2. 启动浏览器。chromium 是 Playwright 自带的内核。
    #    headless=False = 显示浏览器窗口（你能看到它操作）；True = 后台无窗口
    browser = p.chromium.launch(headless=False)

    # 3. 新建一个"上下文"（独立会话，互不影响）
    context = browser.new_context()

    # 4. 在上下文里打开一个标签页，page 就是你后面操作的主角
    page = context.new_page()

    # 5. 让浏览器打开若依登录页
    page.goto("http://localhost")

    # 6. 等页面网络空闲（接口都请求完了），避免图没加载完就截图
    page.wait_for_load_state("networkidle")

    # 7. 截图，保存到 screenshots 文件夹
    page.screenshot(path="screenshots/day1_login_page.png")

    # 8. 打印网页标题，确认打开的是哪个页面
    print("页面标题：", page.title())
    print("当前网址：", page.url)

    # 9. 停 3 秒，让你亲眼看到浏览器窗口
    page.wait_for_timeout(3000)

    # 10. 关闭浏览器
    browser.close()

print("脚本执行完成！请看 screenshots/day1_login_page.png")
