from selenium import webdriver
from fixtura.session import SessionHelper
from fixtura.group import GroupHelper
from fixtura.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wb = webdriver.Firefox()
        elif browser == "chrome":
            self.wb = webdriver.Chrome()
        elif browser == "ie":
            self.wb = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wb.implicitly_wait(10)
        self.session=SessionHelper(self)
        self.group=GroupHelper(self)
        self.contact=ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wb.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wb = self.wb
        wb.get(self.base_url)

    def return_home_page(self):
        wb = self.wb
        if not (wb.current_url.endswith('/addressbook/') and len(wb.find_elements_by_id("MassCB")) > 0):
            wb.find_element_by_link_text("home").click()

    def destroy(self):
        wb = self.wb
        self.wb.quit()


