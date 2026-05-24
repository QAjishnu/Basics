from playwright.sync_api import Page, expect


def test_login_assertion(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("abcdfeghs")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("checkbox" , name="terms").click()
    page.get_by_role("button" , name ="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


