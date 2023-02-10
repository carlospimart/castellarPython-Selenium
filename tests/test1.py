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

        time.sleep(1)

        admin_logging.verifying_page_message()

        items = ["Nada", 1988, 3.5,"Austral","Good",
                 "Se trata de una obra existencialista que representa el estancamiento y la pobreza que se vivieron en la posguerra española, durante los primeros años del franquismo.",
                 "Paperback"]
        items_2 = ["Spanish", "Carmen Laforet"]
        admin_logging.menu("items","post", items, items_2)
        time.sleep(1)
        admin_logging.submit()
        time.sleep(2)
        log.info("Test successful")

