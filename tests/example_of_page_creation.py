from playwright.sync_api import sync_playwright

#This happens while we call a method with page fixture
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

page.goto("")

