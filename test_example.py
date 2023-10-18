import time


def test_first(page):
    page.goto("https://saucedemo.com/v1/")
    page.locator("input[id='user-name']").fill("standard_user")
    page.locator("input[id='password']").fill("secret_sauce")
    page.locator("input[id='login-button']").click()
    time.sleep(5)  # pytest --headed --slowmo 1000
