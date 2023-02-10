import time
from selenium.webdriver.common.by import By

class Log_in():

    def __init__(self, driver):
        self.driver = driver

    def Loggin_In(self, user, password):

        self.driver.find_element(By.NAME, "username").send_keys(user)

        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(password)

        time.sleep(1)

        self.driver.find_element(By.ID, "submit_button").click()