from playwright.sync_api import Page

def test_playwright_basics(playwright): #playwright is gobal fixture
    browser=playwright.chromium.launch(headless=False)
    context =browser.new_context() #for seperate private window which has its own cache, cookies,data.
    page = context.new_page() #it opens a new tab/page.
    page.goto("https://google.com") #navigates to the website

def test_playwright_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")



