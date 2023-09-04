import pytest
from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "stepik",
#                     "value": "sd4fFfv!x_cfcstepik",
#                     "url": "https://example.com"  # Замените на нужный URL
#                 },
#             ]
#         },
#     }


# @pytest.fixture(scope="function")
# def browser_fixture():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()

@pytest.fixture(scope="function")
def page(playwright: sync_playwright) -> None:
    print("\nStarting browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1600, "height": 800})
    yield page
    page.close()
    context.close()
    browser.close()
    print("\nBrowser closed...")
