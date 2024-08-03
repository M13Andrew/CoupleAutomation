import time
from pages.elements import ElementsPage
from generator.generator import generated_person


class TestElementsPage:
    class TestTextBoxPage:

        def test_fill_boxes_valid_data(self, page):
            personal_info = next(generated_person())
            name = personal_info.full_name
            email = personal_info.email
            current = personal_info.current_address
            permanent = personal_info.permanent_address
            page.goto('https://demoqa.com/text-box')
            test_text_box_page = ElementsPage.TextBoxPage(page)
            test_text_box_page.fill_text_box(name, email, current, permanent)
            test_text_box_page.click_submit_button()
            result = test_text_box_page.text_box_result()
            assert name == result[0]
            assert email == result[1]
            assert current + " " == result[2]
            assert permanent == result[3]
