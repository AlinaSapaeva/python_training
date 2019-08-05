import time


class SessionHelper:
    def __init__(self,app):
        self.app=app

    def login(self, username, password):
        wb = self.app.wb
        self.app.open_home_page()
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(username)
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wb = self.app.wb
        wb.find_element_by_link_text("Logout").click()
        time.sleep(1)

    def ensure_logout(self):
        wb = self.app.wb
        if self.is_logget_in():
            self.logout()

    def is_logget_in(self):
        wb = self.app.wb
        return len(wb.find_elements_by_link_text("Logout"))>0

    def ensure_login(self, username, password):
        if self.is_logget_in():
            if self.is_logget_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)

    def is_logget_in_as(self, username):
        wb = self.app.wb
        return wb.find_element_by_xpath("//div/div[1]/form/b").text=="("+username+")"




