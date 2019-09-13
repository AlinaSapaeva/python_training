from selenium.webdriver.support.select import Select
from model.contact import Contact
import re

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

    def select_contact_by_id(self, id):
        wb = self.app.wb
        wb.find_element_by_id(id).click()

    def delete_contact_by_id(self, id):
        wb = self.app.wb
        self.app.return_home_page()
        self.select_contact_by_id(id)
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
       # wb.find_element_by_css_selector("input[value = '%s']" % id).click()
        self.fill_contact_form(new_data)
        # submit update
        wb.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_home_page()
        self.contact_cache = None

    def add_contact_to_group(self, id_group, id_contact):
        wb = self.app.wb
        self.app.return_home_page()
        wb.find_element_by_css_selector("input[value = '%s']" % id_contact).click()
        groups = Select(wb.find_element_by_name("to_group"))
        groups.select_by_value("%s" % id_group)
        wb.find_element_by_name("add").click()
        self.app.return_home_page()

    def delete_group_in_contact(self, id_group, id_contact):
        wb = self.app.wb
        self.app.return_home_page()
        groups = Select(wb.find_element_by_name("group"))
        groups.select_by_value("%s" % id_group)
        wb.find_element_by_css_selector("input[value = '%s']" % id_contact).click()
        wb.find_element_by_name("remove").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
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
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                 all_phones_from_home_page = all_phones,
                                                 address = address, all_emails__from_home_page =all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wb = self.app.wb
        self.app.return_home_page()
        wb.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        lastname = wb.find_element_by_name("lastname").get_attribute("value")
        firstname = wb.find_element_by_name("firstname").get_attribute("value")
        id = wb.find_element_by_name("id").get_attribute("value")
        homephone = wb.find_element_by_name("home").get_attribute("value")
        mobilephone = wb.find_element_by_name("mobile").get_attribute("value")
        workphone = wb.find_element_by_name("work").get_attribute("value")
        phone2 = wb.find_element_by_name("phone2").get_attribute("value")
        address = wb.find_element_by_name("address").get_attribute("value")
        email  = wb.find_element_by_name("email").get_attribute("value")
        email2  = wb.find_element_by_name("email2").get_attribute("value")
        email3  = wb.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, homephone = homephone,
                       mobilephone = mobilephone, workphone = workphone, phone2=phone2, address = address,
                       email=email, email2=email2, email3=email3)

#    def get_contact_from_view_page(self, index):
#       wb = self.app.wb
#        wb.find_elements_by_xpath("//img[@alt='Details']")[index].click()
#       text = wb.find_elements_by_id("content").text
#        homephone = re.search("H: (.*)", text).group(1)
#        mobilephone = re.search("M: (.*)", text).group(1)
#        workphone = re.search("W: (.*)", text).group(1)
#        phone2 = re.search("P: (.*)", text).group(1)
 #       return Contact(mobilephone=mobilephone, workphone=workphone, phone2=phone2)








