import time

from selenium.webdriver.common.by import By

from pageObjects.Log_in import Log_in
from pageObjects.Admin import Admin_In
from pageObjects.Search_page import Search_page
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass



class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator_text):

        self.driver.find_element(by, locator_text).click()

    home = (By.ID, "home_button")
    sign = (By.ID, "sign_in_text")
    admin = (By.CLASS_NAME, "site-title")
    search_textbox = (By.CLASS_NAME, "Bar")
    search_button = (By.CLASS_NAME, "search_submit")

    def home_page(self):
        self.driver.find_element(*HomePage.home).click()  # we use asterix because we are dealing with a tuple

    def sign_in(self):

        self.driver.find_element(*HomePage.sign).click()  # we use asterix because we are dealing with a tuple
        log_in = Log_in(self.driver)  # we create an instance of CheckOutPage
        return log_in

    def admin_in(self):
        self.driver.find_element(*HomePage.admin).click()
        admin_in = Admin_In(self.driver)
        return admin_in

    def alert(self, order):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        if(order=="dismiss"):
            alert.dismiss()
    def verifying_page_message(self, path, message_text):

        message = self.driver.find_element(By.XPATH, path).text
        assert message_text in message

    def search(self, item):
        self.driver.find_element(*HomePage.search_textbox).send_keys(item) # we use asterix because we are dealing with a tuple
        time.sleep(1)
        self.driver.find_element(*HomePage.search_button).click()
        search_instance = Search_page(self.driver)  # we create an instance of CheckOutPage
        return search_instance

