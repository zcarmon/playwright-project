from playwright.sync_api import Page, expect

BASE_URL = "https://devexpress.github.io/testcafe/example/"

# def test_demo_page_loaded(page:Page):
#     page.goto(BASE_URL)
#     print("\n",page.url)
#     expect(page).to_have_url(BASE_URL + "kuku",timeout=6500)
#     pass

# def test_user_name_presented(page :Page):
#     page.goto(BASE_URL)
#     # there are some options to fill a fiels copy paste like or type like
#     #page.locator("[id='developer-name']").press_sequentially("Zvi Carmon",delay=500)
#     page.locator("#developer-name").fill("Kuki muki")
#
#     pass

def test_title_presented(page :Page):
    page.goto(BASE_URL)
    # fill a text box by typing
    page.locator("#developer-name").press_sequentially("Zvi Carmon",delay=150)


    # check the title
    expect(page).to_have_title("TestCafe Example Page")

    # check a ckeckbox
    page.locator('[data-testid="remote-testing-checkbox"]').check()
    page.locator('[data-testid="remote-testing-checkbox"]').check()

    # click on a ckeckbox
    page.locator('[data-testid = "reusing-js-code-checkbox"]').click()
    page.locator('[data-testid = "reusing-js-code-checkbox"]').click()

    #select radio button
    page.get_by_test_id("macos-radio").check()

    #select from dropdown list
    page.locator(('[data-testid="preferred-interface-select"]')).select_option("JavaScript API")

    #select the checkbox in order to enable the comment area
    page.locator('[data-testid="tried-testcafe-checkbox"]').check()

    # FILL THE TEXT AREA
    page.get_by_test_id("comments-area").fill("fsfsgfdgfds sdfg sdfg sdfg s dg s dfgs")

    #press the submit button
    page.get_by_role("button",name="Submit").click()

    page.wait_for_timeout(5000)

    pass
