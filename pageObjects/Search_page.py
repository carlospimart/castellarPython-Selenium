import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.BaseClass import BaseClass
class Search_page(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def verifying_page_message(self, path, message_text):
        log = self.getLogger()
        message = self.driver.find_element(By.XPATH, path).text
        assert message_text in message, "The title provide is not present in the page"
        log.info("The new title has been found. The book was added")




