from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage

import time

from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_Form(self):

        log = self.getLogger()

        log.info("Let's start the test...")
        homepage = HomePage(self.driver)

        time.sleep(1)

        loggin_in = homepage.sign_in()
        time.sleep(1)

        log.info("Logging In...")

        loggin_in.Loggin_In("carlospimart","bonpassdemot")

        time.sleep(3)

        log.info("Succesfully Logged")

        homepage.alert("dismiss")

        time.sleep(3)

        homepage.verifying_page_message()

        time.sleep(1)

        admin_logging = homepage.admin_in()

        time.sleep(1)

        admin_logging.Loggin_In("Aquiescencia820338$")

        time.sleep(1)

        admin_logging.alert("dismiss")

        author = ["Carmen", "", "Laforet", "Spain"]

        admin_logging.menu("author", "post", author, None)

        time.sleep(2)

        admin_logging.alert("dismiss")

        time.sleep(2)
