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

        def test_no_valid_email(self, page):
            personal_info = next(generated_person())
            name = personal_info.full_name
            email = personal_info.email
            current = personal_info.current_address
            permanent = personal_info.permanent_address
            page.goto('https://demoqa.com/text-box')
            test_text_box_page = ElementsPage.TextBoxPage(page)
            test_text_box_page.fill_text_box(name, email.replace('@', ''), current, permanent)
            test_text_box_page.click_submit_button()
            error = test_text_box_page.error_checking()
            assert error == True

    class TestCheckBoxPage:

        def test_check_box(self, page):
            page.goto('https://demoqa.com/checkbox')
            check_box_page = ElementsPage.CheckBox(page)
            check_box_page.click_expand_all_button()
            check_box_page.click_random_checkbox()
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_check_box == output_result

    class TestRadioButtonPage:

        def test_radio_button_impressive(self, page):
            page.goto('https://demoqa.com/radio-button')
            radio_button_page = ElementsPage.RadioButton(page)
            radio_button_page.click_radio_button('impressive')
            result = radio_button_page.result_radio_button()
            assert result == "Impressive"

        def test_radio_button_yes(self, page):
            page.goto('https://demoqa.com/radio-button')
            radio_button_page = ElementsPage.RadioButton(page)
            radio_button_page.click_radio_button('yes')
            result = radio_button_page.result_radio_button()
            assert result == "Yes"

        def test_radio_button_no(self, page):
            page.goto('https://demoqa.com/radio-button')
            radio_button_page = ElementsPage.RadioButton(page)
            radio_button_page.click_radio_button('no')
            result = radio_button_page.result_radio_button()
            assert result == "No"

    class TestWebTables:

        def test_add_new_person(self, page):
            page.goto('https://demoqa.com/webtables')
            web_tables_page = ElementsPage.WebTables(page)
            web_tables_page.add_button()
            personal_info = web_tables_page.fill_person_info()
            web_tables_page.submit_button()
            result = web_tables_page.get_result()
            personal_info_list = list(personal_info)
            assert personal_info_list == result[:len(personal_info_list)]

        def test_edit_person(self, page):
            page.goto('https://demoqa.com/webtables')
            web_tables_page = ElementsPage.WebTables(page)
            web_tables_page.add_button()
            web_tables_page.fill_person_info()
            web_tables_page.submit_button()
            web_tables_page.edit_button()
            personal_info = web_tables_page.fill_person_info()
            web_tables_page.submit_button()
            result = web_tables_page.get_result()
            personal_info_list = list(personal_info)
            assert personal_info_list == result[:len(personal_info_list)]

        def test_delete_all_persones(self, page):
            page.goto('https://demoqa.com/webtables')
            web_tables_page = ElementsPage.WebTables(page)
            web_tables_page.add_button()
            web_tables_page.fill_person_info()
            web_tables_page.submit_button()
            web_tables_page.delete_button()
            result = web_tables_page.empty_result()
            assert result

        def test_search_by(self, page):
            page.goto('https://demoqa.com/webtables')
            web_tables_page = ElementsPage.WebTables(page)
            web_tables_page.add_button()
            person = web_tables_page.fill_person_info()
            web_tables_page.submit_button()
            web_tables_page.search_by_name(person[0])
            result = web_tables_page.search_result()
            assert person[0] in result

    class TestButtons:

        def test_double_click(self, page):
            page.goto('https://demoqa.com/buttons')
            buttons_page = ElementsPage.Buttons(page)
            buttons_page.double_click()
            result = buttons_page.double_click_result()
            assert result

        def test_right_click(self, page):
            page.goto('https://demoqa.com/buttons')
            buttons_page = ElementsPage.Buttons(page)
            buttons_page.right_click()
            result = buttons_page.right_click_result()
            assert result

        def test_dymanic_click(self, page):
            page.goto('https://demoqa.com/buttons')
            buttons_page = ElementsPage.Buttons(page)
            buttons_page.dynamic_click()
            result = buttons_page.dynamic_click_result()
            assert result
