'''Write a test script to automate a e commerce website and perform the below actions:
1. Login
2.sort items by high to low price.
3. Select one Orange Tshirt.
4. checkout and purchase.
5. Back to home'''

from playwright.sync_api import Page ,expect

def test_swag_lab(page:Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("password").fill("secret_sauce")
    page.get_by_role("button", name ="Login").click()
    page.get_by_role("combobox").select_option("hilo")
    page.get_by_role("button",name="add-to-cart-test.allthethings()-t-shirt-(red)" ).click()



