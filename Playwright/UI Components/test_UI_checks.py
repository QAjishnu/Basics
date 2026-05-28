from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    # IRCTC website open
    page.goto("https://www.irctc.co.in/nget/train-search")

    # Maximize like view
    page.set_viewport_size({"width": 1536, "height": 864})

    # Popup handle
    page.locator("button").filter(has_text="OK").click()

    # FROM station
    from_station = page.locator("input[placeholder='From*']")
    from_station.click()
    from_station.fill("del")

    # Suggestion select
    page.locator("li[role='option']").filter(
        has_text="NEW DELHI - NDLS"
    ).click()

    # TO station
    to_station = page.locator("input[placeholder='To*']")
    to_station.click()
    to_station.fill("kanpur")

    # Suggestion select
    page.locator("li[role='option']").filter(
        has_text="KANPUR CENTRAL - CNB"
    ).click()

    # 5 sec wait to see result
    page.wait_for_timeout(5000)

    browser.close()