from selenium.webdriver.support.select import Select
from model.contact import Contact

class ContactHelper:
    def __init__(self,app):
        self.app=app

    def add_new(self, contact):
        wb = self.app.wb
        self.app.return_home_page()
        self.open_create_contacts_page()
        self.fill_contact_form(contact)
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_home_page()
        self.contact_cache = None

    def open_create_contacts_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("add new").click()

    def delete_contact_by_index(self, index):
        wb = self.app.wb
        self.app.return_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wb.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wb.switch_to_alert().accept()
        wb.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wb = self.app.wb
        self.app.return_home_page()
        wb.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_data):
        self.modify_contact_by_index(new_data, 0)

    def modify_contact_by_index(self, new_data, index):
        wb = self.app.wb
        self.app.return_home_page()
        # submit editing
        wb.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_data)
        # submit update
        wb.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_home_page()
        self.contact_cache = None

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
        self.app.return_home_page()
        return len(wb.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wb = self.app.wb
            self.app.return_home_page()
            self.contact_cache = []
            for element in wb.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname =cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)
