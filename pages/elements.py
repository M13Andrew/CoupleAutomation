from playwright.sync_api import Page
from generator.generator import generated_person


class ElementsPage:

    class TextBoxPage:

        def __init__(self, page: Page):
            self.page = page

        def fill_text_box(self):
            personal_info = next(generated_person())
            name = personal_info.full_name
            email = personal_info.email
            current = personal_info.current_address
            permanent = personal_info.permanent_address
            self.page.get_by_placeholder("Full Name").fill(name)
            self.page.get_by_placeholder("name@example.com").fill(email)
            self.page.get_by_placeholder("Current Address").fill(current)
            self.page.locator("#permanentAddress").fill(permanent)
            return name, email, current + ' ', permanent

        def click_submit_button(self):
            self.page.get_by_role("button", name="Submit").click()

        def text_box_result(self):
            name = self.page.query_selector("p[id='name']").text_content()
            email = self.page.query_selector("p[id='email']").text_content()
            current = self.page.query_selector("p[id='currentAddress']").text_content()
            permanent = self.page.query_selector("p[id='permanentAddress']").text_content()
            return name.split(':')[1], email.split(':')[1], current.split(':')[1], permanent.split(':')[1]