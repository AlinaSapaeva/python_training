from selenium.webdriver.firefox.webdriver import WebDriver
from fixtura.session import SessionHelper
from fixtura.group import GroupHelper
from fixtura.contact import ContactHelper


class Application:
    def __init__(self):
        self.wb = WebDriver()
        self.wb.implicitly_wait(5)
        self.session=SessionHelper(self)
        self.group=GroupHelper(self)
        self.contact=ContactHelper(self)

    def is_valid(self):
        try:
            self.wb.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wb = self.wb
        wb.get("http://localhost/addressbook/")

    def return_home_page(self):
        wb = self.wb
        wb.find_element_by_link_text("home").click()

    def destroy(self):
        wb = self.wb
        self.wb.quit()


