from playwright.sync_api import Page, expect

BASE_URL = "https://devexpress.github.io/testcafe/example/"

def test_demo_page_loaded(page:Page):
    page.goto(BASE_URL)
    print("\n",page.url)
    expect(page).to_have_url(BASE_URL + "kuku",timeout=6500)
    pass

def test_user_name_presented(page :Page):
    page.goto(BASE_URL)

    pass

def test_title_presented(page :Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("TestCafe Example Page")
    pass
