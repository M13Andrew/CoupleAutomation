import time
from pages.elements import ElementsPage


class TestElementsPage:

    class TestTextBoxPage:

        def test_fill_boxes_valid_data(self, page):
            page.goto('https://demoqa.com/text-box')
            test_text_box_page = ElementsPage.TextBoxPage(page)
            person = test_text_box_page.fill_text_box()
            test_text_box_page.click_submit_button()
            result = test_text_box_page.text_box_result()
            assert person == result
