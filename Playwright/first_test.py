import pytest
from playwright.sync_api import Page, expect


def test_google_title_and_search(page: Page):
    # 1. Google ke page par jaana
    page.goto("https://www.google.com")

    # 2. Check karna ki page ka title 'Google' hai ya nahi (Assertion)
    expect(page).to_have_title("Google")

    # 3. Search box ko dhoondna aur usme type karna
    # Google ka search input element ka naam 'q' hota hai
    search_box = page.locator("textarea[name='q']")
    search_box.fill("Playwright Python automation")

    # 4. Enter press karna search karne ke liye
    search_box.press("Enter")

    # 5. Thoda wait karna taaki hume results dikh sakein (Sirf dekhne ke liye)
    page.wait_for_timeout(2000)