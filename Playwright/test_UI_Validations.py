from playwright.sync_api import Page , expect

def test_UI_Validations_dynamic(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("checkbox", name="terms").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")#to refine the search only 2 iphone block
    iphoneProduct.get_by_role("button").click()# to click on the  Add to cart button.
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")#to refine the search only 2 Nokia block
    NokiaProduct.get_by_role("button").click()# to click on the  Add to cart button.
    page.get_by_text("Checkout").click() # to click on checkout button
    expect(page.locator(".media-body")).to_have_count(2) # to validate 2 items are added in cart
    page.get_by_role("button",name="Checkout").click()
    page.get_by_role("button",name="Purchase").click()





