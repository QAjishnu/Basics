from playwright.sync_api import Page

def test_playwright_basics(playwright): #playwright is gobal fixture
    browser=playwright.chromium.launch(headless=False)
    context =browser.new_context() #for seperate private window which has its own cache, cookies,data.
    page = context.new_page() #it opens a new tab/page.
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("checkbox", name ="terms").click()
    #page.get_by_role("radio", value= "user").click()
    page.get_by_role("button", name="Sign In").click()



