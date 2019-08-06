from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self,app):
        self.app=app

    def add_new(self, contact):
        wb = self.app.wb
        self.open_create_contacts_page()
        self.fill_contact_form(contact)
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_home_page()

    def open_create_contacts_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wb = self.app.wb
        self.select_first_contact()
        # submit deletion
        wb.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wb.switch_to_alert().accept()

    def select_first_contact(self):
        wb = self.app.wb
        wb.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_data):
        wb = self.app.wb
        self.select_first_contact()
        wb.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_data)
        wb.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_home_page()

    def modify(self, new_data):
        wb = self.app.wb
        # select first contact
        self.select_first_contact()
        # submit editing
        wb.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_data)
        # submit update
        wb.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value_date("bday", contact.bday)
        self.change_field_value_date("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value_date("aday", contact.aday)
        self.change_field_value_date("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value_date(self, field_name, text):
        wb = self.app.wb
        if text is not None:
            wb.find_element_by_name(field_name).click()
            Select(wb.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wb = self.app.wb
        if text is not None:
            wb.find_element_by_name(field_name).click()
            wb.find_element_by_name(field_name).clear()
            wb.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wb = self.app.wb
        return len(wb.find_elements_by_name("selected[]"))