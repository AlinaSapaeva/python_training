from selenium.webdriver.support.select import Select
import os

class ContactHelper:
    def __init__(self,app):
        self.app=app

    def add_new(self, contact):
        wb = self.app.wb
        self.open_create_contacts_page()
        self.fill_contact_form(contact)
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_home_page()

    def fill_contact_form(self, contact):
        wb = self.app.wb
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(contact.firstname)
        wb.find_element_by_name("middlename").click()
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys(contact.middlename)
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(contact.lastname)
        wb.find_element_by_name("nickname").click()
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(contact.nickname)
        image = os.path.abspath('rr.jpg')
        wb.find_element_by_xpath("//input[@type='file']").clear()
        wb.find_element_by_xpath("//input[@type='file']").send_keys(image)
        wb.find_element_by_name("title").click()
        wb.find_element_by_name("title").clear()
        wb.find_element_by_name("title").send_keys(contact.title)
        wb.find_element_by_name("company").click()
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(contact.company)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(contact.address)
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(contact.home)
        wb.find_element_by_name("mobile").click()
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys(contact.mobile)
        wb.find_element_by_name("work").click()
        wb.find_element_by_name("work").clear()
        wb.find_element_by_name("work").send_keys(contact.work)
        wb.find_element_by_name("fax").click()
        wb.find_element_by_name("fax").clear()
        wb.find_element_by_name("fax").send_keys(contact.fax)
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(contact.email)
        wb.find_element_by_name("email2").click()
        wb.find_element_by_name("email2").clear()
        wb.find_element_by_name("email2").send_keys(contact.email2)
        wb.find_element_by_name("email3").click()
        wb.find_element_by_name("email3").clear()
        wb.find_element_by_name("email3").send_keys(contact.email3)
        wb.find_element_by_name("homepage").click()
        wb.find_element_by_name("homepage").clear()
        wb.find_element_by_name("homepage").send_keys(contact.homepage)
        wb.find_element_by_name("bday").click()
        Select(wb.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wb.find_element_by_name("bmonth").click()
        Select(wb.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wb.find_element_by_name("byear").click()
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys(contact.byear)
        wb.find_element_by_name("aday").click()
        Select(wb.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wb.find_element_by_name("amonth").click()
        Select(wb.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wb.find_element_by_name("ayear").click()
        wb.find_element_by_name("ayear").clear()
        wb.find_element_by_name("ayear").send_keys(contact.ayear)
        wb.find_element_by_name("address2").click()
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(contact.address2)
        # wb.find_element_by_name("new_group").click()
        # wb.find_element_by_name("theform").click()
        wb.find_element_by_name("phone2").click()
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(contact.phone2)
        wb.find_element_by_name("notes").click()
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(contact.notes)

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
        self.change_field_value("contact_firstname", contact.firstname)
        self.change_field_value("contact_middlename", contact.middlename)
        self.change_field_value("contact_lastname", contact.lastname)
        self.change_field_value("contact_nickname", contact.nickname)
        self.change_field_value("contact_title", contact.title)
        self.change_field_value("contact_company", contact.company)
        self.change_field_value("contact_address", contact.address)
        self.change_field_value("contact_home", contact.home)
        self.change_field_value("contact_mobile", contact.mobile)
        self.change_field_value("contact_work", contact.work)
        self.change_field_value("contact_fax", contact.fax)
        self.change_field_value("contact_email", contact.email)
        self.change_field_value("contact_email2", contact.email2)
        self.change_field_value("contact_email3", contact.email3)
        self.change_field_value("contact_bday", contact.bday)
        self.change_field_value("contact_bmonth", contact.bmonth)
        self.change_field_value("contact_byear", contact.byear)
        self.change_field_value("contact_aday", contact.aday)
        self.change_field_value("contact_amonth", contact.amonth)
        self.change_field_value("contact_ayear", contact.ayear)
        self.change_field_value("contact_address2", contact.address2)
        self.change_field_value("contact_phone2", contact.phone2)
        self.change_field_value("contact_notes", contact.notes)

    def change_field_value(self, field_name, text):
        wb = self.app.wb
        if text is not None:
            wb.find_element_by_name(field_name).click()
            wb.find_element_by_name(field_name).clear()
            wb.find_element_by_name(field_name).send_keys(text)

