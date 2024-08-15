from generator.generator import generated_person
from pages.base_page import BasePage
import random
import time


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

    class RadioButton(BasePage):

        def click_radio_button(self, choice):
            choices = {'yes': "Yes",
                       'impressive': "Impressive",
                       'no': "No"
                       }
            self.page.get_by_text(choices[choice]).click()

        def result_radio_button(self):
            result = self.page.query_selector("span.text-success").text_content()
            return result

    class WebTables(BasePage):

        def add_button(self):
            self.page.get_by_role("button", name="Add").click()

        def fill_person_info(self):
            personal_info = next(generated_person())
            firstname = personal_info.firstname
            lastname = personal_info.lastname
            email = personal_info.email
            age = personal_info.age
            salary = personal_info.salary
            department = personal_info.department
            self.page.get_by_placeholder("First Name").fill(firstname)
            self.page.get_by_placeholder("Last Name").fill(lastname)
            self.page.get_by_placeholder("name@example.com").fill(email)
            self.page.get_by_placeholder("Age").fill(str(age))
            self.page.get_by_placeholder("Salary").fill(str(salary))
            self.page.get_by_placeholder("Department").fill(department)
            return firstname, lastname, str(age), email, str(salary)

        def submit_button(self):
            self.page.get_by_role("button", name="Submit").click()

        def get_result(self):
            rows = self.page.locator('div.rt-tr-group').element_handles()
            row = rows[3].inner_text()
            return row.split()

        def edit_button(self):
            self.page.locator("#edit-record-4 path").click()

        def delete_button(self):
            while True:
                delete_buttons_count = self.page.locator("span[title='Delete']").all()
                if not delete_buttons_count:
                    break
                delete_buttons_count[0].click()

        def empty_result(self):
            result = self.page.locator('div.rt-noData').text_content()
            return result

        def search_by_name(self, search):
            self.page.get_by_placeholder("Type to search").fill(search)

        def search_result(self):
            result = self.page.locator("div[class='rt-tr -odd']").inner_text()
            return result

    class Buttons(BasePage):

        def double_click(self):
            self.page.get_by_role("button", name="Double Click Me").dblclick()

        def double_click_result(self):
            result = self.page.get_by_text("You have done a double click").inner_text()
            return result

        def right_click(self):
            self.page.get_by_role("button", name="Right Click Me").click(button="right")

        def right_click_result(self):
            result = self.page.get_by_text("You have done a right click").inner_text()
            return result

        def dynamic_click(self):
            self.page.get_by_role("button", name="Click Me", exact=True).click()

        def dynamic_click_result(self):
            result = self.page.get_by_text("You have done a dynamic click").inner_text()
            return result
a