from generator.generator import generated_person
from pages.base_page import BasePage
import random


class ElementsPage:

    class TextBoxPage(BasePage):

        def fill_text_box(self, name, email, current, permanent):
            self.page.get_by_placeholder("Full Name").fill(name)
            self.page.get_by_placeholder("name@example.com").fill(email)
            self.page.get_by_placeholder("Current Address").fill(current)
            self.page.locator("#permanentAddress").fill(permanent)

        def click_submit_button(self):
            self.page.get_by_role("button", name="Submit").click()

        def text_box_result(self):
            name = self.page.query_selector("p[id='name']").text_content()
            email = self.page.query_selector("p[id='email']").text_content()
            current = self.page.query_selector("p[id='currentAddress']").text_content()
            permanent = self.page.query_selector("p[id='permanentAddress']").text_content()
            return name.split(':')[1], email.split(':')[1], current.split(':')[1], permanent.split(':')[1]

        def error_checking(self):
            error = self.page.locator("input[class='mr-sm-2 field-error form-control']").count()
            if error > 0:
                return True
            else:
                return False

    class CheckBox(BasePage):

        def click_expand_all_button(self):
            self.page.get_by_label("Expand all").click()

        def click_random_checkbox(self):
            item_list = self.page.locator("span[class='rct-title']").element_handles()
            count = 21
            while count != 0:
                item = item_list[random.randint(1, 15)]
                if count > 0:
                    item.click()
                    count -= 1
                else:
                    break

        def get_checked_checkboxes(self):
            checked_list = self.page.locator("svg[class='rct-icon rct-icon-check']").element_handles()
            data = []
            for box in checked_list:
                title_item = box.query_selector("xpath=ancestor::span[contains(@class, 'rct-text')]")
                if title_item:
                    data.append(title_item.inner_text())
            return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

        def get_output_result(self):
            result_list = self.page.locator("span[class='text-success']").element_handles()
            data = []
            for item in result_list:
                data.append(item.inner_text())
            return str(data).replace(' ', '').lower()