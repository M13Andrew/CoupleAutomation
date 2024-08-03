import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  # Change to headless=True if you don't need the browser UI
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    yield page
    page.close()