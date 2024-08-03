from pages.elements import ElementsPage


class TestNoValidEmail:

    def test_no_valid_email(self, page):
        page.goto('https://demoqa.com/text-box')
        test_email = ElementsPage.TextBoxPage(page)
        person = test_text_box_page.fill_text_box()
        test_text_box_page.click_submit_button()
        result = test_text_box_page.text_box_result()
        assert person == result
