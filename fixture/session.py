



class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Enter_Login(self, Login, Password):
        driver = self.app.driver
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(Login)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(Password)
        driver.find_element_by_id("LoginForm").submit()
