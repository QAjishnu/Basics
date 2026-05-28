from playwright.sync_api import Page, Playwright


def test_child_windows(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context =browser.new_context() #for seperate private window which has its own cache, cookies,data.
    page = context.new_page() #it opens a new tab/page.
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with (page.expect_popup() as newpage):
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        childpage =newpage.value
        text =childpage.locator(".red").text_content()
        print(tex
