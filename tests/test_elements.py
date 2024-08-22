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
            assert result == 'You have done a double click'

        def test_right_click(self, page):
            page.goto('https://demoqa.com/buttons')
            buttons_page = ElementsPage.Buttons(page)
            buttons_page.right_click()
            result = buttons_page.right_click_result()
            assert result == 'You have done a right click'

        def test_dynamic_click(self, page):
            page.goto('https://demoqa.com/buttons')
            buttons_page = ElementsPage.Buttons(page)
            buttons_page.dynamic_click()
            result = buttons_page.dynamic_click_result()
            assert result == 'You have done a dynamic click', 'test has been fallen'

    class TestLinks:

        def test_home_link(self, page):
            page.goto('https://demoqa.com/links')
            with page.context.expect_page() as new_page_info:
                link_button = ElementsPage.Links(page)
                link_button.click_links_buttons('home')
            new_page = new_page_info.value
            new_page.wait_for_load_state('load')
            new_url = new_page.url
            assert new_url == 'https://demoqa.com/'

        def test_home_dynamic_link(self, page):
            page.goto('https://demoqa.com/links')
            with page.context.expect_page() as new_page_info:
                link_button = ElementsPage.Links(page)
                link_button.click_links_buttons('homedynamic')
            new_page = new_page_info.value
            new_page.wait_for_load_state('load')
            new_url = new_page.url
            assert new_url == 'https://demoqa.com/'

        def test_created_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('created')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 201 and status text Created'

        def test_no_content_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('no-content')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 204 and status text No Content'

        def test_moved_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('moved')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 301 and status text Moved Permanently'

        def test_bad_request_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('bad-request')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 400 and status text Bad Request'

        def test_unauthorized_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('unauthorized')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 401 and status text Unauthorized'

        def test_forbidden_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('forbidden')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 403 and status text Forbidden'

        def test_invalid_url_link(self, page):
            page.goto('https://demoqa.com/links')
            link_button = ElementsPage.Links(page)
            link_button.click_links_buttons('invalid-url')
            result = link_button.links_responded()
            assert result == 'Link has responded with staus 404 and status text Not Found'

    class TestUploadAndDownload:

        def test_choose_file(self, page):
            page.goto('https://demoqa.com/upload-download')
            choose_file = ElementsPage.UploadAndDownload(page)
            file_name, result = choose_file.select_file()
            assert file_name == result

    class TestDynamicProperties:

        def test_enable_buttons(self, page):
            page.goto('https://demoqa.com/dynamic-properties')
            dynamic_page = ElementsPage.DynamicProperties(page)
            time.sleep(6)
            visible_button = dynamic_page.check_visible_button()
            enable_button = dynamic_page.check_enable_button()
            assert enable_button == True
            assert visible_button == True

        def test_color_button(self, page):
            page.goto('https://demoqa.com/dynamic-properties')
            dynamic_page = ElementsPage.DynamicProperties(page)
            previous_color, color_after = dynamic_page.check_color_button()
            assert previous_color != color_after
