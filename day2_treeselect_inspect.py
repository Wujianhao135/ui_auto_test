"""探测 vue-treeselect 展开后的真实 DOM"""
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
    dialog.locator(".vue-treeselect__input").click()
    page.wait_for_timeout(800)

    print("=== body 下所有浮层的 class ===")
    overlays = page.locator("body > div[class*='vue-treeselect'], body > div[class*='select-dropdown'], body > div[class*='popper']")
    for i in range(overlays.count()):
        el = overlays.nth(i)
        cls = el.get_attribute("class")
        visible = el.is_visible()
        print(f"  overlay[{i}]: class={cls!r} visible={visible}")

    print("\n=== 找包含'研发部门'文字的元素 ===")
    nodes = page.locator("text=研发部门")
    print(f"  共 {nodes.count()} 个'研发部门'")
    for i in range(min(nodes.count(), 5)):
        el = nodes.nth(i)
        print(f"  node[{i}]: tag=<{el.evaluate('e=>e.tagName')}>, class={el.get_attribute('class')!r}, "
              f"visible={el.is_visible()}")

    page.screenshot(path="screenshots/day2_treeselect_open.png")
    browser.close()
