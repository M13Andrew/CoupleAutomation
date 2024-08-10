from generator.generator import generated_person
from pages.base_page import BasePage


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
