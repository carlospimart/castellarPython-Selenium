import time

from selenium.webdriver.common.by import By

from pageObjects.Log_in import Log_in
from pageObjects.Admin import Admin_In
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass



class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator_text):

        self.driver.find_element(by, locator_text).click()

    sign = (By.ID, "sign_in_text")
    admin = (By.CLASS_NAME, "site-title")

    def sign_in(self):

        self.driver.find_element(*HomePage.sign).click()  # we use asterix because we are dealing with a tuple
        log_in = Log_in(self.driver)  # we create an instance of CheckOutPage
        return log_in

    def admin_in(self):
        self.driver.find_element(*HomePage.admin).click()  # we use asterix because we are dealing with a tuple
        admin_in = Admin_In(self.driver)  # we create an instance of CheckOutPage
        return admin_in

    def alert(self, order):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        if(order=="dismiss"):
            alert.dismiss()
    def verifying_page_message(self):

        message = self.driver.find_element(By.XPATH, "//div[@class='home_text']").text
        assert "THIS IS THE HOME PAGE" in message
