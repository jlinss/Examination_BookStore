import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://tap-vt26-testautomatisering.github.io/exam/",
                  wait_until="domcontentloaded"
                  )
        yield page
        browser.close()
