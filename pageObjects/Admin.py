import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Admin_In():

    def __init__(self, driver):
        self.driver = driver

    def Loggin_In(self, password):

        self.driver.find_element(By.NAME, "password").send_keys(password)

        time.sleep(1)

        self.driver.find_element(By.ID, "submit_button").click()

    def alert(self, order):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        if(order=="dismiss"):
            alert.dismiss()

    def verifying_page_message(self):

        message = self.driver.find_element(By.XPATH, "//div[@class='admin_text']").text
        assert "Items" in message

    def menu(self, option, operation, items, items_2):

        if(option=="items"):
            self.driver.find_element(By.ID, "1").click()
            time.sleep(1.5)
            if('post'==operation):
                items_form = self.driver.find_elements(By.CLASS_NAME, "book_form")
                items_dropdown = self.driver.find_elements(By.CLASS_NAME, "book_dropdown")

                for i,j in zip(items_form, items):
                   i.send_keys(j)
                   time.sleep(0.5)

                for k,l in zip(items_dropdown, items_2):
                   for option in k.find_elements(By.TAG_NAME, "option"):
                      if option.text==l:
                          option.click()
                          time.sleep(0.5)
    def submit(self):
        self.driver.find_element(By.ID, "submit_items").click()
